# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from datetime import date, timedelta

from odoo import models


class ProjectProject(models.Model):
    _inherit = "project.project"

    def action_view_sprints(self):
        self.ensure_one()
        action = self.env["ir.actions.actions"]._for_xml_id("project_scrum.action_ps_sprint_current")
        action["context"] = {
            "default_project_id": self.id,
            "search_default_project_id": [self.id],
            "group_by": "state",
        }
        action["domain"] = [("project_id", "=", self.id)]
        return action

    def _cronograma_sprints(self):
        self.ensure_one()
        return self.sprint_ids.sorted(key=lambda s: (s.date_start or date.max, s.id))

    def _cronograma_data(self):
        self.ensure_one()
        fases = self._cronograma_sprints()
        hitos = self.milestone_ids.sorted(
            key=lambda m: (m.deadline or date.max, m.id)
        )

        fechas = []
        if self.date_start:
            fechas.append(self.date_start)
        if self.date:
            fechas.append(self.date)
        for f in fases:
            if f.date_start:
                fechas.append(f.date_start)
            if f.date_stop:
                fechas.append(f.date_stop)
        for h in hitos:
            if h.deadline:
                fechas.append(h.deadline)

        semanas = []
        if fechas:
            inicio, fin = min(fechas), max(fechas)
            cursor = inicio - timedelta(days=inicio.weekday())
            n = 1
            while cursor <= fin:
                semanas.append(
                    {
                        "label": "Semana %d" % n,
                        "inicio": cursor,
                        "fin": cursor + timedelta(days=6),
                    }
                )
                cursor += timedelta(days=7)
                n += 1
        else:
            semanas = [
                {"label": "Semana %d" % (i + 1), "inicio": None, "fin": None}
                for i in range(len(fases))
            ]

        def semana_index(d):
            if not d:
                return None
            for i, s in enumerate(semanas):
                if s["inicio"] and s["inicio"] <= d <= s["fin"]:
                    return i
            return None

        fase_rows = []
        for i, f in enumerate(fases):
            start = f.date_start
            end = f.date_stop
            col_start = semana_index(start)
            col_end = semana_index(end)
            if col_start is None and col_end is None:
                col_start = col_end = i
            elif col_start is None:
                col_start = col_end
            elif col_end is None:
                col_end = col_start
            fase_rows.append(
                {
                    "name": f.name,
                    "col_start": col_start,
                    "col_end": col_end,
                    "subtasks": f.task_ids.mapped("name"),
                }
            )

        hito_rows = []
        for h in hitos:
            estado = (
                "Alcanzado"
                if h.is_reached
                else "Vencido"
                if h.is_deadline_exceeded
                else "Pendiente"
            )
            hito_rows.append(
                {
                    "name": h.name,
                    "deadline": h.deadline,
                    "col": semana_index(h.deadline),
                    "estado": estado,
                }
            )

        return {
            "semanas": semanas,
            "fases": fase_rows,
            "hitos": hito_rows,
            "hito_cols": {h["col"] for h in hito_rows if h["col"] is not None},
        }

    def copy(self, default=None):
        new_projects = super().copy(default=default)
        for old_project, new_project in zip(self, new_projects):
            if not old_project.sprint_ids:
                continue
            sprint_mapping = {}
            for old_sprint in old_project.sprint_ids:
                new_sprint = old_sprint.copy({"project_id": new_project.id, "us_ids": False})
                sprint_mapping[old_sprint.id] = new_sprint.id
            for task in new_project.task_ids:
                if task.sprint_id and task.sprint_id.id in sprint_mapping:
                    task.sprint_id = sprint_mapping[task.sprint_id.id]
        return new_projects

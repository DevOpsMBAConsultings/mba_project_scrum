# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    use_scrum = fields.Boolean(readonly=True)
    notes = fields.Html(string="Notas de la tarea")

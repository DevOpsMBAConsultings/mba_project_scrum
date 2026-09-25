# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class ProjectScrumSprint(models.Model):
    _inherit = "project.scrum.sprint"
    _order = "sequence, date_start, id"

    description = fields.Html(string="Descripción")
    notes = fields.Html(string="Notas del Sprint")

    def action_start(self):
        self.write({"state": "open"})

    def action_pause(self):
        self.write({"state": "pending"})

    def action_done(self):
        self.write({"state": "done"})

    def action_cancel(self):
        self.write({"state": "cancel"})

    def action_draft(self):
        self.write({"state": "draft"})

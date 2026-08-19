# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import api, fields, models


class ProjectScrumUs(models.Model):
    _inherit = "project.scrum.us"

    # --- Flujo de Estados / Ciclo de Vida ---
    state = fields.Selection(
        [
            ("draft", "Borrador / Backlog"),
            ("refinement", "Refinamiento"),
            ("ready", "Listo para Sprint"),
            ("in_progress", "En Progreso"),
            ("testing", "En Pruebas / QA"),
            ("done", "Aprobado / Listo"),
            ("cancelled", "Cancelado"),
        ],
        string="Estado",
        default="draft",
        tracking=True,
        index=True,
    )

    # --- Narrativa Ágil Estructurada ---
    role = fields.Char(
        string="Como (Rol / Actor)",
        help="Ej. Contador, Cajero POS, Gerente de Ventas, Administrador de Almacén",
    )
    want = fields.Text(
        string="Quiero (Objetivo / Funcionalidad)",
        help="Acción o funcionalidad concreta requerida en el sistema",
    )
    benefit = fields.Text(
        string="Para (Beneficio / Valor)",
        help="Razón de negocio o valor que aporta esta historia",
    )

    # --- Criterios de Aceptación & DoD ---
    acceptance_criteria = fields.Html(
        string="Criterios de Aceptación (Escenarios BDD)",
        help="Escenarios estructurados: Dado que... / Cuando... / Entonces...",
    )
    definition_of_done = fields.Html(
        string="Definition of Done (DoD)",
        help="Condiciones técnicas y funcionales que deben cumplirse antes de dar la historia por terminada",
    )

    # --- Clasificación Odoo ---
    odoo_module_category = fields.Selection(
        [
            ("invoicing_fe", "Facturación / FE Panamá (PAC)"),
            ("sale_crm", "Ventas / CRM"),
            ("purchase", "Compras / Proveedores"),
            ("stock", "Inventario / Almacén"),
            ("account_oca", "Contabilidad & Finanzas (OCA)"),
            ("pos", "Punto de Venta (POS)"),
            ("bi_dashboard", "BI Dashboard & Reportes"),
            ("mrp", "Fabricación / MRP"),
            ("project", "Proyectos / Servicios"),
            ("hr_payroll", "Recursos Humanos / Nómina"),
            ("other", "Otro"),
        ],
        string="Módulo Odoo",
        index=True,
    )
    request_type = fields.Selection(
        [
            ("feature", "Feature / Nueva Funcionalidad"),
            ("improvement", "Mejora Funcional"),
            ("bug", "Bug / Defecto"),
            ("gap", "GAP / Personalización"),
            ("technical_debt", "Deuda Técnica"),
            ("spike", "Spike / Investigación"),
        ],
        string="Tipo de Requerimiento",
        default="feature",
        index=True,
    )
    solution_type = fields.Selection(
        [
            ("standard", "Estándar Odoo (Sin código)"),
            ("mba_custom", "Módulo Propio (mba_*)"),
            ("oca_module", "Módulo Comunitario (OCA)"),
            ("data_migration", "Carga de Datos / Migración"),
            ("external_integration", "Integración Externa (PAC / Banco / API)"),
        ],
        string="Tipo de Solución",
        default="mba_custom",
    )
    golive_criticality = fields.Selection(
        [
            ("blocking", "🔴 Bloqueante para Go-Live"),
            ("desirable", "🟡 Deseable antes de Go-Live"),
            ("post_golive", "🟢 Post Go-Live"),
        ],
        string="Criticidad Go-Live",
        default="desirable",
        index=True,
    )
    environment = fields.Selection(
        [
            ("local_dev", "Desarrollo Local"),
            ("staging", "Servidor Staging / UAT"),
            ("prod", "Servidor Producción"),
        ],
        string="Entorno / Servidor",
        default="staging",
    )

    # --- Ficha Técnica Odoo (Para el Desarrollador) ---
    technical_module_repo = fields.Char(
        string="Módulo Técnico / Repo",
        help="Ej. mba_pa_edi_hka, mba_bi_dashboard, mba_pos_invoice_status",
    )
    inherited_models = fields.Char(
        string="Modelos Heredados / Nuevos",
        help="Ej. account.move, sale.order, pos.order, res.partner",
    )
    technical_specs = fields.Text(
        string="Campos, Vistas XPath & Lógica Técnica",
        help="Detalles de diseño técnico, hooks, vistas y métodos a implementar",
    )

    # --- Estimación Ágil ---
    story_points = fields.Selection(
        [
            ("1", "1 SP"),
            ("2", "2 SP"),
            ("3", "3 SP"),
            ("5", "5 SP"),
            ("8", "8 SP"),
            ("13", "13 SP"),
            ("21", "21 SP"),
        ],
        string="Story Points",
    )

    # --- Acciones de Transición de Estado ---
    def action_set_draft(self):
        self.write({"state": "draft"})

    def action_set_refinement(self):
        self.write({"state": "refinement"})

    def action_set_ready(self):
        self.write({"state": "ready"})

    def action_set_in_progress(self):
        self.write({"state": "in_progress"})

    def action_set_testing(self):
        self.write({"state": "testing"})

    def action_set_done(self):
        self.write({"state": "done"})

    def action_set_cancelled(self):
        self.write({"state": "cancelled"})

# MBA - Project Scrum User Stories Enhancements (`mba_project_scrum`)

Módulo de extensión agnóstico para Odoo 18 Community que enriquece el modelo `project.scrum.us` (`project_scrum` de OCA) con una estructura orientada a implementaciones y desarrollos en Odoo.

## Características Principales

1. **Pipeline de Estados (Statusbar):**
   - `Borrador / Backlog` ➔ `Refinamiento` ➔ `Listo para Sprint` ➔ `En Progreso` ➔ `En Pruebas / QA` ➔ `Aprobado / Listo (Done)` ➔ `Cancelado`.
2. **Narrativa Ágil Estructurada:**
   - **Como:** Rol / Persona (Contador, Cajero POS, etc.).
   - **Quiero:** Objetivo / Requerimiento funcional.
   - **Para:** Beneficio / Valor de negocio.
3. **Criterios de Aceptación (BDD & DoD):**
   - Plantilla de escenarios *Dado que... / Cuando... / Entonces...*.
   - Checklist de *Definition of Done*.
4. **Clasificación Funcional Odoo:**
   - Módulos Odoo (Facturación FE, Ventas, Compras, Inventario, Contabilidad OCA, POS, BI Dashboard, MRP, Proyectos, RRHH).
   - Tipo de Requerimiento (Feature, Mejora, Bug, GAP, Deuda Técnica, Spike).
   - Tipo de Solución (Estándar, Módulo Propio `mba_*`, Módulo OCA, Carga de Datos, Integración Externa).
   - Criticidad Go-Live (🔴 Bloqueante, 🟡 Deseable, 🟢 Post Go-Live).
   - Entorno de Despliegue (Local, Staging / UAT, Producción).
5. **Ficha Técnica para Desarrolladores:**
   - Módulo técnico / Repositorio (`mba_pa_edi_hka`, `mba_bi_dashboard`, etc.).
   - Modelos heredados o nuevos (`_inherit` / `_name`).
   - Especificaciones de Vistas XPath, campos y lógica técnica.
6. **Métricas y Estimación:**
   - Story Points (Fibonacci: 1, 2, 3, 5, 8, 13, 21).

## Dependencias
- `project` (Odoo Core)
- `project_scrum` (OCA `project-agile`)

## Autor
- MBA Consultings (<https://www.mbaconsultings.com>)

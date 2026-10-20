---
id: HU-CONN-06
titulo: BYOK de producción con registro de número y promoción
spec: SPEC-08
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: M
impacto: [ingreso, confianza]
req: [REQ-CONN-03]
dependencias: [HU-CONN-01, HU-CONN-05]
skills: ["deep-research", "frontend-design", "built-in-browser", "meta-whatsapp", "panel-ui"]
ola: 3
estado: borrador
---

# HU-CONN-06 · BYOK de producción con registro de número y promoción

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-08](../spec.md).

**ID:** HU-CONN-06

**Título:** BYOK de producción con registro de número y promoción

**Workstream:** Canales y conexiones

**Historia:** Como negocio que ya tiene su app de Meta quiero conectar mi número de producción con mis credenciales, registrarlo con PIN y pasar de prueba a producción desde el panel para atender clientes reales sin depender de Embedded Signup.

**Por qué importa (valor empresarial):** Hoy BYOK queda siempre en sandbox (`meta_byok.py:97`), así que no hay ningún camino de producción que funcione. Es también el respaldo si Meta tarda en aprobar a SolversHub como Tech Provider (R-01): sin esta HU, el Hito 0A depende de un tercero.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-CONN-03

**Dependencias:** [HU-CONN-01](HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-05](HU-CONN-05-webhook-por-conexion.md)

**Criterios de aceptación (Gherkin):**
- **Elegir entorno.** Dado el wizard BYOK, cuando elijo "Producción", entonces la conexión se guarda con `environment = production`.
- **Registro del número.** Dado un número de producción sin registrar, cuando ingreso el PIN, entonces se registra en la Cloud API y queda `conectada`.
- **Promoción.** Dado una conexión BYOK de prueba, cuando pulso "Pasar a producción", entonces el panel guía el cambio (número real, registro, plantillas) y al terminar el entorno cambia.
- **Chequeos de su app.** Dado una conexión BYOK de producción, cuando corre el checklist, entonces evalúa la app del negocio, no la de la plataforma.

**Evidencia / Definición de Terminado:**
- Alta BYOK de producción real documentada; tests del wizard con entorno.

**Riesgos/Notas:**
- El modelo de la API del wizard hoy no tiene campo de entorno (`meta_wizard.py:164-170`).

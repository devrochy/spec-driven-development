---
id: HU-APP-12
titulo: "Configuración móvil: colaboradores, habilidades, conexiones y ajustes"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [confianza, operacion]
req: [REQ-APP-07]
dependencias: [HU-APP-03]
skills: [frontend-design, backend-design:security-discipline]
estado: terminada
---

# HU-APP-12 · Configuración móvil: colaboradores, habilidades, conexiones y ajustes

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-12

**Título:** Configuración móvil: colaboradores, habilidades, conexiones y ajustes

**Workstream:** App móvil

**Historia:** Como dueño quiero administrar desde la app a mis colaboradores (invitar, asignar permisos, activar/desactivar, restablecer contraseña), activar o desactivar habilidades, ver el estado de mis conexiones de WhatsApp y ajustar la configuración de mi negocio, para que el control administrativo no dependa del escritorio.

**Por qué importa (valor empresarial):** El dueño necesita resolver "agregué un vendedor" o "el WhatsApp no responde" sin abrir un computador. La configuración móvil es la sección que más confianza genera en el control del negocio y cierra la réplica del panel.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-07

**Dependencias:** [HU-APP-03](HU-APP-03-navegacion-por-permisos.md)

**Criterios de aceptación (Gherkin):**
- **Colaboradores.** Dado un dueño, cuando abre Colaboradores, entonces ve las cuentas con rol, estado y permisos por sección, puede invitar, activar/desactivar y restablecer contraseña (acciones del panel, con confirmación para las irreversibles).
- **Habilidades.** Dado un dueño, cuando abre Habilidades, entonces ve el catálogo con estado y puede activar/desactivar y editar configuración con el formulario por JSON Schema (los secretos nunca salen del backend).
- **Conexiones.** Dado un dueño, cuando abre Conexiones, entonces ve estado/salud de cada conexión, puede marcar principal, activar/desactivar y re-suscribir el WABA; los wizards OAuth se abren en browser/webview con retorno a la app.
- **Ajustes.** Dado un dueño, cuando abre Ajustes, entonces ve las pestañas del panel (Identidad, Cerebro, Memoria, Habilidades, Chat web, Avanzado) en formato móvil con guardado y errores explícitos.
- **Permisos.** Dado un colaborador sin permiso de colaboradores (solo owner/master), cuando navega, entonces no ve la sección.

**Evidencia / Definición de Terminado:**
- `modules/configuracion/` contra `/api/v1/admin/collaborators`, `/admin/plugins`, `/admin/connections` y `/admin/settings`; formulario JSON Schema reutilizado del patrón del panel; tests unitarios y de render; captura en dev client.

**Implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — configuración móvil (colaboradores, habilidades, conexiones).

**Riesgos/Notas:**
- Los wizards completos de Embedded Signup/BYOK son flujos largos: en la v1 móvil se llevan al navegador externo con deep link de retorno; la app muestra estado y checklist.
- El panel SSR legado (`/legacy`) no se replica: todo va contra `/api/v1`.

**App implementada (2026-10-06):** [solvershub-apk #117](https://github.com/devrochy/solvershub-apk/pull/117) — `modules/configuracion`: colaboradores (activar/desactivar con confirmación), habilidades (activar/desactivar) y conexiones (estado). Wizards OAuth y formularios de configuración completos quedan en web (deuda). 3 tests.

**Chat web y Avanzado en la app (2026-10-08):** [solvershub-apk #140](https://github.com/devrochy/solvershub-apk/pull/140).
Son las dos pestañas de Ajustes que habían quedado solo en web. Ahora son sub-pestañas de Ajustes, cada una con su propio guardado:
- **Chat web**: activar el widget, dominios permitidos, secreto de Turnstile (vacío = se conserva el
  actual), rotar la clave y compartir el fragmento.
- **Avanzado**: versiones del agente (activar con confirmación), LLM y llave BYOK (vacía = se conserva),
  guardrails con aviso de las líneas ignoradas, flow y evals de solo lectura, y el editor del
  AgentSpec (valida el JSON y pide confirmación antes de reemplazarlo).

Tiene 10 tests nuevos. Verificado en el OPPO contra test: las dos pestañas cargan datos reales.
Avanzado mostró una herramienta desconocida en el flow de Cobranza Demo: `generar_link_pago`.
Con esto, Ajustes cubre todas las pestañas del panel.

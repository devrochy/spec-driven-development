---
id: HU-SH-06
titulo: Onboarding autoservicio desde la invitación hasta el primer mensaje
spec: SPEC-07
fase: 0
hito: 0A
workstream: UX/Onboarding
prioridad: P0
critico: true
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-SH-05, REQ-UX-02, REQ-COMP-08]
dependencias: [HU-SH-03, HU-UI-02]
skills: ["frontend-design", "built-in-browser", "marketing:email-sequence", "panel-ui"]
ola: 4
estado: en-curso
---

# HU-SH-06 · Onboarding autoservicio desde la invitación hasta el primer mensaje

> Estado SDD: En curso. Implementada y mergeada el 2026-10-09 ([core #349](https://github.com/devrochy/agent-core/pull/349) + [panel #48](https://github.com/devrochy/solvershub-panel/pull/48)); falta desplegarla en test, verificar los criterios y hacer la prueba con un usuario sin contexto.

**ID:** HU-SH-06

**Título:** Onboarding autoservicio desde la invitación hasta el primer mensaje

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio recién creado quiero que, al aceptar la invitación, el panel me guíe paso a paso (datos del negocio, conectar WhatsApp, cargar mi catálogo o servicios, probar el asistente, invitar a mi equipo) para dejar mi asistente funcionando el mismo día.

**Por qué importa (valor empresarial):** El alta automática solo convierte si el cliente llega a su primer mensaje real. Cada paso sin guía es un abandono y un ticket de soporte. "Listo en minutos" es la promesa de Visito y Wati; aquí se mide.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** L

**REQ mapeados:** REQ-SH-05, REQ-UX-02, REQ-COMP-08

**Dependencias:** [HU-SH-03](HU-SH-03-aprovisionamiento-automatico.md), [HU-UI-02](../../SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md)

**Criterios de aceptación (Gherkin):**
- **Invitación.** Dado el enlace de invitación, cuando lo abro, entonces defino mi contraseña y entro a mi negocio (ADR-0081).
- **Primeros pasos calculados.** Dado mi negocio nuevo, cuando entro al Resumen, entonces veo un checklist calculado del estado real: datos del negocio, WhatsApp conectado y verificado, catálogo o servicios, probar el asistente, equipo invitado; cada paso marca su avance solo.
- **Tour.** Dado mi primera visita, cuando acepto el tour, entonces recorro 5 pasos accesibles por teclado y puedo saltarlo.
- **Packs pendientes.** Dado un pack que quedó "pendiente de configurar" (por ejemplo pagos), cuando entro, entonces aparece como paso con su explicación.
- **Medición.** Dado cada paso completado, cuando ocurre, entonces se registra el tiempo desde el alta para medir el embudo de activación.

**Evidencia / Definición de Terminado:**
- Endpoint de estado de primeros pasos; componente en el Resumen; métricas del embudo; prueba con un usuario sin contexto.

**Riesgos/Notas:**
- Los modales de ayuda y las guías por habilidad llegan en [SPEC-12](../../../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md).

**Avance (2026-10-09):**
- ADR-0124 «Primeros pasos calculados y embudo de activación»: el canje de la invitación abre la sesión (enmienda ADR-0121 § 3.8).
- Panel: páginas `/invitacion` y `/recuperar`, invitaciones pendientes al entrar, checklist en el Resumen y tour de 5 pasos.
- Backend: `GET /api/v1/admin/onboarding`, tabla `onboarding_hitos` (migración `0062`) y CLI `agent-core tenant embudo`.
- Revisión de seguridad corregida: bloqueo progresivo en el reset de contraseña, cupo de pedidos de código y cierre de la sesión anterior al canjear.
- **Para verificar en test:** `SYSTEM_SMTP_*` configurado y la prueba con un usuario sin contexto (el guion está en panel #48).
- **Guía de prueba en test:** [guia-de-prueba-alta-automatica.md](../guia-de-prueba-alta-automatica.md).

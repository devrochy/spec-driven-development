---
id: HU-ARCH-11
titulo: Una burbuja por respuesta por defecto y estilo editable
spec: SPEC-02
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: S
impacto: [ingreso, confianza]
req: [REQ-ARCH-18]
dependencias: []
skills: ["optimizer", "eval-runner", "frontend-design"]
ola: 1
estado: terminada
---

# HU-ARCH-11 · Una burbuja por respuesta por defecto y estilo editable

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-02](../spec.md).

**ID:** HU-ARCH-11

**Título:** Una burbuja por respuesta por defecto y estilo editable

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de un negocio quiero que el asistente responda en un solo mensaje por defecto y poder cambiarlo en Configuración para no pagarle a Meta tres mensajes por cada respuesta.

**Por qué importa (valor empresarial):** Desde el 2026-10-01 Meta cobra cada mensaje de servicio. Con `pocos_cortos` (`core/config.py:143`) una conversación de 8 turnos cuesta (cifra interna) en Meta contra (cifra interna) con un solo mensaje: el cliente ahorra dos tercios sin perder nada.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-ARCH-18

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Nuevo valor por defecto.** Dado un negocio nuevo, cuando se crea, entonces su estilo de envío es `un_mensaje`.
- **Negocios existentes.** Dado un negocio que nunca cambió el estilo, cuando se despliega, entonces pasa a `un_mensaje`; si lo eligió explícitamente, se respeta.
- **Editable con explicación.** Dado Configuración del panel, cuando el dueño cambia el estilo, entonces ve cuántos mensajes de Meta implica cada opción.
- **Mensajes largos.** Dado una respuesta que supera el límite de WhatsApp, cuando se envía con `un_mensaje`, entonces se parte solo por límite técnico.

**Evidencia / Definición de Terminado:**
- Migración de datos auditada y test del splitter.
- Captura del selector en Configuración.

**Implementada (2026-10-02):**
- Backend (PR #186 en `devrochy/agent-core`): default `MESSAGE_SPLIT_STYLE=un_mensaje`; `un_mensaje` parte solo por el límite técnico de WhatsApp (4096); `split_style` en `/settings/identity` con validación; migración `0044` que fija `un_mensaje` en negocios que no lo eligieron (auditado) y respeta a los que sí.
- Panel (PR #7): selector "Estilo de envío" en Configuración › Identidad, con cuántos mensajes cobra Meta por opción.
- Tests: splitter (límite técnico), default global y guardado del endpoint; gates de backend y panel verdes.

**Riesgos/Notas:**
- Fuente del cambio de Meta: fuentes-externas.md.

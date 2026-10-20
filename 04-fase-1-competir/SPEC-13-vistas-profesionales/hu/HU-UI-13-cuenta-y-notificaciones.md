---
id: HU-UI-13
titulo: Cuenta, recuperación de contraseña y notificaciones a operadores
spec: SPEC-13
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: L
impacto: [operacion, confianza]
req: [REQ-UX-07]
dependencias: [HU-UI-03]
skills: ["backend-design:auth-and-authorization", "backend-design:security-reviewer", "frontend-design", "panel-ui"]
estado: parqueada
---

# HU-UI-13 · Cuenta, recuperación de contraseña y notificaciones a operadores

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-13](../spec.md).

**ID:** HU-UI-13

**Título:** Cuenta, recuperación de contraseña y notificaciones a operadores

**Workstream:** UX/Onboarding

**Historia:** Como colaborador quiero gestionar mi perfil, recuperar mi contraseña yo mismo y elegir cómo me avisan de tickets, pedidos y comprobantes para trabajar sin depender del administrador.

**Por qué importa (valor empresarial):** Hoy no existe recuperación de contraseña (cada olvido es un ticket) ni avisos al equipo (los tickets esperan a que alguien abra el panel). Las notificaciones son las que hacen que el humano llegue a tiempo cuando el asistente escala.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-UX-07

**Dependencias:** [HU-UI-03](../../../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md)

**Criterios de aceptación (Gherkin):**
- **Recuperar contraseña.** Dado mi correo, cuando pido recuperar, entonces recibo un enlace de un solo uso y con vencimiento, y el intento queda limitado contra abuso.
- **Perfil.** Dado mi perfil, cuando lo abro, entonces cambio nombre, contraseña y preferencias de tema.
- **Preferencias.** Dado mis notificaciones, cuando elijo canales por tipo de evento, entonces recibo solo lo elegido por WhatsApp (plantilla), correo o campana.
- **Campana.** Dado eventos pendientes, cuando miro la barra superior, entonces la campana muestra el conteo y la lista.

**Evidencia / Definición de Terminado:**
- Endpoints de recuperación y preferencias; servicio de notificaciones en el core; tests.

**Riesgos/Notas:**
- El servicio de notificaciones lo reutilizan comercio (alertas de pedido) y suscripciones.

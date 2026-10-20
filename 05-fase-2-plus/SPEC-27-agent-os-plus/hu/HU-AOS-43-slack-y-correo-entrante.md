---
id: HU-AOS-43
titulo: "Slack y correo entrante como conexiones"
spec: SPEC-27
fase: 2
hito: "2"
workstream: Agent OS
prioridad: P2
critico: false
estimacion: L
impacto: [diferenciacion]
req: [REQ-AOS-01]
dependencias: [HU-AOS-42]
skills: ["cloudflare-email-service", "backend-design:think-before-coding"]
estado: borrador
---

# HU-AOS-43 · Slack y correo entrante como conexiones

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-27](../spec.md).

**ID:** HU-AOS-43

**Título:** Slack y correo entrante como conexiones

**Workstream:** Agent OS

**Historia:** Como negocio quiero atender por Slack y por correo con los mismos agentes y superpoderes, para estar donde están mis clientes.

**Por qué importa (valor empresarial):** Más canales sobre el mismo kernel, sin código por canal en los agentes.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-AOS-01

**Dependencias:** [HU-AOS-42](HU-AOS-42-canal-api-y-webhooks.md)

**Criterios de aceptación (Gherkin):**
- **Correo.** Dado una conexión de correo entrante, cuando llega un correo, entonces se abre la conversación de (conexión, cliente) y la atiende su Coordinador.
- **Slack.** Dado una conexión de Slack, cuando un usuario escribe en el canal configurado, entonces responde el agente que corresponde.
- **Mismos superpoderes.** Dado un procedimiento de Ventas, cuando se usa desde correo, entonces aplica las mismas etapas y comprobaciones.

**Evidencia / Definición de Terminado:**
- Adaptadores de canal; tipos de conexión; tests.

**Riesgos/Notas:**
- Formato de correo largo: normalización antes del kernel.

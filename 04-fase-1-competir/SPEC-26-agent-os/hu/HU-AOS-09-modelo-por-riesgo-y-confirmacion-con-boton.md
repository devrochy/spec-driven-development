---
id: HU-AOS-09
titulo: "Política de modelo por riesgo y confirmación con botón interactivo"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [calidad_ia, confianza]
req: [REQ-AOS-06, REQ-AOS-03]
dependencias: [HU-AOS-05]
skills: ["meta-whatsapp", "agentcore-conventions", "optimizer"]
estado: terminada
---

# HU-AOS-09 · Política de modelo por riesgo y confirmación con botón interactivo

> Estado SDD: Terminada (2026-10-11) — issue cerrado en agent-core; PRs abajo.

**ID:** HU-AOS-09

**Título:** Política de modelo por riesgo y confirmación con botón interactivo

**Workstream:** Agent OS

**Historia:** Como dueño quiero que los pasos de alto riesgo usen más deliberación y que lo irreversible se confirme con un botón, para reducir errores donde más cuestan sin encarecer los turnos normales.

**Por qué importa (valor empresarial):** Concentra costo y control donde importa. Confirmar con un botón elimina los malentendidos de interpretar un "sí" en texto libre.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-06, REQ-AOS-03

**Dependencias:** [HU-AOS-05](HU-AOS-05-motor-de-procedimientos.md)

**Criterios de aceptación (Gherkin):**
- **Etapa de riesgo alto.** Dado una etapa `risk: high`, cuando corre el turno, entonces se usa el modelo con *thinking* y queda registrado en `usage_ledger`.
- **Reintento con respaldo.** Dado un fallo del verificador, cuando se reintenta, entonces se usa el respaldo del agente (`model.fallback`; hoy `gpt-4o-mini`, D-22).
- **Botón.** Dado una confirmación de pago por WhatsApp, cuando el cliente toca "Confirmar", entonces el payload determinista registra `confirmed` sin interpretar texto.

**Evidencia / Definición de Terminado:**
- `modelPolicy` del KernelSpec aplicado; botones interactivos en el adaptador de WhatsApp; clasificador sí/no de alta precisión para canales sin botones; tests.

**Terminada (2026-10-11):** PRs agent-core [#445](https://github.com/devrochy/agent-core/pull/445).

**Riesgos/Notas:**
- Los botones interactivos solo van dentro de la ventana de 24 h; fuera de ella se usa una plantilla aprobada con botones.
- Es dueña del botón de punta a punta: salida (botón interactivo) y entrada (`interactive.button_reply.id` y el payload de los botones de plantilla, que hoy se descartan en `core/gateway/channels/whatsapp/inbound.py:76-81`). Listas, ubicación y varias imágenes son de [HU-INMO-02](../../SPEC-28-inmoagent/hu/HU-INMO-02-entrada-estructurada-whatsapp.md) y [HU-INMO-03](../../SPEC-28-inmoagent/hu/HU-INMO-03-salida-interactiva.md), con piloto (D-SPEC-28-9).

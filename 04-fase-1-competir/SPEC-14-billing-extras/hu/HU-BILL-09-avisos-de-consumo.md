---
id: HU-BILL-09
titulo: Avisos de consumo fuera del panel
spec: SPEC-14
fase: 1
hito: "1"
workstream: Billing
prioridad: P1
critico: false
estimacion: S
impacto: [ingreso]
req: [REQ-BILL-08]
dependencias: [HU-BILL-06, HU-ARCH-13]
skills: ["marketing:email-sequence", "backend-design:idempotency-and-side-effects"]
estado: parqueada
---

# HU-BILL-09 · Avisos de consumo fuera del panel

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-14](../spec.md).

**ID:** HU-BILL-09

**Título:** Avisos de consumo fuera del panel

**Workstream:** Billing

**Historia:** Como dueño de un negocio quiero recibir un WhatsApp o un correo cuando llego al 80 % o al 100 % de mis créditos para recargar antes de que mi asistente deje de atender clientes nuevos.

**Por qué importa (valor empresarial):** El dueño no vive en el panel. Un aviso a tiempo convierte un bloqueo (cliente frustrado) en una recarga (ingreso).

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-BILL-08

**Dependencias:** HU-BILL-06, [HU-ARCH-13](../../../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md)

**Criterios de aceptación (Gherkin):**
- **Umbrales.** Dado el 80 %, el 100 % y la entrada al colchón, cuando ocurren, entonces el owner recibe un aviso por cada umbral una sola vez por período.
- **Canal.** Dado las preferencias del owner, cuando se envía, entonces usa WhatsApp con plantilla o correo según lo elegido.
- **Enlace.** Dado el aviso, cuando lo abro, entonces lleva a recargar o cambiar de plan.

**Evidencia / Definición de Terminado:**
- Tests de umbrales sin duplicados; plantillas documentadas.

**Riesgos/Notas:**
- El aviso consume el fee de plantilla del negocio de plataforma, no del cliente.

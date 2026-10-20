---
id: HU-SH-07
titulo: Antiabuso y cumplimiento del alta automática
spec: SPEC-07
fase: 0
hito: 0A
workstream: Asistente SolversHub
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, legal]
req: [REQ-SH-06]
dependencias: [HU-SH-03, HU-GTM-02]
skills: ["backend-design:security-discipline", "turnstile-spin", "doc-coauthoring"]
ola: 4
estado: borrador
---

# HU-SH-07 · Antiabuso y cumplimiento del alta automática

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-07](../spec.md).

**ID:** HU-SH-07

**Título:** Antiabuso y cumplimiento del alta automática

**Workstream:** Asistente SolversHub

**Historia:** Como dueño de SolversHub quiero límites a las pruebas gratis, detección de duplicados, aceptación de términos registrada y un interruptor de emergencia para abrir el alta automática sin exponerme a abuso ni a riesgos legales.

**Por qué importa (valor empresarial):** Un alta automática sin controles invita a crear decenas de negocios Free para consumir créditos gratis, y sin aceptación de términos registrada el contrato no es exigible. Es la condición para abrir el canal al público.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-SH-06

**Dependencias:** [HU-SH-03](HU-SH-03-aprovisionamiento-automatico.md), HU-GTM-02

**Criterios de aceptación (Gherkin):**
- **Un Free por persona.** Dado un teléfono o documento que ya tuvo un Free en los últimos 12 meses, cuando pide otro, entonces el asistente ofrece un plan pago.
- **Términos aceptados.** Dado un alta, cuando el cliente confirma la compra, entonces acepta términos, privacidad y DPA con enlace a la versión vigente, y queda registrado quién, cuándo y qué versión.
- **Revisión humana.** Dado señales de riesgo (dominio desechable, muchos intentos, datos inconsistentes), cuando se dispara el alta, entonces queda en revisión y se avisa al equipo.
- **Interruptor.** Dado un ataque, cuando el master apaga el aprovisionamiento automático, entonces las nuevas altas quedan en cola para revisión.
- **Límites de tasa.** Dado más de N pedidos de alta por hora desde un mismo origen, cuando llegan, entonces se frenan.

**Evidencia / Definición de Terminado:**
- Tests de cada regla; registro de aceptación con versión; interruptor en Plataforma.

**Riesgos/Notas:**
- Desde [HU-SH-03](HU-SH-03-aprovisionamiento-automatico.md) (ADR-0121), un Free repetido del mismo cliente o correo ya va a revisión, y el enlace de acceso va solo por correo. Rotar teléfono y correo en cada alta sigue siendo posible: lo cierra «Un Free por persona».
- Los datos usados para antiabuso son personales: finalidad declarada en el aviso de privacidad (HU-GTM-02).

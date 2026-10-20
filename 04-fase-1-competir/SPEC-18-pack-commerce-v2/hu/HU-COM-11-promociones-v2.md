---
id: HU-COM-11
titulo: Promociones v2 con horarios, cupones y domicilio gratis
spec: SPEC-18
fase: 1
hito: "1"
workstream: Comercio y suscripciones
prioridad: P1
critico: false
estimacion: M
impacto: [ingreso, diferenciacion]
req: [REQ-COM-06]
dependencias: [HU-COM-04]
skills: ["backend-design:data-modeling-discipline", "db-migration"]
estado: parqueada
---

# HU-COM-11 · Promociones v2 con horarios, cupones y domicilio gratis

> Estado SDD: Parqueada (2026-10-17, D-35) — ver [SPEC-18](../spec.md).

**ID:** HU-COM-11

**Título:** Promociones v2 con horarios, cupones y domicilio gratis

**Workstream:** Comercio y suscripciones

**Historia:** Como dueño de un restaurante quiero crear un "happy hour", un 2x1, un cupón de bienvenida con límite o domicilio gratis sobre un monto para vender más en las horas flojas.

**Por qué importa (valor empresarial):** Las promociones son la herramienta comercial más usada por restaurantes y retail; ninguno de los dos códigos tiene horarios ni cupones reales.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-COM-06

**Dependencias:** [HU-COM-04](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md)

**Criterios de aceptación (Gherkin):**
- **Horario.** Dado una promoción de martes a jueves de 15 a 18 h, cuando un cliente cotiza en esa franja, entonces aplica; fuera, no.
- **Cupón.** Dado un cupón con límite de 1 uso por cliente y 100 en total, cuando se usa, entonces se respeta el límite.
- **Domicilio gratis.** Dado un subtotal mínimo, cuando se supera, entonces el domicilio queda en $0.
- **Sin acumulación.** Dado dos promociones elegibles, cuando aplica, entonces gana la mejor salvo que el negocio permita acumular.

**Evidencia / Definición de Terminado:**
- Modelo de promociones extendido; UI; tests.

**Riesgos/Notas:**
- El monto final lo calcula el servidor ([HU-COM-01](../../../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md)).

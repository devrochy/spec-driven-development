---
id: HU-CONN-09
titulo: Costos de Meta verificables y opcionales por conexión
spec: SPEC-08
fase: 0
hito: 0B
workstream: Canales y conexiones
prioridad: P0
critico: false
estimacion: M
impacto: [diferenciacion, confianza]
req: [REQ-CONN-05, REQ-PLUS-03]
dependencias: [HU-CONN-01, HU-CONN-08]
skills: ["data:sql-queries", "kpi-dashboard-design", "frontend-design", "meta-whatsapp", "panel-ui"]
estado: borrador
---

# HU-CONN-09 · Costos de Meta verificables y opcionales por conexión

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-08](../spec.md) (D-SPEC-08-2).

**ID:** HU-CONN-09

**Título:** Costos de Meta verificables y opcionales por conexión

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero activar el seguimiento de lo que Meta me cobra por cada conexión, verificar que funciona y verlo junto a mi consumo de IA para conocer el costo total de mi atención por WhatsApp.

**Por qué importa (valor empresarial):** Desde el 2026-10-01 Meta cobra los mensajes de servicio: el costo de Meta ya es comparable al de la IA. Mostrarlo de forma confiable es transparencia (PLUS-03) y responde la pregunta del cliente: hoy la sección no se habilita, siempre se ve y siempre está vacía.

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-CONN-05, REQ-PLUS-03

**Dependencias:** [HU-CONN-01](HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-08](HU-CONN-08-lista-y-hub-meta.md)

**Criterios de aceptación (Gherkin):**
- **Opcional.** Dado una conexión de producción, cuando se crea, entonces el seguimiento de costos viene encendido; en una de prueba viene apagado con la explicación "los números de prueba no generan cobros".
- **Verificar.** Dado la pestaña Costos del hub, cuando pulso "Verificar", entonces se consulta el día anterior y veo éxito o el error de Meta, y queda la fecha de la última sincronización.
- **Verdad al sincronizar.** Dado "Sincronizar", cuando falla para alguna conexión, entonces el panel lo dice (no "Costos sincronizados." cuando no se sincronizó nada).
- **Tarjeta agregada.** Dado la página de Consumo, cuando ninguna conexión tiene el seguimiento activo, entonces no aparece la tarjeta de WhatsApp; si alguna lo tiene, aparece con el total y el detalle por conexión.
- **Créditos de Meta.** Dado una conexión ES con línea de crédito, cuando consulto, entonces veo el saldo de Meta en modo lectura.

**Evidencia / Definición de Terminado:**
- Flag por conexión con migración; job de precios por conexión; tests; texto de ayuda revisado.

**Riesgos/Notas:**
- La página "Costos LLM" pasa a "Consumo de IA" con la pestaña de WhatsApp ([SPEC-12](../../../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md)).

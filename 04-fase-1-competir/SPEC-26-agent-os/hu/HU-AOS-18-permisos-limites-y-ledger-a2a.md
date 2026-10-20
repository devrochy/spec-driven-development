---
id: HU-AOS-18
titulo: "Permisos de colaboración, límites y ledger A2A"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: L
impacto: [confianza, diferenciacion]
req: [REQ-AOS-07, REQ-AOS-08, REQ-AOS-09]
dependencias: [HU-AOS-15]
skills: ["backend-design:security-discipline", "auditor-multitenant", "backend-design:think-before-coding"]
estado: borrador
---

# HU-AOS-18 · Permisos de colaboración, límites y ledger A2A

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-18

**Título:** Permisos de colaboración, límites y ledger A2A

**Workstream:** Agent OS

**Historia:** Como dueño quiero decidir qué agente puede pasar la conversación, encargar o consultar a cuál, con límites de tiempo, profundidad y presupuesto, para que la colaboración sea segura y trazable.

**Por qué importa (valor empresarial):** Cumple el grafo de permisos y la trazabilidad A2A que exige el Agent OS, y previene bucles y costos descontrolados.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-AOS-07, REQ-AOS-08, REQ-AOS-09

**Dependencias:** [HU-AOS-15](HU-AOS-15-migracion-sin-regresion.md)

**Criterios de aceptación (Gherkin):**
- **Permiso.** Dado que Ventas no tiene permiso de consultar a Cobranza, cuando lo intenta, entonces se deniega con `no_link` y queda en `a2a_events`.
- **Anti-bucle.** Dado una cadena que vuelve a un agente ya visitado, cuando se evalúa, entonces se deniega con `cycle` y se emite `a2a.loop.detected`.
- **Presupuesto.** Dado un enlace con 0,02 USD, cuando la operación lo superaría, entonces se deniega con `budget`.
- **Entre negocios.** Dado un permiso hacia un agente de otro negocio, cuando se guarda, entonces la FK compuesta lo rechaza; y lo mismo con cualquier referencia de `a2a_conversations` o `a2a_events` (conexión, conversación, turno, instancia, versión).
- **Modos.** Dado un enlace con `broadcast` o `collaborate` en `modes`, cuando se guarda, entonces se rechaza: son mecanismos internos del Coordinador y basta con que la instancia esté habilitada (ADR-0116 §1).
- **Profundidad.** Dado un enlace con `max_depth` mayor que el límite del KernelSpec, cuando se valida la release, entonces falla.

**Evidencia / Definición de Terminado:**
- Guarda A2A en el kernel; grafo versionado con scope de negocio y validación (límites por defecto en el KernelSpec: profundidad 3, 6 operaciones por turno, más de 2 cambios de dueño en 6 turnos congela al dueño); `a2a_events` conservado hasta `purge_tenant` y `a2a_conversations` como proyección en la misma transacción; gasto en `usage_ledger` con `a2a_call_id`; una consulta por llamada (sin vista con `tenant_id`); tests de caos (ciclos, autollamada, ping-pong).

**Riesgos/Notas:**
- Límites demasiado estrictos cortan casos válidos: los valores iniciales se calibran con el tablero ([HU-AOS-29](HU-AOS-29-tablero-de-fiabilidad.md)).
- Permisos solo con scope de negocio por ahora: el de conexión (con un `deny` de conexión que gana) se agrega cuando un negocio con dos conexiones pida permisos distintos (ADR-0116 §2).
- `a2a_events.payload_hash` es un HMAC con clave del servidor, no un sha256 plano (revisión de seguridad de [HU-AOS-02](HU-AOS-02-esquema-aditivo.md)): con un hash sin clave, un payload corto o predecible (un número de documento, un monto) se recupera por fuerza bruta aunque el payload esté redactado. El CHECK de formato (`^[0-9a-f]{64}$`) vale para HMAC-SHA256.

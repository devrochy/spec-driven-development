# 02 · Visión y decisiones

## Resumen ejecutivo

SolversHub tiene un motor sólido (multi-tenant con RLS real, habilidades activables, AgentSpec, API
`/api/v1`), un panel amplio y una app móvil. La re-validación del 2026-10-01 encontró que **todavía no
podía vender, cobrar y dar de alta clientes sin intervención humana** y que su producción corría en la
máquina de desarrollo; de sus 38 hallazgos, los más urgentes (el modelo de lenguaje por defecto
discontinuado, los mensajes de servicio de Meta cobrados mientras el motor enviaba hasta 3 por turno,
el LLM decidiendo el monto de los links de pago) se atienden en el Hito 0A. El estado real de cada HU
vive en la [bitácora](../08-bitacora-de-ejecucion.md).

**Lo que se vende es el agente** ([D-35](decisiones.md#d-35--solvershub-vende-agentes), 2026-10-17).
Cada negocio tiene sus agentes (Ventas, Cobranza, Agenda, Suscripciones o personalizados), cada uno
con su configuración (identidad, proveedor y modelo, superpoderes, memoria, reglas), y un
**Coordinador** —el agente core del negocio instanciado en cada conexión— que los orquesta en el mismo
hilo. Las habilidades (packs) son capacidades que se le dan a un agente y los presets solo instalan
agentes «para un fin». El cliente entra a SolversHub a ver cada agente y la data que construyó, y los
planes cobran por agentes publicados, crédito mensual de uso y colaboradores
(documento de precios (privado) §5). Esa visión la construye
[SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) (Agent OS de procedimientos, D-27); las specs que no la sirven quedan **parqueadas**, fuera del
calendario y de los totales de pendientes.

La propuesta organiza el trabajo en **3 fases, 31 specs y 295 HU** (30 de ellas parqueadas), con un
primer hito muy concreto:

> **Hito 0A · "SolversHub vende y cobra solo".** Un prospecto real agenda una demo con el asistente
> de SolversHub, compra un plan, paga (Free sin cobro), su negocio se crea solo con una invitación,
> conecta su WhatsApp por Embedded Signup y su suscripción genera el cobro del período siguiente con
> aviso por plantilla. Todo sin intervención humana y con evidencia auditada.

Todo lo que se construye para ese hito es **parametrizable**: los mismos agentes de Ventas, Agenda y
Suscripciones sirven a un gimnasio, un colegio o un software con mensualidad. Solo SolversHub agrega
la acción de crear un negocio al venderse un plan. El agente es lo que se vende; el preset solo lo
instala.

| Fase | Para qué | Specs | HU | Hito |
|---|---|---|---|---|
| **0 · Go-live** | Vender, cobrar y operar en producción con confianza | [SPEC-00](../03-fase-0-go-live/SPEC-00-reestructuracion/spec.md) a SPEC-11 | 97 | 0A (48 HU) y 0B (49 HU) |
| **1 · Competir** | Agent OS (SolversHub vende agentes), app móvil oficial, sistema de diseño, agenda, canales y centro de pruebas | [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md) a [SPEC-20](../04-fase-1-competir/SPEC-20-crecimiento/spec.md), [SPEC-24](../04-fase-1-competir/SPEC-24-agenda-y-citas/spec.md), [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md), [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md), [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md), [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md) y [SPEC-30](../04-fase-1-competir/SPEC-30-centro-de-pruebas/spec.md) | 176 (25 parqueadas) | 1 |
| **2 · Plus** | Agent OS plus, extensibilidad avanzada, voz e ISO 27001 | [SPEC-21](../05-fase-2-plus/SPEC-21-agencia-e-internacional/spec.md) a [SPEC-23](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/spec.md) y [SPEC-27](../05-fase-2-plus/SPEC-27-agent-os-plus/spec.md) | 22 (5 parqueadas) | 2 |

## Diff conceptual frente al plan vigente

**Se mantiene**

- Los requerimientos `REQ-ARCH/FIX/COMP/PLUS/MEDIA/GTM` como base (ver [requerimientos.md](requerimientos.md)).
- Las decisiones del cliente: plataforma directa ahora y agencia después, dos verticales en
  paralelo, voz en llamadas fuera de v1, STT y OCR dentro.
- El port de multimodalidad desde `agent-sale` (STT, visión, OCR de comprobantes).
- Los bloqueantes del go-live (dominio con TLS, producción separada, backups, calidad ≥95 %).

**Se corrige**

- La matriz tiene 13 competidores reales, no 14: ChatBotCorp es la columna de ejemplo y Wolkvox no
  tiene columna.
- El estado real de cada brecha: la DLQ está peor de lo dicho, la caché de Anthropic también,
  `FIX-07` está cerrado y la cobranza ya vive en el backend (no en NestJS).
- "Oleadas 0/1/2" pasan a **Fases** con specs SDD; la Fase 0 se parte en los hitos 0A y 0B.
- Los claims falsos: la prueba de 30 días es solo de Free, no hay integraciones con HubSpot y
  compañía, el alta no es de "2–4 semanas".
- La columna SolversHub de la matriz deja de prometer Instagram y web.
- El lenguaje de la oferta: no se venden packs ni presets, se venden agentes (D-35).

**Se añade**

| Línea nueva | Requerimientos | Specs |
|---|---|---|
| Agent OS: SolversHub vende agentes (agentes por negocio, Coordinador por conexión, procedimientos tipados, releases con rollback, consola por agente) | REQ-AOS-01..17 | [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md), [SPEC-27](../05-fase-2-plus/SPEC-27-agent-os-plus/spec.md) |
| Billing v2 por créditos (llave híbrida, Meta aparte, precios re-derivados) con planes por agentes, crédito y colaboradores (D-35) | REQ-BILL-01..12 | SPEC-03, [SPEC-14](../04-fase-1-competir/SPEC-14-billing-extras/spec.md) (parqueada salvo [HU-BILL-12](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md)), [SPEC-21](../05-fase-2-plus/SPEC-21-agencia-e-internacional/spec.md) (parqueada) |
| Framework de presets y habilidades como capacidades que se le dan a un agente | REQ-FWK-01..08 | [SPEC-05](../03-fase-0-go-live/SPEC-05-presets-y-flujos/spec.md), [SPEC-16](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/spec.md), [SPEC-22](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md) |
| UX guiada, arquitectura de información y sistema de diseño unificado | REQ-UX-01..11 | [SPEC-10](../03-fase-0-go-live/SPEC-10-panel-confiable/spec.md), [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md), [SPEC-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/spec.md) (parqueada), [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md) |
| Editor visual del flujo por pack | REQ-FLOW-01..05 | [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) (parqueada: lo útil vive en [HU-AOS-05](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md), [HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md) y [HU-AOS-45](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md)), [SPEC-22](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/spec.md) |
| Planes y suscripciones como habilidad replicable | REQ-SUB-01..07 | SPEC-06 |
| Asistente SolversHub que vende, cobra y da de alta solo | REQ-SH-01..07 | [SPEC-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/spec.md) |
| Conexión WhatsApp-Meta efectiva en prueba y producción | REQ-CONN-01..05 | [SPEC-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/spec.md) |
| Comercio confiable (barrido de `agent-sale`) | REQ-COM-01..08 | [SPEC-09](../03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md), [SPEC-18](../04-fase-1-competir/SPEC-18-pack-commerce-v2/spec.md) (parqueada) |
| Agenda y citas | REQ-CAL-01..03 | [SPEC-24](../04-fase-1-competir/SPEC-24-agenda-y-citas/spec.md) |
| App móvil oficial | REQ-APP-01..11 | [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md), [SPEC-29](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/spec.md) |
| Vertical inmobiliaria (InmoAgent), con piloto como condición del código | REQ-INMO-01..12 | [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md) |
| Centro de pruebas con rol tester solo en test | REQ-ARCH-22 | [SPEC-30](../04-fase-1-competir/SPEC-30-centro-de-pruebas/spec.md) |
| Reestructura `solvershub-<section>` | REQ-REP-01..03 | [SPEC-00](../03-fase-0-go-live/SPEC-00-reestructuracion/spec.md) |
| Metodología SDD con opciones, pros y contras | — | [Constitución](../00-constitucion.md) |

## Documentos de esta carpeta

| Documento | Contenido |
|---|---|
| [requerimientos.md](requerimientos.md) | Catálogo único de REQ, existentes y nuevos, con estado y HU que los cubren |
| [decisiones.md](decisiones.md) | Registro D-01 a D-35 con opciones, pros y contras |
| [preguntas-abiertas.md](preguntas-abiertas.md) | P-01 a P-31, con recomendación y las ya decididas marcadas ✅ |
| [arquitectura-objetivo.md](arquitectura-objetivo.md) | "Planes y suscripciones" como habilidades de los agentes y el recorrido de SolversHub |
| documento de precios (privado) | Créditos, costos por proveedor, márgenes y planes v2 por agentes (D-35) |
| [arquitectura-informacion-panel.md](arquitectura-informacion-panel.md) | Menú, glosario y onboarding propuestos |
| [riesgos-supuestos.md](riesgos-supuestos.md) | Riesgos con mitigación y supuestos explícitos |
| [calendario-estimado.md](calendario-estimado.md) | Esfuerzo por hito y fechas en rango (D-17) |

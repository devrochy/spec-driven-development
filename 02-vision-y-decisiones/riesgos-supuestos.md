# Riesgos y supuestos

## Riesgos

Probabilidad e impacto: A alto · M medio · B bajo.

| ID | Riesgo | Prob. | Impacto | Mitigación | Dónde |
|---|---|---|---|---|---|
| R-01 | Meta tarda en aprobar a SolversHub como Tech Provider (verificación del negocio, App Review, `config_id`) y Embedded Signup no se puede usar | A | A | Empezar los trámites en la primera semana; BYOK de producción como respaldo ([HU-CONN-06](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md)) | [HU-SH-05](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md), HU-GTM-03 |
| R-02 | `deepseek-flash` falla con tools o cambia de comportamiento | M | A | Gate de evals en CI; respaldo automático a otro modelo | [HU-ARCH-10](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md) |
| R-03 | El costo de Meta por mensaje (desde 2026-10-01) sorprende a los clientes | A | M | `un_mensaje` por defecto; costos de Meta visibles por conexión | [HU-ARCH-11](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-11-un-mensaje-por-defecto.md), [HU-CONN-09](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-09-costos-meta-verificables.md) |
| R-04 | Una sola persona no alcanza para el Hito 0A en el plazo esperado | A | A | Corte 0A/0B (D-18); agentes de IA; recalibrar al cerrar cada spec | [calendario-estimado.md](calendario-estimado.md) |
| R-05 | Wompi admite una sola URL de eventos por entorno y el billing de plataforma y los pagos del tenant `solvershub` se pisan | M | A | Verificar; si se confirma, cuentas de Wompi separadas o un enrutador de eventos | [HU-SH-04](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md) |
| R-06 | Pérdida de datos antes de tener backups probados | M | A | Backups en el Hito 0A, antes del primer cliente | [HU-ARCH-03](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md) |
| R-07 | Exposición legal por alta automática y subprocesadores no declarados | M | A | Legal v2 revisado por abogado antes de cerrar el 0A | HU-GTM-02, [HU-SH-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md) |
| R-08 | Abuso de pruebas gratis (Free a repetición) | M | M | Límites por teléfono y documento, verificación, kill-switch | [HU-SH-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md) |
| R-09 | Gasto de LLM sin techo con la llave de plataforma antes de tener créditos (llegan en el 0B) | M | M | Mantener el tope `costo_llm_usd` actual hasta HU-BILL-06; alertas de costo | [HU-ARCH-07](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md) |
| R-10 | Dos proveedores de suscripción divergen con el tiempo | M | M | Contrato único con tests compartidos | HU-SUB-01, HU-SUB-15 |
| R-11 | Renombres rompen despliegues (CLI, variables, entry points) | M | M | Alias durante la transición y ADR | [HU-REP-03](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-03-transicion-de-identificadores.md) |
| R-12 | El proveedor de visión elegido se retira (Gemini 2.5 Flash-Lite el 2026-10-20) | A | B | Elegir por benchmark entre proveedores vigentes; tarifario con ciclo de vida de modelos | [HU-MEDIA-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md), HU-BILL-03 |
| R-13 | Credencial del master en el historial de git | B | A | Rotar ya; limpiar el historial si se confirma | [HU-ARCH-04](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md) |
| R-14 | Evals de un solo turno dan falsa confianza | A | M | Journeys multi-turno con eventos simulados | HU-SUB-12, [HU-SH-08](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) |

## Supuestos

Cada supuesto tiene la HU que lo convierte en dato.

| ID | Supuesto | Valor | Se valida en |
|---|---|---|---|
| S-01 | TRM | (cifra interna) | HU-BILL-01 |
| S-02 | Perfil de conversación | 8 turnos, 1,6 llamadas por turno, 9.500 tokens de entrada y 150 de salida por llamada, 75 % de caché | HU-BILL-01 (SQL sobre `usage_ledger`) |
| S-03 | Costo fijo mensual | (cifra interna) | P-01 |
| S-04 | Tarifa de Meta en Colombia | (tarifa de Meta) | [HU-CONN-09](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-09-costos-meta-verificables.md) |
| S-05 | Mínimo de Wompi | (mínimo de Wompi) | HU-SUB-13 |
| S-06 | Factor de aceleración con agentes de IA | 2,5× a 4× | Al cerrar cada spec |
| S-07 | `deepseek-flash` soporta tools en modo sin razonamiento | Sí | [HU-ARCH-10](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md) |
| S-08 | Tráfico en horario pico de DeepSeek | 15 % | HU-BILL-01 |
| S-09 | Nota de voz promedio | 30 s | [HU-MEDIA-03](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md) |
| S-10 | Imagen tras redimensionar | ~1.600 tokens | [HU-MEDIA-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md) |

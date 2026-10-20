# Plan vigente contra el código

Cada requerimiento de `solvershub-comercial/PLAN-COMPETENCIA-Y-PRODUCCION.md` con su estado real.
Estados: **vigente** (sigue abierto), **parcial**, **cerrado**, **peor** (más grave de lo que el plan
decía). La última columna dice qué HU lo resuelve ahora.

## REQ-ARCH

| REQ | Qué pedía | Estado | Evidencia | Cubierto por |
|---|---|---|---|---|
| ARCH-01 | Dominio con TLS para el webhook de Meta | **parcial** | `app.solvershub.site` pasa por Cloudflare Tunnel, pero es el entorno de **test**; no hay dominio de producción (`docs/despliegue-coolify.md`) | [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md), [HU-ARCH-02](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-02-borde-tls-y-webhook-prod.md) |
| ARCH-02 | Producción separada | **parcial** | Hay prod (`main`) y test (`develop`), cada uno con su Postgres y Redis, **pero los dos en la máquina de desarrollo** (invariante 9) | [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) |
| ARCH-03 | Backup con restauración probada | **vigente** | Sin WAL, PITR ni dumps versionados; `pack_cobranza/evidencias.py:5` cita "el backup del runbook", que no cubre los archivos | [HU-ARCH-03](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md) |
| ARCH-04 | CSRF, rate limit de login, webhook fail-closed | **vigente** | Sin contador ni bloqueo de intentos en la API ni en la API de campo (`pack_cobranza/api_gestor.py:144-155`). El panel nuevo mitiga CSRF con cookie `SameSite=Lax` en el BFF | [HU-ARCH-04](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md) |
| ARCH-05 | Procesamiento de media | **vigente** | No existe `mod_media_processor`; la media entra como texto de reemplazo y la URL se guarda vacía (`core/gateway/webhooks.py`, `channels/whatsapp/inbound.py:67-73`) | [SPEC-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/spec.md) |
| ARCH-06 | MCP por tenant | **vigente** | No hay cliente MCP; solo tools HTTP declarativas con allowlist (`core/mcp/declarative.py:1-21`) | [HU-ARCH-19](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md) |
| ARCH-07 | Guardrails de runtime | **parcial** | Hay chequeo previo a la tool y confirmación humana, pero las tools sin binding corren igual ("fail-open transitorio", `core/orchestrator/loop.py`), ninguna tool declara `scopes` y la señal `escalate` no se lee | [HU-ARCH-12](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md), [HU-ARCH-20](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-20-guardrails-runtime.md) |
| ARCH-08 | Cola confiable | **peor** | (re-verificado 2026-10-01) `CONSUMER = "orchestrator-1"` fijo (`core/orchestrator/consumer.py:59`) y solo lee entradas nuevas `">"` (`:88`): una entrada fallida nunca se re-lee, **la DLQ es inalcanzable** y hay mensajes perdidos | [HU-ARCH-06](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md) |
| ARCH-09 | Observabilidad | **vigente** | Sin `/metrics`, sin p99 del webhook, `/healthz` estático; OTel apagado por defecto | [HU-ARCH-07](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md), [HU-ARCH-21](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-21-status-page-y-slos.md) |
| ARCH-10 | Calidad ≥95 % | **parcial** | Framework: 34–35/35 tras los ajustes de flujo. `solvershub`: 7/7 pero de un solo turno. Sin golden de cobranza ni de agenda | [HU-ARCH-16](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-16-golden-set-comercio.md), [HU-ARCH-17](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-17-golden-set-cobranza.md), HU-SUB-12, [HU-SH-08](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) |
| ARCH-11 | `ToolContext` completo y pricing editable | **vigente** | (re-verificado) Precios fijos en `core/llm/openai_compatible.py:41-45` y `anthropic_provider.py:40-42`; un modelo desconocido cuesta 0 (`openai_compatible.py:55`) | HU-BILL-03 (precios), [HU-ARCH-25](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-25-toolcontext-y-embeddings.md) (contrato) |
| ARCH-12 | No-root, mypy, vector configurable | **vigente** | Dockerfile sin `USER`; `make lint` corre `mypy … \|\| true`; `Vector(384)` fijo | [HU-ARCH-24](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-24-contenedor-y-tipos.md) |
| ARCH-13 | Billing recurrente | **vigente** | `billing_lifecycle` solo pasa a `past_due`/`expired`; no genera links de renovación | [HU-SH-04](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md), [HU-BILL-12](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md) |

## REQ-FIX

| REQ | Estado | Evidencia | Cubierto por |
|---|---|---|---|
| FIX-01 Salida IG/Messenger | **vigente** | `connection_types.py` los marca `available=False`; el código vive en ramas sin mergear | [HU-CHAN-01](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-01-instagram-y-messenger.md) |
| FIX-02 Widget web | **vigente** | `"web"` existe en `ChannelKind` pero no hay ruta ni widget | [HU-CHAN-02](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-02-chat-web.md) |
| FIX-03 Editor de flujo | **vigente** | El flujo se edita solo por archivo (ADR-0054 §5) | [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) |
| FIX-04 Bandeja con asignación | **parcial** | El modelo tiene `assigned_admin_id` (`core/db/models.py:504-521`) pero la API solo lista escalaciones (`api/routers/escalations.py:31`) | [HU-UI-05](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-05-tickets-reales.md), [HU-UI-06](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-06-bandeja-dos-paneles.md) |
| FIX-05 Catálogo de integraciones honesto | **vigente** | El FAQ promete HubSpot, Salesforce, Pipedrive y Zoho | HU-GTM-05, [HU-GTM-10](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-10-paginas-de-integraciones-y-seo.md) |
| FIX-06 Add-ons de plan | **vigente** | Sin recargas ni add-ons | SPEC-03, [HU-BILL-10](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md) |
| FIX-07 `BASE_RULES` y tool de escalamiento | **cerrado** | `escalate_to_human` existe (`core/tools/core_skill.py`) y `BASE_RULES` ya no está | — |
| FIX-08 Caché de Anthropic | **peor** | `cache_control` en cada bloque: con el spec por defecto hay 5 o más y el límite es 4 (`core/llm/anthropic_provider.py:55-62`) | [HU-ARCH-15](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-15-cache-anthropic.md) |
| FIX-09 Dashboard de calidad | **vigente** | Sin tasa de "resuelto sin humano" ni CSAT | [HU-UI-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) |

## REQ-COMP, REQ-PLUS, REQ-MEDIA y REQ-GTM

| REQ | Estado | Cubierto por |
|---|---|---|
| COMP-01 Multicanal | vigente | [SPEC-17](../04-fase-1-competir/SPEC-17-canales-y-campanas/spec.md) |
| COMP-02 MCP y marketplace | vigente | [HU-ARCH-19](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md), [HU-FWK-14](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FWK-14-integraciones-mcp.md) |
| COMP-03 Campañas | parcial: las plantillas se gestionan pero **no se pueden enviar** (`gateway/channels/whatsapp/outbound.py` solo tiene texto e imagen) | [HU-ARCH-13](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), [HU-CHAN-03](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md) |
| COMP-04 Páginas de integraciones y casos de uso | vigente: el sitemap tiene 6 URL | [HU-GTM-10](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-10-paginas-de-integraciones-y-seo.md) |
| COMP-05 Prueba social | vigente: `SHOW_SOCIAL_PROOF = false` | [HU-GTM-13](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-13-prueba-social.md) |
| COMP-06 Reporte mensual | vigente | [HU-UX-07](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-UX-07-reporte-mensual.md) |
| COMP-07 Demo pública | parcial: hay demo en la landing y agente de WhatsApp de prueba | [HU-SH-09](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md) |
| COMP-08 Onboarding autoservicio | parcial: solo wizard del master | [HU-SH-03](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md), [HU-SH-06](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md), [HU-UX-06](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-06-registro-desde-landing.md) |
| PLUS-01 IA confiable | parcial | [SPEC-02](../03-fase-0-go-live/SPEC-02-agente-confiable/spec.md), [SPEC-09](../03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md) |
| PLUS-02 BYOK total | parcial: BYOK de WhatsApp roto para casi todas las tools de Meta | SPEC-03, [HU-CONN-01](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md) |
| PLUS-03 Costo por conversación visible | parcial | HU-BILL-07 |
| PLUS-04 Cobranza con APK | hecho en código; falta producción | [HU-ARCH-08](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-08-apk-a-produccion.md), HU-SUB-15 |
| PLUS-05 Motor + habilidades | hecho; falta UI por descriptores | [SPEC-16](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/spec.md) |
| PLUS-05b Modelo listo para sub-cuentas | vigente | [HU-FWK-12](../05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-FWK-12-organizaciones-y-subcuentas.md) |
| PLUS-06 Dogfooding | parcial: el tenant `solvershub` existe | [SPEC-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/spec.md) |
| PLUS-07 Paquete de confianza | parcial | HU-GTM-02, [HU-ARCH-22](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-22-pentest.md) |
| PLUS-08 ISO 27001 | vigente | [HU-GTM-14](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-14-camino-iso-27001.md) |
| MEDIA-01..07 | vigentes | [SPEC-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/spec.md), [HU-MEDIA-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-MEDIA-07-visor-de-media.md) |
| MEDIA-08 Voz en llamadas | diferido por decisión | [HU-MEDIA-08](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-MEDIA-08-voz-en-llamadas.md) |
| GTM-01 Legal publicado | vigente: borradores con `⟨PENDIENTE⟩` | HU-GTM-02 |
| GTM-02 WhatsApp de Roshi verificado | vigente | HU-GTM-03 |
| GTM-03 Redes activas | vigente (0 %) | [HU-GTM-07](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-07-redes-activas.md) |
| GTM-04 Activos de venta | vigente | [HU-GTM-08](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-08-activos-de-venta.md) |
| GTM-05 Leads con SLA <5 min | vigente | [HU-GTM-09](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-09-leads-con-sla.md) |
| GTM-06 Dominio final | vigente | HU-GTM-01 |
| GTM-07 Fee de implementación | vigente | HU-GTM-01 |
| GTM-08 SLOs y status page | vigente | [HU-ARCH-21](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-21-status-page-y-slos.md) |

## Bloqueantes que el plan identificó, hoy

| Bloqueante | Estado al 2026-10-01 |
|---|---|
| Dominio con TLS para el webhook | Test sí; producción no |
| Entorno de producción separado | Existe pero en la máquina de desarrollo |
| Backup con restauración probada | No |
| Calidad ≥95 % | Framework sí; asistente `solvershub` y verticales no medidos en multi-turno |
| Panel sin CSRF ni rate limit | Panel nuevo mitiga CSRF; falta lockout |
| Procesador de media | No existe |

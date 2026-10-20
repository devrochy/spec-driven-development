# Catálogo de requerimientos

Un solo catálogo. Los requerimientos existentes vienen de
`solvershub-comercial/PLAN-COMPETENCIA-Y-PRODUCCION.md`; los nuevos nacen de las directrices del
cliente (2026-09-28 a 2026-10-01). Estado: ⏳ abierto · 🟡 parcial · ✅ cerrado · ⤵ absorbido por otro
REQ. El detalle de evidencia está en
[`01-revalidacion/plan-previo-vs-codigo.md`](../01-revalidacion/plan-previo-vs-codigo.md).

## Existentes

| REQ | Requerimiento | Estado | Fase | HU |
|---|---|---|---|---|
| REQ-ARCH-01 | Dominio con TLS para el webhook de Meta | 🟡 | 0 | [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md), [HU-ARCH-02](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-02-borde-tls-y-webhook-prod.md) |
| REQ-ARCH-02 | Producción separada | 🟡 | 0 | [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) |
| REQ-ARCH-03 | Backup con restauración probada | ⏳ | 0 | [HU-ARCH-03](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md) |
| REQ-ARCH-04 | Endurecer el acceso y el webhook | ⏳ | 0 | [HU-ARCH-04](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md), [HU-ARCH-05](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-05-webhook-fail-closed.md) |
| REQ-ARCH-05 | Procesamiento de media | ⏳ | 0 | [HU-MEDIA-01](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-01-adr-media.md), [HU-MEDIA-02](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md) |
| REQ-ARCH-06 | MCP por tenant | ⏳ | 1 | [HU-ARCH-19](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md) |
| REQ-ARCH-07 | Guardrails de runtime | 🟡 | 0–2 | [HU-ARCH-12](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md), [HU-ARCH-20](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-20-guardrails-runtime.md), [HU-ARCH-26](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-26-tool-siguiente-forzada.md) |
| REQ-ARCH-08 | Cola confiable (DLQ) | ⏳ | 0–1 | [HU-ARCH-06](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-06-consumer-y-dlq.md), [HU-ARCH-27](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-27-turnos-timeout-y-observabilidad.md) |
| REQ-ARCH-09 | Observabilidad | ⏳ | 0–1 | [HU-ARCH-07](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-07-observabilidad-prod.md), [HU-ARCH-21](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-21-status-page-y-slos.md), [HU-ARCH-27](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-27-turnos-timeout-y-observabilidad.md) |
| REQ-ARCH-10 | Calidad ≥95 % | 🟡 | 0 | [HU-ARCH-16](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-16-golden-set-comercio.md), [HU-ARCH-17](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-17-golden-set-cobranza.md), HU-SUB-12, [HU-SH-08](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) |
| REQ-ARCH-11 | `ToolContext` y pricing configurable | ⏳ | 0–2 | HU-BILL-03, [HU-ARCH-25](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-ARCH-25-toolcontext-y-embeddings.md) |
| REQ-ARCH-12 | Contenedor no-root, mypy, vector configurable | ⏳ | 1 | [HU-ARCH-24](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-24-contenedor-y-tipos.md) |
| REQ-ARCH-13 | Billing recurrente | ⤵ REQ-BILL-11 | 0–1 | [HU-SH-04](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md), [HU-BILL-12](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md) |
| REQ-FIX-01 | Salida por Instagram y Messenger | ⏳ | 1 | [HU-CHAN-01](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-01-instagram-y-messenger.md) |
| REQ-FIX-02 | Widget de chat web | ⏳ | 1 | [HU-CHAN-02](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-02-chat-web.md) |
| REQ-FIX-03 | Editor de flujo | ⤵ REQ-FLOW | 1 | [SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md) |
| REQ-FIX-04 | Bandeja con asignación | 🟡 | 1 | [HU-UI-05](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-05-tickets-reales.md), [HU-UI-06](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-06-bandeja-dos-paneles.md) |
| REQ-FIX-05 | Catálogo de integraciones honesto | ⏳ | 0–1 | HU-GTM-05, [HU-GTM-10](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-10-paginas-de-integraciones-y-seo.md) |
| REQ-FIX-06 | Add-ons de plan | ⤵ REQ-BILL | 0–1 | HU-BILL-05, [HU-BILL-10](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md) |
| REQ-FIX-07 | Limpiar `BASE_RULES` y tool de escalamiento | ✅ | — | — |
| REQ-FIX-08 | Caché de Anthropic | ⏳ | 0 | [HU-ARCH-15](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-15-cache-anthropic.md) |
| REQ-FIX-09 | Dashboard de calidad | ⏳ | 1 | [HU-UI-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-07-dashboard-con-tendencias.md) |
| REQ-COMP-01 | Multicanal | ⏳ | 1 | [HU-CHAN-01](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-01-instagram-y-messenger.md), [HU-CHAN-02](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-02-chat-web.md) |
| REQ-COMP-02 | MCP y marketplace | ⏳ | 1–2 | [HU-ARCH-19](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md), [HU-FWK-14](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FWK-14-integraciones-mcp.md) |
| REQ-COMP-03 | Campañas salientes | 🟡 | 0–1 | [HU-ARCH-13](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), [HU-CHAN-03](../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md) |
| REQ-COMP-04 | Páginas de integraciones, casos y SEO | ⏳ | 1 | [HU-GTM-10](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-10-paginas-de-integraciones-y-seo.md) |
| REQ-COMP-05 | Prueba social real | ⏳ | 2 | [HU-GTM-13](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-13-prueba-social.md) |
| REQ-COMP-06 | Reporte mensual | ⤵ REQ-UX-08 | 2 | [HU-UX-07](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-UX-07-reporte-mensual.md) |
| REQ-COMP-07 | Demo pública | 🟡 | 0 | [HU-SH-09](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md) |
| REQ-COMP-08 | Onboarding autoservicio | 🟡 | 0–1 | [HU-SH-03](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md), [HU-SH-06](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md), [HU-UX-06](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-06-registro-desde-landing.md) |
| REQ-PLUS-01 | IA confiable | 🟡 | 0 | [HU-ARCH-12](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-12-precondiciones-y-escalate.md), [HU-ARCH-18](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md), [HU-COM-01](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md), [HU-COM-02](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md) |
| REQ-PLUS-02 | BYOK total | 🟡 | 0 | HU-BILL-03, [HU-CONN-01](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md) |
| REQ-PLUS-03 | Costo por conversación visible | 🟡 | 0 | HU-BILL-07, [HU-CONN-09](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-09-costos-meta-verificables.md) |
| REQ-PLUS-04 | Cobranza con APK | 🟡 | 0 | [HU-ARCH-08](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-08-apk-a-produccion.md), HU-SUB-15 |
| REQ-PLUS-05 | Motor + habilidades activables | 🟡 | 1 | [HU-FWK-04](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md), [HU-FWK-07](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md) |
| REQ-PLUS-05b | Modelo listo para sub-cuentas | ⤵ REQ-FWK-08 | 2 | [HU-FWK-12](../05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-FWK-12-organizaciones-y-subcuentas.md) |
| REQ-PLUS-06 | Dogfooding | 🟡 | 0 | [SPEC-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/spec.md) |
| REQ-PLUS-07 | Paquete de confianza | 🟡 | 0–1 | HU-GTM-02, [HU-ARCH-22](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-22-pentest.md) |
| REQ-PLUS-08 | Camino a ISO 27001 | ⏳ | 2 | [HU-GTM-14](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-GTM-14-camino-iso-27001.md) |
| REQ-MEDIA-01 | Descarga y almacenamiento de media | ⏳ | 0 | [HU-MEDIA-02](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md) |
| REQ-MEDIA-02 | Notas de voz a texto | ⏳ | 0 | [HU-MEDIA-03](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md) |
| REQ-MEDIA-03 | Dispatcher de visión | ⏳ | 0 | [HU-MEDIA-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md) |
| REQ-MEDIA-04 | OCR de comprobantes | ⏳ | 0 | [HU-MEDIA-05](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-05-ocr-comprobantes.md) |
| REQ-MEDIA-05 | Clasificación comprobante/producto | ⏳ | 0 | [HU-MEDIA-06](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-06-clasificacion-de-imagenes.md) |
| REQ-MEDIA-06 | Ruteo de ingesta e idempotencia | ⏳ | 0 | [HU-MEDIA-01](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-01-adr-media.md), [HU-MEDIA-02](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-02-almacenamiento-media.md) |
| REQ-MEDIA-07 | Costo de media en el ledger | ⏳ | 0–1 | [HU-MEDIA-03](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md), [HU-MEDIA-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md), [HU-MEDIA-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-MEDIA-07-visor-de-media.md) |
| REQ-MEDIA-08 | Voz en llamadas | ⏳ (diferido por D-03) | 2 | [HU-MEDIA-08](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-MEDIA-08-voz-en-llamadas.md) |
| REQ-GTM-01 | Legal revisado y publicado | ⏳ | 0 | HU-GTM-02 |
| REQ-GTM-02 | WhatsApp de Roshi verificado | ⏳ | 0 | HU-GTM-03 |
| REQ-GTM-03 | Redes activas | ⏳ | 1 | [HU-GTM-07](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-07-redes-activas.md) |
| REQ-GTM-04 | Activos de venta | ⏳ | 1 | [HU-GTM-08](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-08-activos-de-venta.md) |
| REQ-GTM-05 | Leads con SLA <5 min | ⏳ | 1 | [HU-GTM-09](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-09-leads-con-sla.md) |
| REQ-GTM-06 | Dominio final | ⏳ | 0 | HU-GTM-01 |
| REQ-GTM-07 | Fee de implementación | ⏳ | 0 | HU-GTM-01 |
| REQ-GTM-08 | SLOs publicados y status page | ⏳ | 1 | [HU-ARCH-21](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-21-status-page-y-slos.md) |

## Nuevos

### Arquitectura y GTM (complementos)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-ARCH-14 | Playground sin efectos reales | 0 | [HU-ARCH-14](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-14-playground-sandbox.md) |
| REQ-ARCH-15 | Envío de plantillas fuera de 24 h | 0 | [HU-ARCH-13](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md) |
| REQ-ARCH-16 | APK de cobranza lista para producción | 0 | [HU-ARCH-08](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-08-apk-a-produccion.md) |
| REQ-ARCH-17 | Higiene de repos y documentación | 0–1 | [HU-REP-01](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-01-limpiar-residuos.md), [HU-ARCH-23](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-23-higiene.md) |
| REQ-ARCH-18 | Modelos y costos de proveedores vigentes | 0 | [HU-ARCH-10](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-10-modelos-deepseek-vigentes.md), [HU-ARCH-11](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-11-un-mensaje-por-defecto.md) |
| REQ-ARCH-19 | Release y pruebas E2E entre repos | 0 | [HU-ARCH-09](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-09-release-y-e2e-entre-repos.md) |
| REQ-ARCH-20 | Consistencia del asistente medida con pass^k, usuario simulado y aserciones sobre el estado final | 0 | [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md), [HU-AOS-21](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md) |
| REQ-ARCH-21 | Verificación determinista de afirmaciones (montos, links, fechas, estados) contra la evidencia del sistema | 0 | [HU-ARCH-29](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md), [HU-AOS-06](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md) |
| REQ-ARCH-22 | Centro de pruebas: catálogo versionado en git con todas las pruebas del proyecto, ciclos con historial, ejecución paso a paso con capturas e informe por tester, y rol tester (master en la operación y dueño en Colaboradores, solo en test) para internos y externos | 1 | [HU-QA-01](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-01-modelo-y-api-de-pruebas.md), [HU-QA-02](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-02-catalogo-versionado-desde-docs.md), [HU-QA-03](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-03-seccion-pruebas-en-el-panel.md), [HU-QA-04](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-04-rol-tester-e-invitaciones.md), [HU-QA-05](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-05-migrar-desde-el-artifact.md), [HU-QA-06](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-06-catalogo-historico-del-proyecto.md), [HU-QA-07](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-07-datos-de-prueba.md), [HU-QA-08](../04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-08-pruebas-por-entorno-y-seccion.md) |
| REQ-GTM-09 | Claims coherentes y honestos | 0 | HU-GTM-05 |
| REQ-GTM-10 | Matriz competitiva corregida | 1 | [HU-GTM-11](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-GTM-11-matriz-corregida.md) |
| REQ-GTM-11 | Primer cliente de pago por vertical | 0 | HU-GTM-06 |
| REQ-GTM-12 | Kit comercial v2 | 0 | HU-GTM-04 |
| REQ-GTM-13 | Oferta de agencia | 2 | [HU-GTM-12](../05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-GTM-12-oferta-de-agencia.md) |

### Billing v2 (REQ-BILL)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-BILL-01 | Unidad de crédito derivada de costos con margen prudente | 0 | HU-BILL-01, HU-BILL-02 |
| REQ-BILL-02 | Tarifario versionado y costeo exacto por proveedor, modelo y llave | 0 | HU-BILL-03 |
| REQ-BILL-03 | Ledger multi-concepto con créditos inmutables e idempotentes | 0 | HU-BILL-04, [HU-MEDIA-03](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-03-stt-notas-de-voz.md), [HU-MEDIA-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/hu/HU-MEDIA-04-dispatcher-de-vision.md) |
| REQ-BILL-04 | Planes v2: créditos + límites estructurales | 0 | HU-BILL-05 |
| REQ-BILL-05 | Enforcement determinista con colchón de gracia y auditoría | 0 | HU-BILL-06 |
| REQ-BILL-06 | Uso visible en el panel (saldo, proyección, desglose, avisos 80/100 %) | 0–1 | HU-BILL-07, [HU-UI-12](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-12-packs-costos-y-plan-compactos.md) |
| REQ-BILL-07 | Precios públicos coherentes con el core | 0 | HU-BILL-08 |
| REQ-BILL-08 | Avisos de consumo fuera del panel | 1 | [HU-BILL-09](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-09-avisos-de-consumo.md) |
| REQ-BILL-09 | Recargas de créditos | 1 | [HU-BILL-10](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-10-recargas.md) |
| REQ-BILL-10 | Margen visible para la plataforma | 1 | [HU-BILL-11](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-11-margen-master.md) |
| REQ-BILL-11 | Renovación, cambio de plan y ciclos anuales | 0–1 | [HU-SH-04](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md), [HU-BILL-12](../04-fase-1-competir/SPEC-14-billing-extras/hu/HU-BILL-12-cambio-de-plan-y-anual.md) |
| REQ-BILL-12 | Cobro internacional y de agencia | 2 | [HU-BILL-13](../05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-BILL-13-cobro-internacional.md), [HU-BILL-14](../05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-BILL-14-billing-de-agencia.md) |

### Framework y habilidades (REQ-FWK)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-FWK-01 | Composición multi-pack correcta del flujo | 0 | [HU-FWK-01](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-01-composicion-de-flujos.md) |
| REQ-FWK-02 | Presets de agente por tipo de negocio | 0–1 | [HU-FWK-02](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-02-adr-presets.md), [HU-FWK-03](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), [HU-FWK-10](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-10-aplicar-preset-desde-panel.md), [HU-FWK-11](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-11-presets-adicionales.md), HU-SUB-11, [HU-AOS-46](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) |
| REQ-FWK-03 | Seeds genéricos por pack | 0 | [HU-FWK-03](../03-fase-0-go-live/SPEC-05-presets-y-flujos/hu/HU-FWK-03-registro-de-presets-y-seeds.md), HU-SUB-11 |
| REQ-FWK-04 | Catálogo de habilidades con metadatos | 1 | [HU-FWK-04](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-04-catalogo-de-habilidades.md) |
| REQ-FWK-05 | Pantallas de packs por descriptores, sin desplegar el panel | 1 | [HU-FWK-05](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-05-manifiesto-de-menu.md), [HU-FWK-06](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-06-descriptores-y-api-de-vistas.md), [HU-FWK-07](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-07-descriptor-view.md), [HU-FWK-08](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-08-formulario-de-schema-v2.md), [HU-FWK-09](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-09-tools-declarativas-panel.md) |
| REQ-FWK-06 | Plugin del tenant formalizado | 2 | [HU-FWK-13](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FWK-13-plugin-del-tenant.md) |
| REQ-FWK-07 | Un error de negocio nunca apaga una habilidad | 0 | [HU-ARCH-18](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-18-errores-de-negocio-no-apagan-packs.md) |
| REQ-FWK-08 | Organizaciones y sub-cuentas | 2 | [HU-FWK-12](../05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-FWK-12-organizaciones-y-subcuentas.md) |

### UX (REQ-UX)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-UX-01 | Arquitectura de información y glosario de negocio | 1 | [HU-UX-01](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-01-adr-arquitectura-de-informacion.md), [HU-UX-02](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md) |
| REQ-UX-02 | Onboarding guiado | 0–1 | [HU-SH-06](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md), [HU-UX-05](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-05-guias-por-habilidad.md), [HU-UX-06](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-06-registro-desde-landing.md) |
| REQ-UX-03 | Ayuda contextual, estados vacíos y permisos coherentes | 1 | [HU-UX-03](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-03-ayuda-contextual.md), [HU-UX-04](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-04-estados-vacios-y-permisos.md) |
| REQ-UX-04 | Vistas operativas profesionales | 1 | [HU-UI-05](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-05-tickets-reales.md) a [HU-UI-12](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-12-packs-costos-y-plan-compactos.md), [HU-MEDIA-07](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-MEDIA-07-visor-de-media.md) |
| REQ-UX-05 | Feedback consistente y acciones seguras | 0 | [HU-UI-01](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-01-bugs-visibles.md), [HU-UI-02](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-02-kit-de-feedback.md) |
| REQ-UX-06 | Panel responsive, accesible y probado | 0 | [HU-UI-03](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-03-shell.md), [HU-UI-04](../03-fase-0-go-live/SPEC-10-panel-confiable/hu/HU-UI-04-calidad-del-panel.md), [HU-ARCH-09](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-09-release-y-e2e-entre-repos.md) |
| REQ-UX-07 | Cuenta y notificaciones a operadores | 1 | [HU-UI-13](../04-fase-1-competir/SPEC-13-vistas-profesionales/hu/HU-UI-13-cuenta-y-notificaciones.md) |
| REQ-UX-08 | Reporte mensual automático | 2 | [HU-UX-07](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/hu/HU-UX-07-reporte-mensual.md) |
| REQ-UX-09 | Sistema de diseño unificado para panel y app: tokens completos, kit documentado y contraste AA verificado en CI | 1 | [HU-DS-01](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-01-tokens-v2.md), [HU-DS-02](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-02-contraste-aa-y-gates.md), [HU-DS-03](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-03-kit-de-componentes-panel.md), [HU-DS-06](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-06-primitivas-de-visualizacion.md), [HU-DS-09](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-09-kit-de-componentes-app.md), [HU-DS-12](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-12-motion-y-microinteracciones.md) |
| REQ-UX-10 | Shell adaptativo del panel: barra lateral plegable que recuerda la preferencia, migas, pestañas de sección, paleta de comandos y atajos | 1 | [HU-DS-04](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-04-shell-adaptativo-del-panel.md), [HU-DS-05](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-05-paleta-de-comandos-y-atajos.md) |
| REQ-UX-11 | Resumen por rol con KPIs comparados, tendencias, alertas y acciones, personalizable | 1 | [HU-DS-07](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-07-resumen-modular-por-rol.md), [HU-DS-08](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-08-widgets-reorganizables.md), [HU-DS-11](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md) |
| REQ-UX-12 | Menú v2 por tarea con ≤ 12 entradas de primer nivel, pestañas dentro de cada sección y redirecciones de las rutas viejas (D-37) | 1 | [HU-UX-02](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md), [HU-UX-10](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-10-cobranza-y-ventas-en-pestanas.md) |
| REQ-UX-13 | Fichas por objeto: conexión con pestañas según su tipo y agente con sus conexiones, enlazados en las dos direcciones (D-37) | 1 | [HU-UX-09](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md) |
| REQ-UX-14 | Agenda unificada: calendario con creación de citas y bloqueos, tipos de cita con color y horario de agendamiento (D-37) | 1 | [HU-UX-08](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-08-agenda-unificada.md) |
| REQ-UX-15 | El cajón del panel en la app sigue el menú v2 del panel web (D-34, D-37) | 1 | [HU-UX-11](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md) |
| REQ-UX-16 | Panel sin tropiezos: tooltips visibles, una sola paginación, avisos de 4 tipos con ícono y textos y validaciones siempre en español (D-38) | 1 | [HU-UX-12](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-12-arreglos-rapidos-del-ciclo.md), [HU-UX-13](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-13-avisos-y-formularios-en-espanol.md) |
| REQ-UX-17 | Shell v2: plegar junto al logo, bloque de usuario con menú (perfil, tema, cerrar sesión), perfil editable, pestañas sobre el título (D-38) | 1 | [HU-UX-14](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-14-shell-v2-y-perfil.md) |
| REQ-UX-18 | Bandeja de conversaciones en vivo estilo WhatsApp Web, con la conexión de cada chat, tickets y notas internas (D-38) | 1 | [HU-UX-15](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-15-bandeja-de-conversaciones.md) |
| REQ-UX-19 | Clientes con ficha editable de lo que el agente aprendió, pausa del agente por cliente, clasificación, filtros por canal y conexión y CSV (D-38) | 1 | [HU-UX-16](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-16-clientes-estilo-agent-sale.md) |
| REQ-UX-20 | Motivos de escalación con lista cerrada, etiqueta, color y filtro (D-38) | 1 | [HU-UX-17](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-17-motivos-de-escalacion-legibles.md) |
| REQ-UX-21 | Listas y formularios de sección claros: promesas con detalle, formularios de habilidad por grupos, guardrails a la vista y paso de habilidad sin configurar (D-38) | 1 | [HU-UX-18](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-18-listas-y-formularios-de-seccion.md) |
| REQ-UX-22 | Centro de notificaciones en el panel y la app (D-38) | 1 | [HU-UX-19](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-19-centro-de-notificaciones.md) |
| REQ-UX-23 | La app cubre lo que faltó en el ciclo: búsqueda en Negocios, Inicio sin conexión con esqueletos y notas de cartera (D-38) | 1 | [HU-UX-20](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-UX-20-apk-lo-que-falto-del-ciclo.md) |

### Editor de flujo (REQ-FLOW)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-FLOW-01 | Flujo versionado en el AgentSpec, con borrador | 1 | [HU-FLOW-01](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-01-adr-editor-de-flujo.md), [HU-FLOW-02](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-02-flujo-en-agentspec.md) |
| REQ-FLOW-02 | Editor visual por pack: agregar, quitar y reordenar tools | 1 | [HU-FLOW-03](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-03-validador-y-api.md), [HU-FLOW-04](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-04-editor-visual.md) |
| REQ-FLOW-03 | Probar el borrador y publicar con rollback | 1 | [HU-FLOW-05](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-05-borrador-y-publicacion.md) |
| REQ-FLOW-04 | Flujo semilla por preset | 1 | [HU-FLOW-06](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/hu/HU-FLOW-06-flujo-semilla-por-preset.md) |
| REQ-FLOW-05 | Edición avanzada del `purpose` y reglas por etapa | 2 | [HU-FLOW-07](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-FLOW-07-purpose-y-reglas-por-etapa.md) |

### Planes y suscripciones (REQ-SUB)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-SUB-01 | Contrato único de suscripción con proveedores intercambiables | 0 | HU-SUB-01, HU-SUB-09, HU-SUB-15 |
| REQ-SUB-02 | Ciclo de vida, cobro y mora correctos | 0 | HU-SUB-02, HU-SUB-04, HU-SUB-05, HU-SUB-06, HU-SUB-13, HU-SUB-18 |
| REQ-SUB-03 | Planes como productos, recurrencia editable y cambio de plan | 0 | HU-SUB-07, HU-SUB-10 |
| REQ-SUB-04 | Eventos de dominio durables | 0 | HU-SUB-03, HU-SUB-14 |
| REQ-SUB-05 | Administración y métricas de suscripciones | 0–1 | HU-SUB-08, [HU-SUB-16](../04-fase-1-competir/SPEC-20-crecimiento/hu/HU-SUB-16-mrr-y-embudo.md) |
| REQ-SUB-06 | "Planes y suscripciones" replicable como preset | 0 | HU-SUB-11, HU-SUB-12 |
| REQ-SUB-07 | Débito recurrente automático | 2 | [HU-SUB-17](../05-fase-2-plus/SPEC-21-agencia-e-internacional/hu/HU-SUB-17-debito-recurrente.md) |

### Asistente SolversHub (REQ-SH)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-SH-01 | Asistente SolversHub reproducible y medido | 0 | [HU-SH-01](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-01-tenant-reproducible.md), [HU-SH-08](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-08-golden-set-asistente.md) |
| REQ-SH-02 | Demo agendada de punta a punta | 0 | [HU-SH-02](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-02-demo-de-punta-a-punta.md) |
| REQ-SH-03 | Alta automática con identidad de servicio | 0 | [HU-SH-03](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md) |
| REQ-SH-04 | Cobro de plataforma por dos canales con fuente única | 0 | [HU-SH-04](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-04-cobro-de-plataforma-dos-canales.md) |
| REQ-SH-05 | WhatsApp del cliente por Embedded Signup y onboarding autoservicio | 0 | [HU-SH-05](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md), [HU-SH-06](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md) |
| REQ-SH-06 | Antiabuso y cumplimiento del alta | 0 | [HU-SH-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md) |
| REQ-SH-07 | Atribución de la landing al asistente | 0 | [HU-SH-09](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-09-landing-con-atribucion.md) |

### Conexiones (REQ-CONN)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-CONN-01 | Credenciales y webhook por conexión | 0 | [HU-CONN-01](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md), [HU-CONN-05](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md) |
| REQ-CONN-02 | Ciclo de vida seguro y diagnóstico confiable | 0 | [HU-CONN-02](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-02-errores-500-y-bloqueos.md), [HU-CONN-03](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-03-ciclo-de-vida-seguro.md), [HU-CONN-04](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-04-diagnostico-confiable.md) |
| REQ-CONN-03 | Producción con Meta efectiva, de prueba a producción | 0 | [HU-CONN-06](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md), [HU-CONN-07](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-07-checklist-produccion-real.md), [HU-SH-05](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md) |
| REQ-CONN-04 | Lista clara y hub por tipo de conexión | 0 | [HU-CONN-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md), [HU-CONN-10](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-10-conexiones-no-meta.md) |
| REQ-CONN-05 | Costos de Meta verificables y opcionales | 0 | [HU-CONN-09](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-09-costos-meta-verificables.md) |

### Comercio (REQ-COM)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-COM-01 | El dinero nunca pasa por el LLM | 0 | [HU-COM-01](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-01-dinero-en-el-servidor.md) |
| REQ-COM-02 | Guardrails y datos según el tipo de producto | 0 | [HU-COM-02](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-02-guardrails-correctos.md), [HU-COM-03](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-03-numeracion-y-datos-por-producto.md) |
| REQ-COM-03 | Pedido confiable de punta a punta | 0 | [HU-COM-04](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-04-barrido-de-defectos.md), [HU-COM-05](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-05-estados-del-pedido.md), [HU-COM-06](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-06-operacion-de-pagos.md), [HU-COM-09](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-09-modificar-pedido.md) |
| REQ-COM-04 | Catálogo para menús y retail | 0–1 | [HU-COM-07](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-07-catalogo-menus-y-retail.md), [HU-COM-15](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-15-modificadores-y-combos.md) |
| REQ-COM-05 | Domicilios | 0 | [HU-COM-08](../03-fase-0-go-live/SPEC-09-comercio-confiable/hu/HU-COM-08-domicilios.md) |
| REQ-COM-06 | Proactividad y promociones v2 | 1 | [HU-COM-10](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-10-proactividad-v2.md), [HU-COM-11](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-11-promociones-v2.md) |
| REQ-COM-07 | Analítica, búsqueda y CRM de ventas | 1 | [HU-COM-12](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-12-kpis-de-ventas.md), [HU-COM-13](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-13-busqueda-y-recomendaciones.md), [HU-COM-14](../04-fase-1-competir/SPEC-18-pack-commerce-v2/hu/HU-COM-14-lead-y-pedido.md) |
| REQ-COM-08 | Varias sucursales | 2 | [HU-COM-16](../05-fase-2-plus/SPEC-22-extensibilidad-avanzada/hu/HU-COM-16-multisucursal.md) |

### Agenda y citas (REQ-CAL)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-CAL-01 | Calendario interno configurable sin Google: horario, tipos de cita, bloqueos y agenda operables desde el panel | 1 | [HU-CAL-01](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-01-bloqueos-de-agenda.md), [HU-CAL-02](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-02-agendar-reagendar-cancelar.md), [HU-CAL-03](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-03-calendario-visual.md), [HU-CAL-05](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-05-pack-de-agendamiento-definitivo.md) |
| REQ-CAL-02 | Agendamiento conversacional confiable: fechas relativas correctas desde la fecha y zona del negocio, confirmaciones solo con evidencia de la tool, aviso y link de la cita al cliente, sin escalar por fallos técnicos | 1 | [HU-CAL-04](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-04-fecha-actual-y-anti-escalamiento.md), [HU-CAL-05](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-05-pack-de-agendamiento-definitivo.md), [HU-CAL-06](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-06-afinado-del-tenant-y-e2e.md) |
| REQ-CAL-03 | Conexión opcional con Google Calendar desde el panel, con OAuth seguro (retorno por el panel, `state` anti-CSRF, tokens en la conexión del negocio) | 1 | [HU-CAL-07](../04-fase-1-competir/SPEC-24-agenda-y-citas/hu/HU-CAL-07-google-desde-el-panel.md) |

### Reestructura (REQ-REP)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-REP-01 | Nombres `solvershub-<section>` y repos limpios | 0–1 | [HU-REP-01](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-01-limpiar-residuos.md), [HU-REP-02](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-02-renombre-cosmetico.md), [HU-REP-03](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-03-transicion-de-identificadores.md), [HU-REP-05](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-05-repo-solvershub-docs.md), [HU-REP-07](../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-REP-07-solvershub-brand.md) |
| REQ-REP-02 | Infraestructura versionada | 0 | [HU-REP-06](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-06-solvershub-infra.md) |
| REQ-REP-03 | Sin marca técnica ante el cliente | 0 | [HU-REP-04](../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-04-sin-fugas-de-marca-tecnica.md) |

### App móvil oficial (REQ-APP)

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-APP-01 | Una sola app modular para todo el panel, con fronteras entre módulos verificadas en CI | 1 | [HU-APP-01](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-01-nucleo-modular-de-la-app.md), [HU-APP-07](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md) |
| REQ-APP-02 | Auth completo en la app: login, cierre de sesión, recuperación de contraseña y desbloqueo biométrico | 1 | [HU-APP-02](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-02-sesion-unica-y-recuperacion.md) |
| REQ-APP-03 | Los módulos de la app aparecen según los permisos del usuario, el negocio y el rol | 1 | [HU-APP-03](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-03-navegacion-por-permisos.md) |
| REQ-APP-04 | Dashboard móvil con KPIs e indicadores del negocio | 1 | [HU-APP-04](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-04-dashboard-con-kpis.md) |
| REQ-APP-05 | Notificaciones push en la app para eventos del negocio y de campo | 1 | [HU-APP-05](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-05-notificaciones-push.md) |
| REQ-APP-06 | Datos locales cifrados en reposo (base local, cola offline, caché) | 1 | [HU-APP-06](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md), [HU-APP-16](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-16-seguridad-de-la-app.md) |
| REQ-APP-07 | Réplica del panel en la app: operación, negocio, comercio, calendario, configuración, herramientas y plataforma | 1 | [HU-APP-08](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-08-operacion-movil.md), [HU-APP-09](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-09-negocio-movil.md), [HU-APP-10](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-10-comercio-movil.md), [HU-APP-11](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-11-calendario-movil.md), [HU-APP-12](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-12-configuracion-movil.md), [HU-APP-13](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-13-herramientas-y-plataforma-movil.md) , [HU-APP-18](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-18-cobranza-admin-movil.md) |
| REQ-APP-08 | Búsqueda global en la app con resultados por sección respetando permisos | 1 | [HU-APP-14](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-14-busqueda-global.md) |
| REQ-APP-09 | La app funciona con conexión intermitente: escrituras encoladas idempotentes y lecturas con caché y sync incremental | 1 | [HU-APP-07](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-07-cobranza-al-nucleo-sin-regresion.md), [HU-APP-15](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-15-sync-offline-por-modulos.md) |
| REQ-APP-10 | Release firmado y reproducible (dev/staging/prod) con guías de build y rollback | 1 | [HU-APP-17](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-17-release-firmado-y-guias.md) |
| REQ-APP-11 | La app usa el mismo sistema de diseño que el panel y conserva las vistas y el flujo de campo de cobranza | 1 | [HU-DS-09](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-09-kit-de-componentes-app.md), [HU-DS-10](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-10-cobranza-de-campo-con-el-kit.md), [HU-DS-11](../04-fase-1-competir/SPEC-29-sistema-de-diseno-unificado/hu/HU-DS-11-shell-del-panel-en-la-app.md) |

### Agent OS (REQ-AOS)

Nacen de la decisión D-27 (2026-10-08): vender SolversHub como sistema operativo de agentes con
operabilidad confiable, precisa y coherente. Ver [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md). REQ-AOS-17 nace de D-35 (2026-10-17): SolversHub vende agentes y el cliente ve cada agente y la data que construyó.

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-AOS-01 | La conexión es la unidad de ejecución: cada conexión con 1 Coordinador y N agentes, y una conversación por (conexión, cliente) | 1–2 | [HU-AOS-01](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-01-adrs-del-agent-os.md), [HU-AOS-11](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-11-conexion-canonica.md), [HU-AOS-13](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-13-instancias-por-conexion.md), [HU-AOS-15](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md), [HU-AOS-42](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-42-canal-api-y-webhooks.md), [HU-AOS-43](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-43-slack-y-correo-entrante.md) |
| REQ-AOS-02 | Todo recurso configurable declara su scope (negocio o conexión) | 1 | [HU-AOS-02](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-02-esquema-aditivo.md), [HU-AOS-16](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md) |
| REQ-AOS-03 | Procedimientos tipados y versionados (superpoderes) que el kernel hace cumplir | 1–2 | [HU-AOS-01](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-01-adrs-del-agent-os.md), [HU-AOS-03](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-03-contrato-de-procedimientos.md), [HU-AOS-05](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-05-motor-de-procedimientos.md), [HU-AOS-06](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-06-comandos-y-verificador-sobre-estado.md), [HU-AOS-07](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-07-procedimientos-de-comercio.md), [HU-AOS-08](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-08-procedimientos-de-agenda-suscripciones-y-cobranza.md), [HU-AOS-09](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md), [HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md), [HU-AOS-45](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md) |
| REQ-AOS-04 | Estado único de la conversación, visible para agentes y personas | 1 | [HU-AOS-04](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-04-estado-de-la-conversacion.md), [HU-AOS-28](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md) |
| REQ-AOS-05 | Agentes especialistas versionados y reutilizables entre conexiones | 1 | [HU-AOS-12](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-12-agentes-versionados.md), [HU-AOS-13](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-13-instancias-por-conexion.md), [HU-AOS-16](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md), [HU-AOS-24](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md), [HU-AOS-46](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) |
| REQ-AOS-06 | Coordinador determinista con LLM como coprocesador | 1 | [HU-AOS-09](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-09-modelo-por-riesgo-y-confirmacion-con-boton.md), [HU-AOS-10](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-10-kernel-del-coordinador.md), [HU-AOS-17](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-17-enrutamiento-y-modo-sombra.md) |
| REQ-AOS-07 | Colaboración entre agentes en 5 modos con permisos, límites y presupuesto | 1 | [HU-AOS-18](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-19](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-19-handoff-delegacion-y-consulta.md), [HU-AOS-20](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-20-colaboracion-con-pila-de-tareas.md), [HU-AOS-22](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-22-dogfooding-solvershub.md), [HU-AOS-26](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-26-colaboracion-en-el-panel.md), [HU-AOS-30](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-30-agentes-de-back-office.md) |
| REQ-AOS-08 | Trazabilidad de punta a punta: decisión, comandos, acciones, estado, A2A, costo y feedback | 1 | [HU-AOS-10](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-10-kernel-del-coordinador.md), [HU-AOS-18](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-28](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-28-depurador-y-en-curso.md), [HU-AOS-29](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md) |
| REQ-AOS-09 | Aislamiento entre negocios garantizado en el esquema; federación solo consentida | 1–2 | [HU-AOS-02](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-02-esquema-aditivo.md), [HU-AOS-18](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-39](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-39-federacion-entre-negocios.md) |
| REQ-AOS-10 | Releases por conexión con rollback en un clic y canary | 1 | [HU-AOS-14](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-14-releases-por-conexion.md), [HU-AOS-27](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-27-versiones-en-el-panel.md), [HU-AOS-32](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-32-canary-y-auto-rollback.md) |
| REQ-AOS-11 | Memoria y caché por scope, invalidadas por versión | 1 | [HU-AOS-35](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-35-cache-por-version.md), [HU-AOS-36](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-36-memoria-por-scope.md) |
| REQ-AOS-12 | Consistencia como gate de release y mejora continua con aprobación humana | 1–2 | [HU-AOS-15](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md), [HU-AOS-21](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-21-gate-de-release-pass-k.md), [HU-AOS-22](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-22-dogfooding-solvershub.md), [HU-AOS-29](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md), [HU-AOS-31](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-31-auditor-de-calidad.md), [HU-AOS-33](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-33-feedback-y-propuestas.md), [HU-AOS-41](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-41-auto-mejora-asistida.md) |
| REQ-AOS-13 | Consola del Agent OS usable por no técnicos | 1–2 | [HU-AOS-23](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md), [HU-AOS-24](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-24-editor-de-agentes.md), [HU-AOS-25](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-25-superpoderes-en-el-panel.md), [HU-AOS-26](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-26-colaboracion-en-el-panel.md), [HU-AOS-27](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-27-versiones-en-el-panel.md), [HU-AOS-38](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-38-lanzamiento-comercial.md), [HU-AOS-45](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md), [HU-AOS-47](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md) |
| REQ-AOS-14 | Costos y cuotas por conexión, agente y operación entre agentes | 1 | [HU-AOS-37](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md), [HU-AOS-38](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-38-lanzamiento-comercial.md) |
| REQ-AOS-15 | Acciones aisladas con tiempo máximo, reintentos seguros, circuit breaker y sandbox | 1–2 | [HU-AOS-34](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-34-acciones-v2.md), [HU-AOS-40](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-40-sandbox-de-acciones.md) |
| REQ-AOS-16 | Topología escalable por roles con disparadores medidos, sin microservicios | 2 | [HU-AOS-44](../05-fase-2-plus/SPEC-27-agent-os-plus/hu/HU-AOS-44-topologia-por-roles.md) |
| REQ-AOS-17 | Cada agente del negocio muestra la data que construyó: conversaciones, tareas, clientes y leads, registros creados (pedidos, citas, promesas), consumo y consistencia; `/admin/plan` expone agentes publicados y colaboradores (D-35) | 1 | [HU-AOS-47](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md) |
| REQ-AOS-18 | Un agente se configura con un guion de unas 10 preguntas según su fin, ofrecido al primer ingreso (D-38) | 1 | [HU-AOS-48](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-48-onboarding-con-guion-por-agente.md) |
| REQ-AOS-19 | Cada agente puede usar documentos del negocio como conocimiento, con búsqueda configurable y aislada por tenant (D-38) | 1 | [HU-AOS-49](../04-fase-1-competir/SPEC-31-mejoras-del-ciclo-de-pruebas/hu/HU-AOS-49-pack-de-conocimiento.md) |

### Vertical inmobiliaria (REQ-INMO)

Nacen de la decisión D-31 (2026-10-09): asistente inmobiliario sobre la arquitectura de agent-core y el
Agent OS planificado. Ver [SPEC-28](../04-fase-1-competir/SPEC-28-inmoagent/spec.md).

| REQ | Requerimiento | Fase | HU |
|---|---|---|---|
| REQ-INMO-01 | Inventario de inmuebles en venta y arriendo con características, medios y ubicación precisa, aislado por negocio | 1 | [HU-INMO-10](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-10-pack-inmobiliario-inventario-geoespacial.md), [HU-INMO-11](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-11-inventario-y-captaciones-en-el-panel.md) |
| REQ-INMO-02 | Búsqueda por operación, tipo, precio, habitaciones, baños, área, estado, características y texto libre | 1 | [HU-INMO-14](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-14-busqueda-con-filtros-y-geo.md) |
| REQ-INMO-03 | Geolocalización: geocodificación confirmada, búsqueda por zona, radio, rango de distancia y cercanía a puntos de interés | 1 | [HU-INMO-12](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-12-geocodificacion-y-zonas.md), [HU-INMO-13](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-13-puntos-de-interes-y-cercanias.md), [HU-INMO-14](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-14-busqueda-con-filtros-y-geo.md) |
| REQ-INMO-04 | Interpretación del interés: recomendaciones explicadas, relajación de filtros, perfil persistente y hechos verificados | 1 | [HU-INMO-15](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-15-recomendaciones-y-relajacion.md), [HU-INMO-16](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-16-perfil-de-busqueda-persistente.md), [HU-INMO-17](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-17-fichas-y-verificacion-de-hechos.md) |
| REQ-INMO-05 | Captación de inmuebles de propietarios por WhatsApp y formulario, con validación y aviso al asesor | 1 | [HU-INMO-11](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-11-inventario-y-captaciones-en-el-panel.md), [HU-INMO-18](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-18-captacion-de-propietarios.md) |
| REQ-INMO-06 | Visitas agendadas en la agenda real del asesor del inmueble, con confirmación y recordatorios | 1 | [HU-INMO-05](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-05-agenda-por-responsable.md), [HU-INMO-06](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-06-agenda-como-capacidad-del-core.md), [HU-INMO-19](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-19-visitas-con-el-asesor.md) |
| REQ-INMO-07 | Pipeline comercial con asignación de asesor y relevo a la persona correcta | 1 | [HU-INMO-07](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-07-escalamiento-al-responsable.md), [HU-INMO-20](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-20-oportunidades-y-asesores.md) |
| REQ-INMO-08 | Arriendos: contrato como registro, cobro del canon, mora e incremento anual dentro del tope legal | 1 | [HU-INMO-08](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-08-suscripciones-de-plazo-fijo.md), [HU-INMO-23](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-23-contrato-de-arriendo-y-canon.md), [HU-INMO-24](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-24-mora-e-incremento-del-canon.md) |
| REQ-INMO-09 | Proactividad con consentimiento: seguimiento post-visita, encuesta, alertas de coincidencias y reenganche | 1 | [HU-INMO-21](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-21-seguimiento-post-visita-y-encuesta.md), [HU-INMO-22](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-22-alertas-y-reenganche.md) |
| REQ-INMO-10 | Mensajes estructurados del canal (ubicación, botones, listas) y avisos por evento declarados por las habilidades | 1 | [HU-INMO-02](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-02-entrada-estructurada-whatsapp.md), [HU-INMO-03](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-03-salida-interactiva.md), [HU-INMO-04](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-04-avisos-abiertos-a-habilidades.md) |
| REQ-INMO-11 | Vertical nativa del Agent OS: afirmaciones de la vertical, procedimientos tipados, especialistas, back-office y memoria por scope | 1 | [HU-INMO-27](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-27-procedimientos-1-1.md), [HU-INMO-29](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-29-procedimientos-inmobiliarios.md), [HU-INMO-30](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-30-especialistas-inmobiliarios.md), [HU-INMO-31](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-31-back-office-y-memoria.md) |
| REQ-INMO-12 | Cumplimiento (supresión de datos del titular, decisiones y ADR), preset replicable, evals y KPIs de la vertical | 1 | [HU-INMO-01](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-01-adrs-y-dor-del-piloto.md), [HU-INMO-09](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-09-supresion-de-datos-del-titular.md), [HU-INMO-25](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-25-preset-golden-y-journeys.md), [HU-INMO-26](../04-fase-1-competir/SPEC-28-inmoagent/hu/HU-INMO-26-kpis-de-la-vertical.md) |

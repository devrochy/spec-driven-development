# 01 · Re-validación

Antes de proponer nada se volvieron a validar los tres insumos: la matriz de competencia, el plan
vigente (`solvershub-comercial/PLAN-COMPETENCIA-Y-PRODUCCION.md`) y el código real de los repos
`solvershub-*`. Esta carpeta guarda la evidencia; las decisiones que salen de aquí están en
[`02-vision-y-decisiones/`](../02-vision-y-decisiones/README.md).

**Corte de la evidencia**

| Repo | Rama / commit leído | Fecha |
|---|---|---|
| `solvershub-backend` (GitHub `devrochy/agent-core`) | `origin/develop` `b0f54d3` (PR #164–#170). Primera auditoría sobre `agent-core` `0cb3f21` | 2026-09-28 y 2026-10-01 |
| `solvershub-panel` | `4749ad5` | 2026-10-01 |
| `solvershub-landing` | `main` `256b1f6` (con cambios sin commitear en `app/globals.css`) | 2026-10-01 |
| `solvershub-apk` | `fb94ddb` | 2026-10-01 |
| `solvershub-comercial` | `main` `7efbf53` | 2026-10-01 |

Las rutas citadas como `ruta:línea` son relativas a la raíz de cada repo. Los hallazgos marcados
"(re-verificado 2026-10-01)" se volvieron a comprobar sobre el código actual; los demás vienen de la
auditoría del 2026-09-28 y su línea puede haberse movido unas pocas posiciones.

## Insumos leídos

**Directamente**

- `solvershub-comercial/`: `PLAN-COMPETENCIA-Y-PRODUCCION.md`, `estudio_mercado_agentes_ia.xlsx`
  (y su `.backup`), `PRODUCCION-SOLVERSHUB.md`, `security.md`, `comercial/README.md`,
  `comercial/roi-calculator.html`, `legal/{README,contrato-servicio,dpa,aviso-privacidad}.md`,
  `runbooks/{README,backup-restore,go-live,incident-response,onboarding-cliente,alta-agente-agencia}.md`,
  `PARIDAD-PANEL.md`, `PARIDAD-ACCIONES.md`, `REPORTE-DE-PRUEBAS-2026-09-28.md`.
- `solvershub-backend/`: `CLAUDE.md`; `docs/{ROADMAP,BACKLOG,BILLING,ASSISTANT-OS,ARCHITECTURE,MULTITENANT,PLUGIN-CONTRACT,WORKFLOW,SDD-TECH-STACK}.md`;
  ADR 0008, 0017, 0033, 0045, 0046, 0050, 0052, 0054, 0055–0068, 0076–0085;
  `core/billing/{plans,metrics,enforcement,service,checkout}.py`, `core/llm/{__init__,openai_compatible,anthropic_provider}.py`,
  `core/subscriptions/__init__.py`, `core/config.py`, `core/orchestrator/{loop,consumer}.py`,
  `core/gateway/{webhooks,meta_byok,sender,message_splitter,meta_production_readiness}.py`,
  `core/api/routers/platform.py`, `packages/pack-{commerce,cobranza,payments,subscriptions,calendar}/**`,
  `tenants/solvershub/**`.
- `solvershub-landing/`: `lib/plans.ts`, `app/precios/page.tsx`, `lib/faq.ts`, `docs/plan-auditoria.md`.
- `solvershub-panel/`: `brand/manual-de-marca.md`, `brand/tokens/*`, `apps/panel-web/DESIGN.md`.

**Vía exploración con agentes (informes con `ruta:línea`, revisados y re-verificados por muestreo)**

- Inventario de repos, nombres y carpeta `apps/` (2026-09-30).
- Brechas del flujo demo → plan → suscripción (2026-09-30).
- Plan previo contra el código, panel, packs, flujo y AgentSpec (2026-09-28).
- `agent-sale` (media, visión, OCR), APK de cobranza y landing (2026-09-28).
- Barrido `agent-sale` → `pack-commerce` (2026-10-01).
- Revisión de vistas del panel nuevo contra `agent-sale` (2026-10-01).
- Auditoría de Conexiones, flujo Meta y costos de Meta en el panel nuevo (2026-10-01).

**No se pudo leer**

- Archivos `.env*` (regla de denegación del entorno): los valores configurados no están verificados.
- El diff de los commits `ba251fe` y `e3790a8` de `solvershub-comercial` ("rotar la credencial del
  admin master"): quedó bloqueado. **El cliente debe revisar si `PLAN-DE-PRUEBAS.md` tiene una
  credencial en el historial** ([HU-ARCH-04](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md)).
- Datos de la base (evals guardados, specs vivos, configs de packs): todo lo que se dice de ellos
  sale de archivos.

## Qué cambió tras la re-validación

1. **La matriz no es lo que el plan decía**: tiene 13 competidores reales, una columna de ejemplo
   (ChatBotCorp) que hay que borrar y **no incluye a Wolkvox**. → matriz-competitiva.md
2. **SolversHub se reestructuró en repos `solvershub-*`**; la carpeta `apps/` suelta es basura de
   un servidor de desarrollo. → [reestructura-y-nombres.md](reestructura-y-nombres.md)
3. **La mayoría de las brechas del plan sigue abierta**, algunas peor de lo descrito (DLQ
   inalcanzable, caché de Anthropic). → [plan-previo-vs-codigo.md](plan-previo-vs-codigo.md)
4. **El panel SSR se retiró** (147 de 148 rutas migradas) y el panel nuevo aún no está en
   producción. → [panel-nuevo.md](panel-nuevo.md)
5. **Conectar WhatsApp en producción no funciona de punta a punta**: Embedded Signup no está
   conectado y BYOK queda fijado en sandbox. → [conexiones-y-costos-meta.md](conexiones-y-costos-meta.md)
6. **pack-commerce tiene 18 defectos**, entre ellos que el LLM pone el monto del link de pago. →
   [comercio-agent-sale-vs-pack-commerce.md](comercio-agent-sale-vs-pack-commerce.md)
7. **Ya existe una capacidad de suscripción en el core**, pero con dos motores y defectos que
   impiden cobrar de verdad. → [suscripciones-alineacion.md](suscripciones-alineacion.md)
8. **El objetivo "SolversHub vende y cobra solo" es viable con los packs actuales**, con piezas
   centrales por construir. → [brechas-objetivo-solvershub.md](brechas-objetivo-solvershub.md)
9. **Hay 38 hallazgos nuevos**, varios urgentes (modelo de DeepSeek discontinuado, Meta cobra los
   mensajes de servicio desde hoy). → hallazgos-nuevos.md
10. Precios de proveedores verificados en fuentes oficiales. → fuentes-externas.md

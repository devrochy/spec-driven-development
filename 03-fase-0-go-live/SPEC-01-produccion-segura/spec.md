# SPEC-01 · Producción segura y confiable

> Estado SDD: Diseño aprobado · Fase 0 · Hitos 0A y 0B · Workstream Arquitectura/Prod

## Problema

- **Producción corre en la máquina de desarrollo** (invariante 9): hay entornos `main` y `develop`,
  cada uno con su Postgres y Redis, pero en el mismo equipo (`solvershub-backend/docs/despliegue-coolify.md`).
- **No hay panel ni landing de producción**: Coolify de producción solo tiene el backend.
- **Sin backups probados**: ni WAL ni PITR; el volumen `TENANTS_ROOT` (ADR-0085) y las evidencias de
  cobranza no tienen respaldo documentado.
- **Acceso débil**: sin bloqueo por intentos fallidos en la API ni en la API de campo
  (`pack_cobranza/api_gestor.py:144-155`); posible credencial del master en el historial de
  `solvershub-comercial` (sin verificar).
- **Webhook que acepta mensajes sin firma** cuando falta el `app_secret` (re-verificado:
  `core/gateway/webhooks.py:223`).
- **DLQ inalcanzable**: `CONSUMER = "orchestrator-1"` y lectura solo de entradas nuevas
  (re-verificado: `core/orchestrator/consumer.py:59,88`); un mensaje fallido no se reintenta nunca.
- **Sin observabilidad de producción**: `/healthz` estático, sin p99 del webhook ni lag de la cola.
- **APK sin endurecer**: `usesCleartextTraffic: true`, cola offline sin cifrar, sin build EAS real.
- **Sin pruebas E2E entre repos** antes de promover a producción.

## Usuarios y contexto

Clientes de pago (sus datos y su operación), el operador (una persona) y clientes enterprise que
preguntan por continuidad y seguridad.

## Por qué importa (valor empresarial)

Es la diferencia entre un piloto y un negocio: **nadie paga una suscripción a un sistema que vive en
un portátil**. Los backups probados, el webhook firmado y la cola sin pérdidas son exactamente lo que
pregunta un cuestionario de seguridad enterprise, y lo que la columna de SolversHub de la matriz ya
promete ("seguridad, SLOs y DPA listos").

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-ARCH-01](hu/HU-ARCH-01-produccion-fuera-de-dev.md) ★ | Producción fuera de la máquina de desarrollo, con panel y landing | 0A |
| [HU-ARCH-02](hu/HU-ARCH-02-borde-tls-y-webhook-prod.md) ★ | Borde TLS y webhook de Meta de producción verificados | 0A |
| [HU-ARCH-03](hu/HU-ARCH-03-backups-pitr-y-restauracion.md) ★ | Backups WAL/PITR fuera del sitio y restauración probada | 0A |
| [HU-ARCH-04](hu/HU-ARCH-04-endurecer-acceso.md) ★ | Endurecer el acceso | 0A |
| [HU-ARCH-05](hu/HU-ARCH-05-webhook-fail-closed.md) ★ | Webhook fail-closed | 0A |
| [HU-ARCH-06](hu/HU-ARCH-06-consumer-y-dlq.md) ★ | Consumer con reclamo de pendientes y DLQ alcanzable | 0A |
| [HU-ARCH-07](hu/HU-ARCH-07-observabilidad-prod.md) ★ | Observabilidad de producción | 0B |
| [HU-ARCH-08](hu/HU-ARCH-08-apk-a-produccion.md) ★ | APK de cobranza a producción | 0B |
| [HU-ARCH-09](hu/HU-ARCH-09-release-y-e2e-entre-repos.md) | Release y pruebas E2E entre repos | 0B |

## Escenarios clave

- **Corte de la máquina de desarrollo.** Dado producción en su propio servidor, cuando se apaga la
  máquina de desarrollo, entonces los negocios en producción siguen atendiendo.
- **Restauración.** Dado un backup PITR, cuando se restaura a un punto de hace 1 hora en un servidor
  limpio, entonces la base, `TENANTS_ROOT` y las evidencias quedan consistentes dentro del RTO.
- **Mensaje fallido.** Dado un mensaje entrante cuyo procesamiento falla 3 veces, cuando se agota el
  reintento, entonces aparece en "Mensajes fallidos" y se puede reintentar desde el panel.

## Decisiones

- **Infraestructura (✅ tomada: D-19, VPS dedicado con Coolify + S3)**: ver [P-01](../../02-vision-y-decisiones/preguntas-abiertas.md#p-01--infraestructura-de-producción).
- **RPO/RTO (✅ tomada: D-20, WAL/PITR, 15 min / 4 h)**: ver [P-02](../../02-vision-y-decisiones/preguntas-abiertas.md#p-02--rpo-y-rto).

### D-SPEC-01-1 · Borde público

| Opción | Pros | Contras |
|---|---|---|
| **A. Cloudflare Tunnel + Access (como en test)** | Ya funciona; sin puertos abiertos; TLS y WAF de Cloudflare | Dependencia de Cloudflare |
| B. IP pública con Caddy o Traefik | Sin intermediario | Abrir 80/443, gestionar certificados y DDoS |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): Cloudflare Tunnel + Access sobre Coolify.

### D-SPEC-01-2 · Observabilidad

| Opción | Pros | Contras |
|---|---|---|
| **A. Sentry (errores) + OTLP a un servicio gestionado con plan gratuito (Grafana Cloud u otro)** | Rápido, sin servidores extra | Límites del plan gratuito |
| B. Prometheus + Grafana propios | Control total | Más infraestructura que operar para una persona |
| C. Solo logs de Coolify | Cero trabajo | Sin alertas ni SLO medibles |

**Recomendación: A.** Estado: ✅ tomada (2026-10-03): Sentry (errores) + OTLP a un servicio gestionado con plan gratuito.

### D-SPEC-01-3 · Secretos

| Opción | Pros | Contras |
|---|---|---|
| **A. Variables de Coolify + runbook de rotación en `solvershub-infra`** | Lo que hay hoy, documentado | Sin auditoría de acceso a secretos |
| B. Gestor de secretos (Doppler, Vault) | Auditoría y rotación | Otra pieza para una persona |

**Recomendación: A** en la Fase 0; B se reevalúa en [HU-ARCH-22](../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-22-pentest.md). Estado: ✅ tomada (2026-10-02): variables de Coolify + runbook de rotación en `solvershub-infra`.

## Fuera de alcance

Alta disponibilidad multi-región, Kubernetes, status page pública ([HU-ARCH-21](../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-21-status-page-y-slos.md)), pentest ([HU-ARCH-22](../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-22-pentest.md)).

## Métricas de éxito

- Producción sin dependencia de la máquina de desarrollo (prueba de apagado).
- Restauración medida ≤ RTO acordado, con evidencia trimestral.
- 0 mensajes perdidos: todo fallo termina procesado o en la DLQ.
- p99 del webhook < 1 s y alertas de error activas.

## Requerimientos cubiertos

REQ-ARCH-01, REQ-ARCH-02, REQ-ARCH-03, REQ-ARCH-04, REQ-ARCH-08, REQ-ARCH-09, REQ-ARCH-16,
REQ-ARCH-19, REQ-UX-06.

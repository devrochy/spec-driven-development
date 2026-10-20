# SPEC-01 · Diseño

## Topología objetivo (recomendación P-01 A)

```
                 Cloudflare (DNS, TLS, Access, WAF)
                        │ túneles
        ┌───────────────┴────────────────┐
  Nodo prod-app                    Nodo prod-data
  Coolify: solvershub-core (API,   Postgres 17 + PostGIS + pgvector
  worker, beat), panel, landing    Redis
        │                                │
        └──── red privada ───────────────┘
                        │
             Almacenamiento S3 compatible fuera del sitio
             (WAL continuo + base backups + TENANTS_ROOT)
```

- `test` sigue en la máquina de desarrollo; **producción nunca**.
- Dominios: `app.<dominio>` (panel), `api.<dominio>` (backend y webhooks), `<dominio>` (landing). El
  dominio final lo decide HU-GTM-01.
- Las rutas `/webhooks/*` y `/healthz` quedan fuera de Access; `/api/v1` no es público (el panel lo
  llama por red privada).

## Backups

| Qué | Cómo | Retención |
|---|---|---|
| Postgres | pgBackRest o wal-g: WAL continuo + base backup diario | 30 días de PITR, 12 mensuales |
| `TENANTS_ROOT` (catálogos, playbooks, evidencias) | Sincronización diaria versionada al mismo almacenamiento | 30 días |
| Configuración | `solvershub-infra` en git | Historia completa |

El simulacro se repite cada trimestre y su resultado queda en `solvershub-comercial/runbooks/evidencia/`.

## Consumer y DLQ

- Nombre de consumidor por réplica (`orchestrator-<hostname>-<pid>`).
- Al arrancar y cada minuto: `XAUTOCLAIM` de entradas pendientes con más de N segundos.
- El contador de entregas sale de `XPENDING`; al llegar a 3 la entrada pasa a `agent_core:inbound:dlq`
  con el error y se hace `XACK`.
- La DLQ se ve y se reintenta desde el panel (la vista ya existe).

## Webhook fail-closed

- En producción, una conexión de Meta sin `app_secret` resoluble **rechaza** el mensaje con 401 y
  registra una alerta. En test se permite con una variable explícita.
- Las altas manuales de conexión exigen `app_secret`.
- El secreto por conexión (BYOK y Embedded Signup en el mismo negocio) llega con [HU-CONN-05](../SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-05-webhook-por-conexion.md).

## Acceso

- Bloqueo progresivo por identificador e IP (5 intentos → 15 min) en `/api/v1/auth/login` y en la API
  de campo, con auditoría.
- El BFF del panel verifica `Origin`/`Sec-Fetch-Site` en los métodos que cambian estado.
- Cabeceras: HSTS, CSP, `X-Frame-Options`, `Referrer-Policy` en panel y landing.
- Rotar la credencial del master y, si estaba en el historial de `solvershub-comercial`, limpiarlo.

## Observabilidad

| Señal | Fuente | Alerta |
|---|---|---|
| Errores | Sentry (backend y panel) | Nuevo error en producción |
| p95/p99 del webhook | Trazas OTLP | p99 > 1 s durante 5 min |
| Lag de la cola y tamaño de la DLQ | Métrica propia | DLQ > 0 |
| `/healthz` profundo | Postgres, Redis, Celery beat | Caído 2 min |
| Costo de LLM por hora | `usage_ledger` | Pico anómalo (riesgo R-09) |

## Release y E2E

Imagen con etiqueta del commit → despliegue en test → smoke E2E con Playwright contra el backend
real (login, probar asistente con sandbox, lista de conexiones, pedido de prueba) → aprobación manual
→ promoción de la **misma imagen** a producción.

## ADR

- No hace falta ADR nuevo: se cumple ADR-0010 (producción en VPS) y la invariante 9.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Migrar datos de la producción actual (en dev) a la nueva | Ventana de mantenimiento corta con dump + restore verificado |
| Costo de la infraestructura | Supuesto S-03 (USD ~250/mes de infra) en el modelo de precios |

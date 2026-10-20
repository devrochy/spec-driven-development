# 09 · Línea base (bloque E, Semana 0)

Registro de la línea base tomada el **2026-10-03** antes de tocar producción. Es
la referencia contra la que se mide el Hito 0A (golden sets, consumo, respaldo).

> Fuente: máquina de desarrollo (hoy producción corre ahí — invariante 9 pendiente
> de [HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)).
> BD `agent_core` local (puerto 5433).

## 1. Dump de seguridad

| Elemento | Valor |
|---|---|
| Archivo | `~/backups/solvershub/dump-20261003-1203.sql` |
| Tamaño | 3,1 MB |
| Formato | `pg_dump` plano (`--no-owner --no-privileges`) |
| Tablas | `CREATE TABLE` presentes |
| Guardado fuera de la máquina | ⏳ **pendiente** (hoy en el mismo equipo; subir a almacenamiento externo) |

Este dump es la red de seguridad hasta [HU-ARCH-03](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md) (PITR).

## 2. Golden sets (referencia)

| Set | Resultado | Escenarios | Ref git |
|---|---|---|---|
| Framework | **34/35** | 35 | `67946df` |
| Tenant `solvershub` | **7/8** | 8 | `67946df` |

Detalle de los fallos (flaky del LLM, revisar antes de exigir ≥95 %):

- Framework: 1 fallo variable (alucinación de tema ajeno / no llamó una tool).
- Tenant `solvershub`: 1 fallo en 8.

**Umbral del 0A: ≥95 % durante 3 noches** — hoy no se cumple; entra con las HU de
evals (ARCH-16/17, SH-08).

## 3. Consumo (`usage_ledger`)

| Métrica | Valor (2026-09-29 → 2026-10-02) |
|---|---|
| Turnos registrados | 140 |
| Tokens entrada (prom.) | 807 |
| Tokens salida (prom.) | 25 |
| Tokens caché (prom.) | 482 |
| Costo total | (cifra interna) |
| Latencia (prom.) | 345 ms |

Por modelo:

| Modelo | Turnos | Costo USD |
|---|---:|---:|
| fake / fake-model / fake-tool | 108 | 0,13 |
| `deepseek-flash` | 20 | 0,0047 |
| `deepseek-chat` (discontinuado) | 12 | 0,0166 |
| `m` (prueba) | 12 | 6,54 |

> El "costo" está dominado por datos de prueba/fake; el costo real de `deepseek-flash`
> es marginal ((cifra interna)). La calibración fina es HU-BILL-01.

## 4. Datos operativos

| Tabla | Filas |
|---|---:|
| `tenants` | 705 |
| `pack_commerce_orders` | 38 |
| `usage_ledger` | 140 |

## 5. N-27 · Credencial del master en el historial de `solvershub-comercial`

**Confirmado.** En `PLAN-DE-PRUEBAS.md` hay tres credenciales sucesivas del admin
master en la historia git (la vigente y dos anteriores, ya rotadas). El repo es
**privado**, lo que reduce el riesgo pero no lo elimina.

**Acciones** ([HU-ARCH-04](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md)):
- Rotar la credencial del master (y no volver a versionarla).
- Sacar las contraseñas reales de `PLAN-DE-PRUEBAS.md` (usar un placeholder).
- Verificar el valor vigente en producción.

## Pendientes de la línea base

- [ ] Subir el dump a almacenamiento **fuera de la máquina**.
- [ ] Rotar la credencial del master y limpiar `PLAN-DE-PRUEBAS.md` (N-27).
- [ ] Golden sets del framework y `solvershub` como línea base reproducible (agente `eval-runner`).
- [ ] Medir **una semana** de `usage_ledger` con tráfico real (hoy hay datos de prueba).

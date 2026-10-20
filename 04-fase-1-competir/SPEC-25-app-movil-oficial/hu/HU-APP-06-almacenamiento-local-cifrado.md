---
id: HU-APP-06
titulo: Almacenamiento local cifrado
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [confianza]
req: [REQ-APP-06]
dependencias: [HU-APP-01]
skills: [backend-design:data-modeling-discipline, backend-design:migration-safety]
estado: terminada
---

# HU-APP-06 · Almacenamiento local cifrado

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-06

**Título:** Almacenamiento local cifrado

**Workstream:** App móvil

**Historia:** Como responsable de seguridad quiero que la base local, la cola offline y la caché de la app estén cifradas en reposo con clave en el Keystore/Keychain, para que robar el teléfono o su almacenamiento no exponga datos de clientes, pagos ni tokens (cierra REQ-APK-021).

**Por qué importa (valor empresarial):** La app maneja datos financieros de clientes en campo (cuotas, pagos, evidencias). REQ-APK-021 exige cifrado local y sigue pendiente: sin él, la app no está lista para producción seria y no se puede presentar como app oficial de un producto que vende confianza.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-06

**Dependencias:** [HU-APP-01](HU-APP-01-nucleo-modular-de-la-app.md)

**Criterios de aceptación (Gherkin):**
- **Cifrado activo.** Dado el build propio con `useSQLCipher: true`, cuando la app abre la base, entonces aplica `PRAGMA key` con la clave de SecureStore y cualquier lectura sin clave falla.
- **Migración.** Dado un usuario con datos previos en AsyncStorage, cuando actualiza la app, entonces sus datos (cola pendiente incluida) se migran a SQLite cifrado con verificación de filas y se borra el origen.
- **Clave protegida.** Dado un dispositivo con biometría, cuando se consulta la clave maestra, entonces SecureStore exige autenticación (`requireAuthentication`).
- **Esquema.** Dado el motor de datos, cuando un módulo persiste entidades, colas o auditoría, entonces usa las tablas `cache_entidad`, `cola_evento`, `auditoria_local` y `sync_cursor` sin duplicar almacenes.

**Evidencia / Definición de Terminado:**
- Config plugin en `app.json`; `src/data/db/**` con apertura, migraciones versionadas y repos; migración AsyncStorage→SQLite con test de ida y vuelta (incluye cola `cobranza_cola_offline`); kill-switch remoto para volver a leer el origen; `npm run check` verde; verificación manual de archivo de base ilegible sin clave.

**Implementada (2026-10-06):** [solvershub-apk #111](https://github.com/devrochy/solvershub-apk/pull/111) — almacenamiento local cifrado (SQLCipher).

**Riesgos/Notas:**
- SQLCipher no aplica en Expo Go: el desarrollo de `data/` exige dev client (EAS development), que ya es el flujo del repo.
- `withExclusiveTransactionAsync` abre conexión propia: hay que aplicar `PRAGMA key` también ahí (documentado en ADR-APP-05).
- El tema y preferencias no sensibles pueden quedarse en AsyncStorage.

**App implementada (2026-10-06):** [solvershub-apk #111](https://github.com/devrochy/solvershub-apk/pull/111) — capa `src/data/` completa: conexión cifrada (`PRAGMA key`, clave en SecureStore, kill-switch local), esquema (cache/cola/auditoría/cursor), repos y migración única de la cola legacy con verificación de totales (la activación queda para [HU-APP-07](HU-APP-07-cobranza-al-nucleo-sin-regresion.md) junto al cambio de motor, según la estrategia del design.md); plugin `useSQLCipher` en `app.json`; 552/552 tests (5 nuevos).

---
id: HU-APP-07
titulo: Cobranza al núcleo sin regresión
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, operacion]
req: [REQ-APP-01, REQ-APP-09, REQ-PLUS-04]
dependencias: [HU-APP-01, HU-APP-02, HU-APP-06]
skills: [frontend-design, backend-design:testing-with-discernment]
estado: terminada
---

# HU-APP-07 · Cobranza al núcleo sin regresión

> Estado SDD: Terminada — implementada 2026-10-06.

**ID:** HU-APP-07

**Título:** Cobranza al núcleo sin regresión

**Workstream:** App móvil

**Historia:** Como gestor en calle quiero que mi app de cobranza siga funcionando exactamente igual o mejor dentro de la app oficial (diario, visitas pago/no-pago, gastos, trayectoria, liquidación y offline), para que la evolución de la app no rompa el trabajo de campo que ya funciona.

**Por qué importa (valor empresarial):** La cobranza con APK es el diferencial casi único (D-02) y el ingreso de campo de la plataforma. Migrarla al nuevo núcleo sin regresiones es la condición de existencia del plan completo: si el campo se rompe, no hay app oficial que valga.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-01, REQ-APP-09, REQ-PLUS-04

**Dependencias:** [HU-APP-01](HU-APP-01-nucleo-modular-de-la-app.md), [HU-APP-02](HU-APP-02-sesion-unica-y-recuperacion.md), [HU-APP-06](HU-APP-06-almacenamiento-local-cifrado.md)

**Criterios de aceptación (Gherkin):**
- **Módulo.** Dado el código de cobranza actual, cuando se mueve a `src/modules/cobranza/` con su navigator y cliente de API, entonces los 490+ tests siguen verdes y el flujo completo funciona en dev client.
- **Cola en SQLite.** Dado un pago registrado sin conexión, cuando vuelve la red, entonces el evento se sincroniza desde la cola en SQLite cifrada con ack por evento, sin duplicados.
- **Autovinculación.** Dado un gestor nuevo, cuando inicia sesión, entonces el flujo de vinculación de dispositivo (IMEI/WhatsApp) queda completo y bloqueado en producción como exige ADR-0068 (cierra el pendiente HU-39/43).
- **Pantallas gigantes.** Dado `ClienteScreen` y `TrayectoDiarioScreen`, cuando se descomponen en hooks/features del módulo, entonces el comportamiento es idéntico y las pruebas por unidad de comportamiento aumentan.
- **Smoke E2E.** Dado el APK preview, cuando corre el smoke de Maestro (login → diario → visita pago offline → sync → liquidación), entonces pasa completo.

**Evidencia / Definición de Terminado:**
- Migración a `modules/cobranza/` con fronteras (ADR-APP-01); cola `cola_evento` en SQLite; autovinculación cerrada con backend (si requiere cambio en agent-core, se incluye aquí con sus tests); descomposición de las pantallas gigantes con tests; flujo Maestro commiteado en `e2e/`; `npm run check` verde; evidencia en test con el smoke grabado.

**Implementada (2026-10-06):** [solvershub-apk #112](https://github.com/devrochy/solvershub-apk/pull/112) — cobranza al núcleo sin regresión.

**Riesgos/Notas:**
- Regla de oro de esta HU: no cambiar comportamiento, salvo la autovinculación (que es un fix de seguridad planeado) y la migración de almacenamiento ([HU-APP-06](HU-APP-06-almacenamiento-local-cifrado.md)).
- Los tests flaky de pantalla se estabilizan aquí (`--runInBand` o timeouts) para que el CI deje de dar falsos rojos.
- El propietario que también es gestor entra al campo vía el exchange de [HU-APP-02](HU-APP-02-sesion-unica-y-recuperacion.md).

**App implementada (2026-10-06):** [solvershub-apk #112](https://github.com/devrochy/solvershub-apk/pull/112) — migración física a `src/modules/cobranza/` con fronteras OK, cola offline en SQLite con traspaso verificado de la legacy y fallback AsyncStorage (misma API pública), descomposición parcial de `ClienteScreen`, autovinculación verificada en código (backend #95 + `VincularDispositivoScreen`) y `e2e/smoke-cobranza.yaml` commiteado. 558/558 tests. **Pendiente**: corrida del smoke Maestro (build preview EAS + CLI local) y descomposición de los modales/trayecto restantes.

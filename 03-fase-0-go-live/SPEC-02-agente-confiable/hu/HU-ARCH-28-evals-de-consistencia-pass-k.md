---
id: HU-ARCH-28
titulo: "Evals de consistencia: usuario simulado, aserciones de estado y pass^k"
spec: SPEC-02
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: L
impacto: [calidad_ia, confianza]
req: [REQ-ARCH-20]
dependencias: [HU-SUB-12]
skills: ["eval-author", "eval-runner", "backend-design:testing-with-discernment", "db-migration"]
ola: 4
estado: en-curso
---

# HU-ARCH-28 · Evals de consistencia: usuario simulado, aserciones de estado y pass^k

> Estado SDD: En curso. Implementada y mergeada ([core #323](https://github.com/devrochy/agent-core/pull/323), ADR-0119 aceptado); falta desplegarla en test (migración `0058`) y medir pass^4 tres noches.

**ID:** HU-ARCH-28

**Título:** Evals de consistencia: usuario simulado, aserciones de estado y pass^k

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de SolversHub quiero que cada noche el mismo escenario de conversación se corra varias veces con un cliente simulado y se compruebe el estado final en la base, para saber si el asistente es consistente y no solo si acertó una vez.

**Por qué importa (valor empresarial):** El umbral del 0A (≥95 % tres noches) mide un intento por escenario. τ-bench (Sierra, 2024) muestra que la consistencia cae mucho cuando el mismo caso se repite k veces: un error que aparece 1 de cada 4 veces llega a clientes reales todos los días. pass^k lo hace visible antes que el cliente y deja de depender de relanzar el gate a ciegas.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** L

**REQ mapeados:** REQ-ARCH-20

**Dependencias:** HU-SUB-12

**Criterios de aceptación (Gherkin):**
- **Usuario simulado.** Dado un escenario con objetivo, datos y estilo del cliente y una semilla, cuando el runner lo corre contra el loop real con acciones sin efectos, entonces la conversación termina por objetivo cumplido, relevo humano o tope de turnos, y queda guardada con su traza.
- **Aserciones de estado.** Dado un escenario con aserciones sobre la base (por ejemplo, pedido con la variante Premium y el total del servidor, sin cargos duplicados), cuando termina, entonces cada aserción se evalúa y se guarda con esperado y real en `eval_results.state_assertions`.
- **pass^k.** Dado k = 4, cuando corre el nightly, entonces cada escenario se ejecuta 4 veces y se guardan pass@1 y pass^4 por escenario y en total en `eval_runs`.
- **Inestabilidad atribuida.** Dado un escenario que pasa en algunos intentos y falla en otros, cuando se publica el reporte, entonces queda marcado "inestable" con los intentos fallidos y lo que cambió entre ellos.
- **Umbral del 0A intacto.** Dado el gate vigente (≥95 % durante tres noches), cuando se agrega pass^k, entonces el gate sigue igual y pass^4 se reporta junto a él.

**Evidencia / Definición de Terminado:**
- Runner extendido sobre el de journeys (HU-SUB-12): simulador con semilla, k intentos, aserciones de estado y atribución de inestabilidad.
- Migración aditiva en `eval_runs` y `eval_results` (k, pass_1, pass_k, simulator, state_assertions, verifier) con RLS intacta y `downgrade` probado.
- Escenarios del framework y de `solvershub` migrados al formato nuevo; reporte nocturno con pass@1 y pass^4.
- ADR-0119 (fiabilidad medida) aceptado; las corridas usan una base efímera (CI y stack local), así que su consumo no llega al ledger de ningún negocio real.

**Riesgos/Notas:**
- Un simulador poco realista da pass^k alto con producción mala: escenarios nacidos de conversaciones reales y varios estilos de cliente.
- Costo del nightly: modelo por defecto y k = 4 (k = 8 solo antes de una release).

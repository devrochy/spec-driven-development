---
id: HU-ARCH-01
titulo: Producción fuera de la máquina de desarrollo, con panel y landing
spec: SPEC-01
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: L
impacto: [confianza, operacion]
req: [REQ-ARCH-01, REQ-ARCH-02]
dependencias: [HU-GTM-01]
skills: ["backend-design:boring-by-default", "backend-design:boring-tech-advisor", "cloudflare-one", "deep-research", "desplegar-test-agent-core"]
ola: 2
estado: en-curso
---

# HU-ARCH-01 · Producción fuera de la máquina de desarrollo, con panel y landing

> Estado SDD: En curso. Preparación mergeada el 2026-10-09 ([core #346](https://github.com/devrochy/agent-core/pull/346)): runbook, inventario de variables y scripts de verificación. Falta que el dueño contrate el VPS y ejecutar el runbook.

**ID:** HU-ARCH-01

**Título:** Producción fuera de la máquina de desarrollo, con panel y landing

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de SolversHub quiero que producción (motor, worker, beat, panel y landing) corra en servidores propios separados de la máquina de desarrollo para que un corte, un reinicio o un experimento local no afecte a ningún cliente de pago.

**Por qué importa (valor empresarial):** Es la condición mínima para cobrar: la invariante 9 lo exige y ningún cliente acepta que su atención dependa de un portátil. Además habilita publicar el panel nuevo, que hoy no existe en producción y sin el cual el retiro del panel clásico no puede terminar.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** L

**REQ mapeados:** REQ-ARCH-01, REQ-ARCH-02

**Dependencias:** HU-GTM-01

**Criterios de aceptación (Gherkin):**
- **Separación real.** Dado el entorno de producción nuevo, cuando se apaga la máquina de desarrollo, entonces el panel, la API, los webhooks, el worker y el beat de producción siguen respondiendo.
- **Panel y landing en producción.** Dado el dominio final, cuando un usuario abre `app.<dominio>` y `<dominio>`, entonces carga la versión de `main` de `solvershub-panel` y `solvershub-landing` con TLS válido.
- **API privada.** Dado `/api/v1`, cuando se llama desde internet sin pasar por el panel, entonces no responde; solo `/webhooks/*` y `/healthz` son públicos.
- **Migración de datos.** Dado los negocios que hoy están en la "producción" de la máquina de desarrollo, cuando se migran, entonces el conteo de filas por tabla coincide y el asistente responde en cada uno.
- **Recursos y secretos.** Dado el entorno nuevo, cuando se revisa, entonces no comparte credenciales ni base con test.
- **Aislamiento verificable.** Dado la BD nueva de producción migrada desde cero, cuando corre el check `rls_forced`, entonces no hay ninguna tabla con RLS sin FORCE (incluye N-36) y el runtime se conecta con `app_runtime`, nunca con el dueño.

**Evidencia / Definición de Terminado:**
- Topología documentada en `solvershub-infra` (o en `solvershub-core/docs/despliegue-coolify.md` si [HU-REP-06](../../SPEC-00-reestructuracion/hu/HU-REP-06-solvershub-infra.md) no terminó).
- Prueba de apagado de la máquina de desarrollo con capturas y hora.
- `despliegue-coolify.md` actualizado: sin la frase "misma máquina de desarrollo".
- Las skills `desplegar-test-agent-core` y `release` y la lista `PROD_RESOURCES` del hook `guards.py` apuntan a los UUID nuevos (N-37).

**Riesgos/Notas:**
- Decisión P-01 pendiente (VPS dedicado recomendado).
- Las variables `AGENT_CORE_API_URL` del panel y `NEXT_PUBLIC_PANEL_URL` de la landing apuntan a los dominios nuevos.

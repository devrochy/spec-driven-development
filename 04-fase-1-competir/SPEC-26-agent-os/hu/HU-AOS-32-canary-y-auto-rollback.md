---
id: HU-AOS-32
titulo: "Canary sticky con no-inferioridad y auto-rollback"
spec: SPEC-26
fase: 1
hito: "1"
workstream: Agent OS
prioridad: P1
critico: false
estimacion: M
impacto: [confianza]
req: [REQ-AOS-10]
dependencias: [HU-AOS-27, HU-AOS-29]
skills: ["release", "data:statistical-analysis", "backend-design:observability-by-default"]
estado: borrador
---

# HU-AOS-32 · Canary sticky con no-inferioridad y auto-rollback

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-26](../spec.md).

**ID:** HU-AOS-32

**Título:** Canary sticky con no-inferioridad y auto-rollback

**Workstream:** Agent OS

**Historia:** Como dueño quiero publicar a una parte de las conversaciones nuevas y que el sistema vuelva atrás solo si la versión empeora, para probar en real con el riesgo acotado.

**Por qué importa (valor empresarial):** Reemplaza en parte ADR-0016: el kernel elige la release, así que un porcentaje real ya es posible.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-AOS-10

**Dependencias:** [HU-AOS-27](HU-AOS-27-versiones-en-el-panel.md), [HU-AOS-29](HU-AOS-29-tablero-de-fiabilidad.md)

**Criterios de aceptación (Gherkin):**
- **Porcentaje sticky.** Dado una publicación al 10 %, cuando empiezan episodios nuevos, entonces cerca del 10 % de las conversaciones usa la candidata (`hash(canary_release_id ‖ conversation_id) % 100`) y la mantiene durante el episodio; con otro canary, el reparto cambia.
- **No-inferioridad.** Dado la muestra mínima (72 h o 200 conversaciones), cuando la completitud cae más de 2 pp o el escalamiento sube más de 2 pp, entonces se vuelve atrás sola y avisa.
- **Sin muestra no hay veredicto.** Dado un canary sin la muestra mínima, cuando se evalúa, entonces no hay promoción ni rollback automáticos por métricas; y si en 7 días no la junta, entonces el dueño puede promover a mano con el gate aprobado.
- **Señal dura.** Dado una candidata con un error a propósito (errores de acción o fallos del verificador por encima del umbral), cuando corre el canary, entonces el auto-rollback se dispara de inmediato, sin esperar la muestra.

**Evidencia / Definición de Terminado:**
- Carril de release en el kernel; job de evaluación; alertas; tests.

**Riesgos/Notas:**
- Poco tráfico alarga la ventana: se usa el mínimo de conversaciones, no solo horas; con poco tráfico, la promoción es manual (ADR-0117 §5).
- Las candidatas de plataforma (`origin = platform`) usan el mismo canary.

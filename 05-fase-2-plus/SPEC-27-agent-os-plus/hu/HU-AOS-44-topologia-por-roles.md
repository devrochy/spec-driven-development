---
id: HU-AOS-44
titulo: "Topología por roles y escalado del runtime"
spec: SPEC-27
fase: 2
hito: "2"
workstream: Agent OS
prioridad: P2
critico: false
estimacion: M
impacto: [operacion]
req: [REQ-AOS-16]
dependencias: [HU-AOS-29]
skills: ["backend-design:performance-and-scaling", "release"]
estado: borrador
---

# HU-AOS-44 · Topología por roles y escalado del runtime

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-27](../spec.md).

**ID:** HU-AOS-44

**Título:** Topología por roles y escalado del runtime

**Workstream:** Agent OS

**Historia:** Como operador quiero separar el panel del gateway+consumer (partición de ADR-0021) cuando las métricas lo pidan, para escalar sin microservicios.

**Por qué importa (valor empresarial):** Escala con evidencia, sin la complejidad de microservicios (ADR-0021).

**Prioridad:** P2 plus

**Estimación:** M

**REQ mapeados:** REQ-AOS-16

**Dependencias:** [HU-AOS-29](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-29-tablero-de-fiabilidad.md)

**Criterios de aceptación (Gherkin):**
- **Disparador.** Dado que el panel degrada el p99 del webhook sobre el umbral operativo (SUPUESTO A VALIDAR: 1 s durante 15 minutos), cuando se revisa el tablero, entonces se recomienda separar por rol (ADR-0021).
- **Mismo binario.** Dado la separación, cuando se despliega, entonces cada contenedor usa la misma imagen con `AGENT_CORE_ROLE` distinto.
- **Resultado.** Dado la separación aplicada, cuando se mide una semana, entonces el p99 del webhook vuelve bajo el umbral.

**Evidencia / Definición de Terminado:**
- Roles en `core/main.py` y en el despliegue de Coolify; runbook; medición.

**Riesgos/Notas:**
- Separar sin necesidad agrega operación: solo con el disparador.

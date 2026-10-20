---
id: HU-DS-05
titulo: Paleta de comandos y atajos
spec: SPEC-29
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [diferenciacion, operacion]
req: [REQ-UX-10]
dependencias: [HU-DS-04]
skills: ["frontend-design", "panel-ui"]
estado: en-curso
---

# HU-DS-05 · Paleta de comandos y atajos

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32).

**ID:** HU-DS-05

**Título:** Paleta de comandos y atajos

**Workstream:** UX/Onboarding

**Historia:** Como usuario frecuente del panel quiero abrir con Ctrl/⌘ K un buscador que me lleve a cualquier sección, acción o registro que pueda ver para no recorrer el menú.

**Por qué importa (valor empresarial):** Es el atajo que hace sentir el panel como una herramienta profesional (Linear, Stripe, Vercel). Al operador le ahorra minutos al día y al dueño le resuelve el "no encuentro X" sin soporte.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-10

**Dependencias:** [HU-DS-04](HU-DS-04-shell-adaptativo-del-panel.md)

**Criterios de aceptación (Gherkin):**
- **Ir a una sección.** Dado cualquier página, cuando pulso Ctrl+K y escribo "prom", entonces veo "Cobranza › Promesas" si tengo permiso y llego con Enter.
- **Sin permiso no aparece.** Dado un colaborador sin permiso de cobranza, cuando busca "prom", entonces no aparece ninguna sección de cobranza.
- **Registros.** Dado que escribo el nombre de un cliente, cuando pasan 250 ms, entonces la paleta muestra resultados de `GET /search` agrupados por sección.
- **Acciones rápidas.** Dado que tengo permiso de escritura, cuando escribo "pausar", entonces veo "Pausar asistente", que pide confirmación con su consecuencia.
- **Teclado y lector.** Dado la paleta abierta, cuando uso flechas, Enter y Escape, entonces funciona sin ratón, el resultado activo se anuncia y el foco vuelve a donde estaba al cerrar.
- **Atajos de una tecla apagables.** Dado que apago los atajos de una tecla en Configuración, cuando pulso `g` y luego `i`, entonces no pasa nada, pero Ctrl+K sigue funcionando.

**Evidencia / Definición de Terminado:**
- Tests de permisos sobre el índice de la paleta.
- Grabación corta del flujo con teclado.
- Medición de JS: `cmdk` se carga solo al abrir la paleta.

**Riesgos/Notas:**
- El índice de secciones sale de `nav.ts` + permisos de `/admin/me`; la búsqueda de registros reusa ADR-0096.
- La ayuda de atajos (`?`) se integra con la ayuda contextual de [HU-UX-03](../../SPEC-12-arquitectura-de-informacion/hu/HU-UX-03-ayuda-contextual.md).

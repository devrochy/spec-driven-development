---
id: HU-AOS-40
titulo: "Sandbox aislado para acciones no confiables"
spec: SPEC-27
fase: 2
hito: "2"
workstream: Agent OS
prioridad: P2
critico: false
estimacion: L
impacto: [confianza, diferenciacion]
req: [REQ-AOS-15]
dependencias: [HU-AOS-34, HU-ARCH-19]
skills: ["backend-design:security-discipline", "backend-design:boring-by-default"]
estado: borrador
---

# HU-AOS-40 · Sandbox aislado para acciones no confiables

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-27](../spec.md).

**ID:** HU-AOS-40

**Título:** Sandbox aislado para acciones no confiables

**Workstream:** Agent OS

**Historia:** Como plataforma quiero ejecutar acciones no confiables en un entorno aislado con red restringida y límites, para abrir integraciones sin riesgo.

**Por qué importa (valor empresarial):** Habilita integraciones de terceros (nivel T4) sin exponer a los demás negocios.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-AOS-15

**Dependencias:** [HU-AOS-34](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-34-acciones-v2.md), [HU-ARCH-19](../../../04-fase-1-competir/SPEC-19-extensibilidad-y-operacion/hu/HU-ARCH-19-mcp-por-tenant.md)

**Criterios de aceptación (Gherkin):**
- **Red restringida.** Dado una acción en sandbox, cuando intenta llamar a un dominio fuera de su allowlist, entonces se bloquea.
- **Límites.** Dado una acción que excede CPU, memoria o tiempo, cuando corre, entonces se corta y se usa su respaldo.
- **Sin secretos ajenos.** Dado una acción de un negocio, cuando corre, entonces solo recibe los secretos que declara su manifiesto.

**Evidencia / Definición de Terminado:**
- Ejecución aislada (contenedor efímero o microVM); egress por allowlist; tests de escape.

**Riesgos/Notas:**
- Costo de operar el aislamiento: solo para acciones que lo necesitan.

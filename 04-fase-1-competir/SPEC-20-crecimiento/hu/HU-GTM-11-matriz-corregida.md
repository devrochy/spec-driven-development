---
id: HU-GTM-11
titulo: Matriz competitiva corregida y mantenida
spec: SPEC-20
fase: 1
hito: "1"
workstream: GTM
prioridad: P1
critico: false
estimacion: S
impacto: [diferenciacion]
req: [REQ-GTM-10]
dependencias: []
skills: ["xlsx", "marketing:competitive-brief", "deep-research"]
estado: terminada
---

# HU-GTM-11 · Matriz competitiva corregida y mantenida

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-20](../spec.md).

**ID:** HU-GTM-11

**Título:** Matriz competitiva corregida y mantenida

**Workstream:** GTM

**Historia:** Como responsable de producto quiero una matriz sin la columna de ejemplo, con Wolkvox y con la columna de SolversHub honesta para tomar decisiones sobre datos verificables.

**Por qué importa (valor empresarial):** Decisiones de producto y de precio tomadas sobre una matriz con errores (ChatBotCorp contado como competidor, promesas propias exageradas) llevan a invertir mal.

**Prioridad:** P1 competir

**Estimación:** S

**REQ mapeados:** REQ-GTM-10

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Limpieza.** Dado la hoja `Matriz Comparativa`, cuando se corrige, entonces ChatBotCorp ya no está y Wolkvox tiene su columna con los 18 ejes.
- **Honestidad.** Dado la columna SolversHub, cuando se lee, entonces refleja el estado real (canales, integraciones, calidad, legal).
- **Mantenimiento.** Dado un trimestre, cuando pasa, entonces la matriz se revisa y se fecha.

**Evidencia / Definición de Terminado:**
- Archivo actualizado en `solvershub-comercial`.

**Implementada (2026-10-03):** matriz corregida en `solvershub-comercial/estudio_mercado_agentes_ia.xlsx`: sin ChatBotCorp, con Wolkvox (18 ejes) y la columna de SolversHub honesta; fecha de revisión anotada. PR [comercial #8](https://github.com/devrochy/solvershub-comercial/pull/8).

**Riesgos/Notas:**
- Ver matriz-competitiva.md.

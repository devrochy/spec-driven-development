---
id: HU-REP-07
titulo: Repo solvershub-brand con tokens publicados
spec: SPEC-19
fase: 1
hito: "1"
workstream: Arquitectura/Prod
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, diferenciacion]
req: [REQ-REP-01]
dependencias: [HU-REP-02]
skills: ["frontend-design", "figma-generate-library", "theme-factory"]
estado: borrador
---

# HU-REP-07 · Repo `solvershub-brand` con tokens publicados

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-19](../spec.md).

**ID:** HU-REP-07

**Título:** Repo solvershub-brand con tokens publicados

**Workstream:** Arquitectura/Prod

**Historia:** Como responsable de marca quiero que el manual, los logos y los tokens vivan en su propio repo y se publiquen como paquete para que panel, APK y landing usen siempre la misma versión de la marca.

**Por qué importa (valor empresarial):** Hoy la APK toma los tokens del repo del panel por ruta relativa y la landing los copia a mano: la marca se desalinea. Un paquete versionado da consistencia profesional en todos los productos.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-REP-01

**Dependencias:** [HU-REP-02](../../../03-fase-0-go-live/SPEC-00-reestructuracion/hu/HU-REP-02-renombre-cosmetico.md)

**Criterios de aceptación (Gherkin):**
- **Repo.** Dado `solvershub-panel/brand/`, cuando se mueve, entonces `solvershub-brand` tiene historia, manual y assets.
- **Paquete.** Dado `@solvershub/tokens`, cuando se publica una versión, entonces panel, APK y landing la instalan y su CI verifica la versión.

**Evidencia / Definición de Terminado:**
- Repo y paquete publicados; `sync-tokens.mjs` de la APK reemplazado.

**Riesgos/Notas:**
- Los binarios grandes de propuestas pueden ir a almacenamiento externo.

---
id: HU-UI-03
titulo: Shell del panel responsive y accesible
spec: SPEC-10
fase: 0
hito: 0B
workstream: UX/Onboarding
prioridad: P0
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-UX-06]
dependencias: [HU-UI-02]
skills: ["frontend-design", "web-perf", "built-in-browser", "panel-ui"]
estado: terminada
---

# HU-UI-03 · Shell del panel responsive y accesible

> Estado SDD: Terminada — implementada 2026-10-11.

**ID:** HU-UI-03

**Título:** Shell del panel responsive y accesible

**Workstream:** UX/Onboarding

**Historia:** Como dueño de un negocio quiero usar el panel desde el celular, ver que algo está cargando, recuperarme de un error y saber si mi asistente está activo para atender mi negocio desde cualquier lugar.

**Por qué importa (valor empresarial):** Los dueños de pymes viven en el celular: hoy el panel no se adapta en absoluto. Sin estados de carga y error, cada navegación lenta parece una falla. Es la base de calidad que exigen los clientes enterprise (WCAG AA).

**Prioridad:** P0 go-live (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-UX-06

**Dependencias:** [HU-UI-02](HU-UI-02-kit-de-feedback.md)

**Criterios de aceptación (Gherkin):**
- **Móvil.** Dado una pantalla de 375 px, cuando abro el panel, entonces el menú es un cajón y ninguna página tiene scroll horizontal.
- **Carga.** Dado una página con varias consultas, cuando navego, entonces veo esqueletos en lugar de una pantalla quieta.
- **Error.** Dado una falla del backend, cuando una página no carga, entonces veo un error en español con "Reintentar".
- **404.** Dado una ruta inexistente, cuando entro, entonces veo una página en español con enlace al inicio.
- **Accesibilidad.** Dado la navegación por teclado, cuando entro al panel, entonces hay skip link, las pestañas y el selector de negocio funcionan con flechas y Escape y las tablas indican el orden.
- **Estado del asistente.** Dado el asistente pausado, cuando miro la barra superior, entonces lo veo y puedo reactivarlo.

**Evidencia / Definición de Terminado:**
- Capturas en móvil y escritorio; reporte de axe sin errores críticos.

**Riesgos/Notas:**
- Respeta `DESIGN.md` (sin animaciones largas, esqueletos y no spinners).

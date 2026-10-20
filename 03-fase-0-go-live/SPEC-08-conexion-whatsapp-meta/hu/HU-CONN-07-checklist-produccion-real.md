---
id: HU-CONN-07
titulo: Checklist de producción real
spec: SPEC-08
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, operacion]
req: [REQ-CONN-03]
dependencias: [HU-CONN-01]
skills: ["backend-design:observability-by-default", "backend-design:performance-and-scaling", "meta-whatsapp"]
ola: 3
estado: borrador
---

# HU-CONN-07 · Checklist de producción real

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-08](../spec.md).

**ID:** HU-CONN-07

**Título:** Checklist de producción real

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero un checklist de producción que evalúe mi conexión y me diga qué falta, y como master quiero los chequeos de la plataforma en mi sección, para que el paso a producción sea verificable.

**Por qué importa (valor empresarial):** Hoy el checklist siempre sale en rojo (exige suscripciones de page e Instagram y corre pytest dentro de la imagen) y puede bloquear el servidor 3 minutos. Un checklist que nunca pasa enseña a ignorarlo.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-CONN-03

**Dependencias:** [HU-CONN-01](HU-CONN-01-credenciales-por-conexion.md)

**Criterios de aceptación (Gherkin):**
- **Por conexión.** Dado el hub de una conexión, cuando abro "Producción", entonces veo los chequeos de esa conexión (número registrado, WABA suscrita, webhook, plantillas mínimas aprobadas, token) evaluados con sus credenciales.
- **Solo lo necesario.** Dado una conexión de WhatsApp, cuando se evalúa, entonces `page` e `instagram` no son obligatorios.
- **Plataforma aparte.** Dado el master, cuando abre "Plataforma → App de Meta", entonces ve los chequeos de la app de la plataforma y de infraestructura, ejecutados como job en segundo plano sin pytest.
- **Sin bloqueo.** Dado una corrida del checklist, cuando se ejecuta, entonces no bloquea el event loop y su resultado queda guardado con fecha.

**Evidencia / Definición de Terminado:**
- Corrección de `meta_production_readiness.py:83-90,222-237`; job de Celery; tests.

**Riesgos/Notas:**
- Requisitos y Producción dejan de ser la misma página con los mismos 10 pasos.

---
id: HU-ARCH-02
titulo: Borde TLS y webhook de Meta de producción verificados
spec: SPEC-01
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: S
impacto: [confianza]
req: [REQ-ARCH-01]
dependencias: [HU-ARCH-01]
skills: ["cloudflare-one", "cloudflare", "built-in-browser", "meta-whatsapp"]
ola: 3
estado: borrador
---

# HU-ARCH-02 · Borde TLS y webhook de Meta de producción verificados

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-01](../spec.md) (D-SPEC-01-1).

**ID:** HU-ARCH-02

**Título:** Borde TLS y webhook de Meta de producción verificados

**Workstream:** Arquitectura/Prod

**Historia:** Como dueño de la app de Meta quiero que el webhook de producción esté detrás de un dominio propio con TLS y verificado por Meta para que los mensajes de los clientes lleguen sin depender del entorno de test.

**Por qué importa (valor empresarial):** Sin webhook de producción no hay WhatsApp en producción, y sin WhatsApp no hay producto. También es requisito de Meta para aprobar a SolversHub como Tech Provider (R-01).

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** S

**REQ mapeados:** REQ-ARCH-01

**Dependencias:** [HU-ARCH-01](HU-ARCH-01-produccion-fuera-de-dev.md)

**Criterios de aceptación (Gherkin):**
- **Verificación de Meta.** Dado el dominio de producción, cuando Meta llama al endpoint de verificación con el token correcto, entonces responde el `challenge` y la app queda suscrita.
- **TLS y Access.** Dado el túnel de producción, cuando se revisa, entonces `/webhooks/*` y `/healthz` no pasan por Access y el resto sí.
- **Mensaje real.** Dado un número de producción conectado, cuando un cliente escribe, entonces el mensaje entra por el webhook de producción y se responde.

**Evidencia / Definición de Terminado:**
- Captura de la configuración del webhook en la app de Meta y prueba de mensaje real.
- Reglas del túnel en `solvershub-infra`.

**Riesgos/Notas:**
- La app de Meta de producción no debe compartir `META_APP_ID` con test (riesgo de re-registrar la app de la plataforma, ver conexiones).

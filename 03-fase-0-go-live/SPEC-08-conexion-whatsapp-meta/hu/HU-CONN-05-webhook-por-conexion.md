---
id: HU-CONN-05
titulo: Webhook y secreto por conexión
spec: SPEC-08
fase: 0
hito: 0A
workstream: Canales y conexiones
prioridad: P0
critico: true
estimacion: M
impacto: [confianza]
req: [REQ-CONN-01]
dependencias: [HU-CONN-01, HU-ARCH-05]
skills: ["backend-design:security-discipline", "backend-design:security-reviewer", "cloudflare-one", "meta-whatsapp"]
ola: 3
estado: borrador
---

# HU-CONN-05 · Webhook y secreto por conexión

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-08](../spec.md).

**ID:** HU-CONN-05

**Título:** Webhook y secreto por conexión

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio con dos números (uno con mi app y otro conectado con Facebook) quiero que los mensajes de ambos lleguen y se verifiquen con el secreto correcto para operar varias conexiones a la vez.

**Por qué importa (valor empresarial):** Hoy agregar una conexión de Embedded Signup rompe los mensajes de la BYOK existente (401). Los negocios que crecen (sucursales, líneas de venta y soporte) necesitan varias conexiones: es requisito de los planes Premium y Empresarial.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-CONN-01

**Dependencias:** [HU-CONN-01](HU-CONN-01-credenciales-por-conexion.md), [HU-ARCH-05](../../SPEC-01-produccion-segura/hu/HU-ARCH-05-webhook-fail-closed.md)

**Criterios de aceptación (Gherkin):**
- **Convivencia.** Dado un negocio con una conexión BYOK y una ES, cuando entran mensajes a ambos números, entonces cada uno se verifica con el secreto de su conexión y se procesa.
- **Registro por conexión.** Dado "Registrar webhook" en el hub de una conexión BYOK, cuando se ejecuta, entonces se registra en la app de esa conexión con su URL y su token de verificación, sin tocar la app de la plataforma.
- **App de la plataforma.** Dado una conexión ES, cuando se intenta re-registrar el webhook, entonces solo el master puede hacerlo.

**Evidencia / Definición de Terminado:**
- Tests de webhook con dos conexiones y orígenes distintos; corrección de `meta_health_service.py:206-216` y `meta_byok.py:311-327`.

**Riesgos/Notas:**
- Defecto 4 y "una sola app por negocio" de la auditoría.

# Arquitectura de información del panel

Responde al encargo 3.3 y a la revisión del panel nuevo. La implementación está en
[SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md); las opciones de
Conexiones se mueven antes, en el Hito 0B ([HU-CONN-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md)).

> **Actualizada por [D-37](decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto) (2026-10-19):** se
> eligió la opción A y el árbol final (lenguaje D-35, ≤ 12 entradas, fichas de conexión y de agente) está en
> [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md#árbol-del-menú-v2-d-37). El hub de
> cada conexión ya no espera a [HU-CONN-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-08-lista-y-hub-meta.md): lo construye [HU-UX-09](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md).

## Menú actual (`solvershub-panel/apps/panel-web/components/shell/nav.ts:54-175`)

| Grupo | Ítems |
|---|---|
| Operación | Resumen, Conversaciones, Escalaciones, Leads |
| Configuración | Conexiones, Habilidades, Colaboradores, Configuración |
| Negocio | Costos LLM, Plan y consumo |
| Cobranza · Comercio · Calendario | Páginas de cada pack |
| Herramientas | Probar asistente, Plantillas WhatsApp, Bandeja de fallos, Requisitos de Meta, Producción |
| Plataforma | Tenants |

**Problemas**: términos técnicos ("Costos LLM", "Tenants", "Leads"); "Configuración" es grupo e ítem
a la vez; lo exclusivo de Meta (Requisitos, Producción, Plantillas) está en un grupo genérico y se
muestra a negocios sin Meta; el menú está escrito a mano y ya se desalineó del backend.

## Opciones

| Opción | Pros | Contras |
|---|---|---|
| **A. Agrupar por tarea del negocio** (atender, vender y cobrar, configurar el asistente, canales, consumo, equipo) | Lo entiende cualquier dueño; escala a packs nuevos | Mueve casi todo de lugar |
| B. Agrupar por habilidad (un grupo por pack) | Fácil de generar | El dueño piensa en tareas, no en packs |
| C. Mantener los grupos y solo renombrar | Cambio mínimo | No resuelve lo de Meta ni el crecimiento |

**Recomendación: A.**

## Menú propuesto

| Grupo | Ítems | Notas |
|---|---|---|
| **Inicio** | Resumen y primeros pasos | El checklist desaparece al completarse |
| **Atención** | Bandeja (conversaciones), Por atender (tickets), Clientes | "Clientes" une Leads del core y de comercio |
| **Ventas y cobros** (contribuido por habilidades, orden fijo) | Ventas (resumen, productos, pedidos, promociones), Suscripciones, Cobranza, Agenda | Solo aparece lo habilitado; el orden lo da el manifiesto ([HU-FWK-05](../04-fase-1-competir/SPEC-16-habilidades-como-plataforma/hu/HU-FWK-05-manifiesto-de-menu.md)) |
| **Asistente** | Identidad y tono, Flujo de conversación, Habilidades, Acciones personalizadas, Probar asistente, Calidad | El editor de flujo vive aquí ([SPEC-15](../04-fase-1-competir/SPEC-15-editor-visual-de-flujo/spec.md)) |
| **Canales** | Conexiones | Cada conexión de WhatsApp-Meta abre su hub: Salud · Números · Plantillas · Webhook · Producción · Costos de WhatsApp |
| **Consumo y plan** | Plan y créditos, Consumo de IA, Costos de WhatsApp | Costos de WhatsApp solo si alguna conexión los tiene activos |
| **Equipo** | Colaboradores, Roles y permisos | |
| **Configuración** | Negocio, Horario y escalamiento, Avanzado (incluye Mensajes fallidos) | |
| **Plataforma** (solo master) | Negocios, Planes y tarifario, App de Meta (requisitos de Tech Provider), Salud de habilidades, Auditoría | Aquí van los pasos que hoy ve cualquier negocio en "Requisitos" y "Producción" |

## Glosario de renombres (alineado con el manual de marca §9.3)

| Hoy | Nuevo |
|---|---|
| Tenant | Negocio |
| Plugin, pack | Habilidad |
| Tool | Acción |
| Costos LLM | Consumo de IA |
| Escalaciones | Por atender |
| Leads | Clientes |
| Bandeja de fallos, DLQ | Mensajes fallidos |
| Playground | Probar asistente |
| Kill-switch | Pausar asistente |
| BYOK | Usar mi propia llave |
| Guardrails | Reglas de seguridad |
| Evals | Pruebas de calidad |
| WABA | Cuenta de WhatsApp Business |
| Embedded Signup | Conectar con Facebook |

## Mapeo y redirecciones

> **Superada (2026-10-19, [D-37](decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto)):** la tabla
> vigente de redirecciones y el árbol v2 (≤ 12 entradas, fichas por objeto) viven en
> [SPEC-12 · Diseño](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/design.md#migración-despliegue-y-reversa).
> Esta tabla queda como antecedente.

| Ruta actual | Destino |
|---|---|
| `/dashboard` | Inicio → Resumen |
| `/conversaciones` | Atención → Bandeja |
| `/escalaciones` | Atención → Por atender (redirección permanente) |
| `/leads` | Atención → Clientes |
| `/costos` | Consumo y plan → Consumo de IA (pestaña WhatsApp si aplica) |
| `/plan` | Consumo y plan → Plan y créditos |
| `/conexiones/meta`, `/conexiones/requisitos`, `/conexiones/produccion`, `/plantillas` | Hub de cada conexión; los pasos de plataforma pasan a Plataforma → App de Meta |
| `/dlq` | Configuración → Avanzado → Mensajes fallidos |
| `/asistente` | Asistente → Probar asistente |
| `/tenants` | Plataforma → Negocios |

## Onboarding

| Pieza | Qué hace | HU |
|---|---|---|
| Invitación → primeros pasos | El owner acepta la invitación, define contraseña y cae en un checklist calculado del estado real: datos del negocio, WhatsApp conectado y verificado con un mensaje de prueba, catálogo o servicios, probar el asistente, invitar al equipo | [HU-SH-06](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md) |
| Tour de 5 pasos | Opcional, sin librería pesada, accesible por teclado | [HU-SH-06](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md) |
| Ayuda contextual | `Tooltip` accesible y modales "¿Qué es esto?" por sección, en lenguaje claro | [HU-UX-03](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-03-ayuda-contextual.md) |
| Estados vacíos con acción | Cada lista vacía dice qué hacer y ofrece el botón | [HU-UX-04](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-04-estados-vacios-y-permisos.md) |
| Guías por habilidad | Checklist y datos de ejemplo por pack y por preset | [HU-UX-05](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-05-guias-por-habilidad.md) |

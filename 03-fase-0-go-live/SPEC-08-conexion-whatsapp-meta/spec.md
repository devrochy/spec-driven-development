# SPEC-08 · Conexión WhatsApp-Meta efectiva

> Estado SDD: Diseño aprobado · Fase 0 · Hitos 0A (CONN-01 a 07) y 0B (CONN-08 a 10) · Workstream Canales y conexiones

## Problema

La auditoría del 2026-10-01 ([conexiones-y-costos-meta.md](../../01-revalidacion/conexiones-y-costos-meta.md))
encontró que **el sistema no sabe qué credenciales usar según la conexión**:

- Las tools de Meta (Números, Plantillas, salud, re-suscribir, sincronización de precios, créditos y
  el cron de plantillas) solo leen el token de Embedded Signup y el secreto de la plataforma: **fallan
  para BYOK**, que es el único alta que funciona.
- **BYOK y Embedded Signup en el mismo negocio rompen los mensajes entrantes de BYOK**
  (`core/gateway/meta_byok.py:311-327`).
- **Dos errores 500**: Números (`PhoneNumber.status`, `core/admin/meta_numbers_service.py:91`) y créditos
  de Meta (`MetaConnection.label`, `core/api/routers/costs.py:200`); el wizard falla con 500 al
  reiniciar después de 24 h.
- **Ciclo de vida inseguro**: "Desactivar" no detiene al bot; "Eliminar" borra en duro números, WABA,
  costos y plantillas (invariante 8); "Activar" fuerza `connected` en borradores.
- **Diagnóstico falso**: verde aunque no haya token; la salud se sobrescribe y pierde campos.
- **BYOK fijado en sandbox** (`meta_byok.py:97`), sin promoción a producción; el checklist de
  producción es imposible (exige page e Instagram y corre pytest dentro de la imagen).
- **UX confusa**: iconos por canal y no por tipo, estado sin motivo, sin entorno visible, opciones
  exclusivas de Meta en menús globales, "Editar" que da 404 en WhatsApp Web y Calendar.
- **Costos de Meta**: no se habilitan (se muestran siempre) y nunca tienen datos.

## Usuarios y contexto

- **Dueño de un negocio** que conecta su WhatsApp en prueba y luego en producción.
- **Equipo de SolversHub** que soporta conexiones y opera la app de Meta de la plataforma.

## Por qué importa (valor empresarial)

WhatsApp es el canal núcleo. Si conectar un número es confuso o falla, no hay cliente: es el punto
donde más negocios abandonan en cualquier plataforma de la matriz. Además, una conexión desactivada
que sigue respondiendo o un borrado que destruye el historial son incidentes de confianza que un
cliente no perdona.

## Alcance

| HU | Qué | Hito |
|---|---|---|
| [HU-CONN-01](hu/HU-CONN-01-credenciales-por-conexion.md) ★ | Resolver de credenciales por conexión | 0A |
| [HU-CONN-02](hu/HU-CONN-02-errores-500-y-bloqueos.md) ★ | Errores 500 y bloqueos | 0A |
| [HU-CONN-03](hu/HU-CONN-03-ciclo-de-vida-seguro.md) ★ | Ciclo de vida seguro | 0A |
| [HU-CONN-04](hu/HU-CONN-04-diagnostico-confiable.md) ★ | Diagnóstico confiable | 0A |
| [HU-CONN-05](hu/HU-CONN-05-webhook-por-conexion.md) ★ | Webhook y secreto por conexión | 0A |
| [HU-CONN-06](hu/HU-CONN-06-byok-produccion.md) ★ | BYOK de producción | 0A |
| [HU-CONN-07](hu/HU-CONN-07-checklist-produccion-real.md) ★ | Checklist de producción real | 0A |
| [HU-CONN-08](hu/HU-CONN-08-lista-y-hub-meta.md) | Lista v2 y hub de WhatsApp-Meta | 0B |
| [HU-CONN-09](hu/HU-CONN-09-costos-meta-verificables.md) | Costos de Meta verificables y opcionales | 0B |
| [HU-CONN-10](hu/HU-CONN-10-conexiones-no-meta.md) | Conexiones que no son Meta | 0B |

## Decisiones

- WhatsApp Web comercial: [P-08](../../02-vision-y-decisiones/preguntas-abiertas.md#p-08--whatsapp-web-no-oficial-adr-0074) (recomendado: no en v1).

### D-SPEC-08-1 · Organización de Conexiones

| Opción | Pros | Contras |
|---|---|---|
| **A. Lista genérica + hub por tipo (Meta, WhatsApp Web, Calendar); las opciones de Meta viven en el hub de cada conexión; lo de la app de la plataforma va a "Plataforma"** | Cada negocio ve solo lo suyo; escala a Instagram y Messenger | Más páginas |
| B. Mantener las páginas globales y mejorar los textos | Menos trabajo | Siguen mezcladas cosas del negocio y de la plataforma |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): lista genérica + hub por tipo.

### D-SPEC-08-2 · Costos de Meta

| Opción | Pros | Contras |
|---|---|---|
| **A. Subsección opcional dentro de cada conexión, con flag por conexión (encendida por defecto en producción), botón "Verificar" y tarjeta agregada solo si alguna conexión la tiene** | Responde "¿cómo se habilita?"; verificable; nada vacío por defecto | Requiere el resolver de credenciales |
| B. Mantener la sección global siempre visible | Sin cambios | Vacía y confusa en la mayoría de los negocios |
| C. Quitar los costos de Meta | Simple | Se pierde transparencia (PLUS-03) justo cuando Meta empieza a cobrar más |

**Recomendación: A.** Estado: ✅ tomada (2026-10-02): subsección opcional por conexión con botón Verificar.

## Fuera de alcance

Instagram y Messenger ([HU-CHAN-01](../../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-01-instagram-y-messenger.md)), campañas ([HU-CHAN-03](../../04-fase-1-competir/SPEC-17-canales-y-campanas/hu/HU-CHAN-03-pack-marketing.md)), reventa de créditos de Meta (D-06).

## Métricas de éxito

- Alta de WhatsApp en prueba < 15 minutos y en producción < 1 día, sin soporte.
- 0 errores 500 en Conexiones; 0 conexiones desactivadas que respondan.
- Costos de Meta con datos en el 100 % de las conexiones de producción con la flag activa.

## Requerimientos cubiertos

REQ-CONN-01 a REQ-CONN-05, REQ-PLUS-02.

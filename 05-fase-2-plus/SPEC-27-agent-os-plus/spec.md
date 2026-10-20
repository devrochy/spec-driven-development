# SPEC-27 · Agent OS Plus

> Estado SDD: En revisión · Fase 2 · Workstream Agent OS · Continúa [SPEC-26](../../04-fase-1-competir/SPEC-26-agent-os/spec.md)

## Problema

Agent OS v1 ([SPEC-26](../../04-fase-1-competir/SPEC-26-agent-os/spec.md)) cubre un negocio con varias conexiones y agentes coherentes. Quedan fuera:
- colaborar con agentes de **otros** negocios;
- ejecutar integraciones de terceros no confiables;
- proponer mejoras de forma automática;
- atender por API, Slack o correo entrante;
- escalar el runtime cuando las métricas lo pidan;
- que el negocio cree la **estructura** de sus propios superpoderes.

## Usuarios y contexto

Negocios con aliados o agencias, integradores, operadores de la plataforma e implementadores.

## Por qué importa (valor empresarial)

Extiende el Agent OS a marketplace, integraciones y canales nuevos sin romper el aislamiento ni la consistencia que lo diferencian.

## Alcance

| HU | Qué |
|---|---|
| [HU-AOS-39](hu/HU-AOS-39-federacion-entre-negocios.md) | Federación entre negocios con consentimiento |
| [HU-AOS-40](hu/HU-AOS-40-sandbox-de-acciones.md) | Sandbox aislado para acciones no confiables |
| [HU-AOS-41](hu/HU-AOS-41-auto-mejora-asistida.md) | Auto-mejora asistida: de fallas a versión candidata |
| [HU-AOS-42](hu/HU-AOS-42-canal-api-y-webhooks.md) | Canal API y webhooks salientes como conexión |
| [HU-AOS-43](hu/HU-AOS-43-slack-y-correo-entrante.md) | Slack y correo entrante como conexiones |
| [HU-AOS-44](hu/HU-AOS-44-topologia-por-roles.md) | Topología por roles y escalado del runtime |
| [HU-AOS-45](hu/HU-AOS-45-editor-de-estructura-de-superpoderes.md) | Editor de estructura de superpoderes para el negocio |

## Escenarios clave (Gherkin)

- **Federación revocable.** Dado una federación activa, cuando una parte la revoca, entonces la siguiente llamada se deniega de inmediato.
- **Sandbox.** Dado una acción no confiable, cuando intenta salir a un dominio no permitido, entonces se bloquea.
- **Canal API.** Dado un mensaje por API repetido con la misma clave, cuando llega, entonces se procesa una sola vez.

## Decisiones

### D-SPEC-27-1 · Mecanismo de federación entre negocios

| Opción | Pros | Contras |
|---|---|---|
| **A. Concesiones con doble consentimiento + gateway de federación; solo resultados tipados** | Aislamiento intacto; revocable al instante | Hay que operar las concesiones |
| B. Agentes compartidos entre negocios | Simple de usar | Rompe el aislamiento por negocio |
| C. Protocolo A2A abierto entre plataformas | Interoperabilidad externa | Superficie de seguridad nueva sin demanda probada |

**Recomendación: A.** Estado: ⏳ pendiente (diferida hasta 2 interesados reales, P-15).

### D-SPEC-27-2 · Aislamiento para acciones no confiables

| Opción | Pros | Contras |
|---|---|---|
| **A. Contenedor efímero con egress por allowlist y límites de CPU, memoria y tiempo** | Tecnología conocida, opera en el VPS | Arranque en frío |
| B. MicroVM | Aislamiento más fuerte | Más operación |
| C. WASM | Rápido | Ecosistema limitado para integraciones |

**Recomendación: A.** Estado: ⏳ pendiente.

## Fuera de alcance

Voz en llamadas ([SPEC-23](../SPEC-23-voz-reportes-y-confianza/spec.md)); agencias y sub-cuentas ([SPEC-21](../SPEC-21-agencia-e-internacional/spec.md)), que se coordinan con la federación.

## Métricas de éxito

- 0 accesos entre negocios fuera de una federación activa (tests y auditoría).
- 0 escapes del sandbox en las pruebas.
- p99 del webhook bajo el umbral tras separar por rol.

## Requerimientos cubiertos

REQ-AOS-01, REQ-AOS-03, REQ-AOS-09, REQ-AOS-12, REQ-AOS-13, REQ-AOS-15, REQ-AOS-16.

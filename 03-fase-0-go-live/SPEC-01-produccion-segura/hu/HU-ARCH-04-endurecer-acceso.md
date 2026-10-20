---
id: HU-ARCH-04
titulo: Endurecer el acceso al panel, la API y la API de campo
spec: SPEC-01
fase: 0
hito: 0A
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, legal]
req: [REQ-ARCH-04]
dependencias: []
skills: ["backend-design:auth-and-authorization", "backend-design:security-discipline", "backend-design:security-reviewer", "/codex:adversarial-review"]
ola: 2
estado: en-curso
---

# HU-ARCH-04 · Endurecer el acceso al panel, la API y la API de campo

> Estado SDD: En curso — issue [core #260](https://github.com/devrochy/agent-core/issues/260).

**ID:** HU-ARCH-04

**Título:** Endurecer el acceso al panel, la API y la API de campo

**Workstream:** Arquitectura/Prod

**Historia:** Como responsable de seguridad quiero bloqueo por intentos fallidos, cabeceras de seguridad, verificación de origen en el BFF y credenciales fuera de los documentos para que nadie entre al panel o a la API de campo por fuerza bruta o por un secreto filtrado.

**Por qué importa (valor empresarial):** El panel da acceso a los datos de todos los clientes de un negocio y el master a todos los negocios. Un acceso indebido es el peor incidente posible para una plataforma multi-tenant y tumba cualquier venta enterprise.

**Prioridad:** P0 go-live ★ (Hito 0A)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-04

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Bloqueo progresivo.** Dado 5 intentos fallidos para un mismo identificador o IP en 10 minutos, cuando llega el sexto, entonces se rechaza por 15 minutos con un mensaje neutro y queda auditado; lo mismo en `/auth/gestor/login` de la API de campo.
- **Origen verificado.** Dado una petición que cambia estado al BFF del panel con un `Origin` ajeno, cuando llega, entonces se rechaza.
- **Cabeceras.** Dado el panel y la landing de producción, cuando se inspeccionan, entonces envían HSTS, CSP, `X-Frame-Options` y `Referrer-Policy`.
- **Credencial del master.** Dado el historial de `solvershub-comercial` (commits `ba251fe`, `e3790a8`), cuando se revisa, entonces la credencial del master se rotó y, si estaba en el historial, se limpió o se documentó el riesgo.
- **Escaneo.** Dado cualquier repo `solvershub-*`, cuando corre gitleaks en CI, entonces no hay secretos.

**Evidencia / Definición de Terminado:**
- Tests de integración del bloqueo (API y API de campo) con aislamiento por negocio.
- Resultado de un escáner de cabeceras sobre panel y landing.
- Nota de la revisión del historial (sin copiar la credencial).

**Implementada (2026-10-07):** bloqueo progresivo de login en [agent-core #259](https://github.com/devrochy/agent-core/pull/259) (ADR-0105: 5 fallos/10 min → 15 min de bloqueo con mensaje neutro, en `/api/v1/auth/login` y `/auth/gestor/login` con aislamiento por negocio y auditoría); cabeceras (HSTS/CSP/X-Frame-Options/Referrer-Policy) y verificación de origen del BFF en [panel #27](https://github.com/devrochy/solvershub-panel/pull/27); cabeceras + gitleaks en [landing #6](https://github.com/devrochy/solvershub-landing/pull/6); gitleaks en [comercial #9](https://github.com/devrochy/solvershub-comercial/pull/9). **Pendiente del cliente:** purga del historial de la credencial del master (N-27, commits `ba251fe`/`e3790a8`) y verificar cabeceras en producción.

**Verificación en test (2026-10-08):** bloqueo progresivo OK en `/api/v1/auth/login` (5 × 401, 6.º 429 «Demasiados intentos…») y en `/api/pack/pack_cobranza/auth/gestor/login` (6.º 429); BFF con `Origin` ajeno → 403; panel de test con HSTS, CSP, `X-Frame-Options: DENY` y `Referrer-Policy`. **Defecto encontrado y arreglado:** el BFF no reenviaba la IP del usuario y `client_ip` confiaba en cualquier `X-Forwarded-For`, así que 5 fallos de cualquiera bloqueaban el login del panel para todos 15 minutos (pasó en test) y la IP se podía falsificar → [agent-core #276](https://github.com/devrochy/agent-core/pull/276) (`TRUSTED_PROXY_CIDRS`, primera IP no confiable de derecha a izquierda) + [panel #36](https://github.com/devrochy/solvershub-panel/pull/36). **Pendientes:** el bloqueo queda en el log estructurado (`auth_login_blocked`), no en `audit_log` (decidir si basta); la landing de producción (`www.solvershub.site`) todavía no envía las cabeceras de landing #6 (falta desplegarla); purga de N-27 (dueño). Nota: la CSP del panel incluye `'unsafe-eval'`.

**Riesgos/Notas:**
- El panel nuevo ya mitiga CSRF con la cookie `SameSite=Lax` del BFF; la verificación de origen es defensa adicional.
- La revisión del historial quedó bloqueada para el agente: la hace el cliente.

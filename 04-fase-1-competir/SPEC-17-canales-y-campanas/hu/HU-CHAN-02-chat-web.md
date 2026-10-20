---
id: HU-CHAN-02
titulo: Chat web embebible
spec: SPEC-17
fase: 1
hito: "1"
workstream: Canales y conexiones
prioridad: P1
critico: false
estimacion: L
impacto: [ingreso, diferenciacion]
req: [REQ-FIX-02, REQ-COMP-01]
dependencias: []
skills: ["turnstile-spin", "frontend-design", "backend-design:security-reviewer"]
estado: terminada
---

# HU-CHAN-02 · Chat web embebible

> Estado SDD: Terminada — implementada 2026-10-03.

**ID:** HU-CHAN-02

**Título:** Chat web embebible

**Workstream:** Canales y conexiones

**Historia:** Como dueño de un negocio quiero pegar un fragmento en mi sitio web y que mis visitantes conversen con el mismo asistente para convertir visitas en ventas sin que salgan de mi página.

**Por qué importa (valor empresarial):** Casi todos los competidores ofrecen chat web; el plan Empresarial ya lo promete. Además el chat web no paga mensajes a Meta.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-FIX-02, REQ-COMP-01

**Dependencias:** —

**Criterios de aceptación (Gherkin):**
- **Instalar.** Dado el fragmento con la clave del negocio, cuando lo pego en un dominio permitido, entonces aparece el widget con la marca del negocio.
- **Conversar.** Dado un visitante, cuando escribe, entonces responde el mismo asistente con las mismas habilidades, con protección anti-bots.
- **Continuar en WhatsApp.** Dado un visitante que prefiere WhatsApp, cuando lo pide, entonces se le ofrece el enlace con el contexto.
- **Dominio no permitido.** Dado otro dominio, cuando carga el fragmento, entonces el widget no funciona.

**Evidencia / Definición de Terminado:**
- Widget, endpoint del canal `web`, CSP por negocio; tests.

**Implementada (2026-10-03):** canal `web` en agent-core ([#202](https://github.com/devrochy/agent-core/pull/202)): `app_settings.web_chat_config` (migración 0047: enabled, clave pública, dominios permitidos, secreto Turnstile), superficie pública `/api/v1/public/web-chat/{key}` (POST valida Origin+Turnstile+rate-limit y encola al mismo stream; GET respuestas/config), paquete `channel-web` y tolerancia a canales solo-salida en el registry. Widget embebible en la landing ([#4](https://github.com/devrochy/solvershub-landing/pull/4)): `/w/{key}` (chat), `/widget.js` (cargador), proxy server-side `/api/webchat/{key}/*` y CSP `frame-ancestors` por dominio permitido. Tests puros del registry/outbound/Origin/rate-limit.

**Completado después:** API `GET/PUT /admin/settings/web-chat` ([core #203](https://github.com/devrochy/agent-core/pull/203)) y pantalla **Chat web** en Configuración del panel ([panel #19](https://github.com/devrochy/solvershub-panel/pull/19)): activar, dominios permitidos, Turnstile, rotar clave y copiar el fragmento `<script>`.

**Riesgos/Notas:**
- Reutiliza el patrón del formulario alojado `/f/<slug>` de la landing.

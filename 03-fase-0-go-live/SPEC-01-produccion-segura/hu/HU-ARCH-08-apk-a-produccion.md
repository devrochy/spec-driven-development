---
id: HU-ARCH-08
titulo: APK de cobranza lista para producción
spec: SPEC-01
fase: 0
hito: 0B
workstream: Arquitectura/Prod
prioridad: P0
critico: true
estimacion: M
impacto: [confianza, diferenciacion]
req: [REQ-ARCH-16, REQ-PLUS-04]
dependencias: [HU-ARCH-02]
skills: ["backend-design:security-discipline", "backend-design:security-reviewer", "/code-review"]
estado: borrador
---

# HU-ARCH-08 · APK de cobranza lista para producción

> Estado SDD: **Absorbida por [SPEC-25](../../../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md)** (D-34, 2026-10-14). Sus criterios ya los cumplen [HU-APP-06](../../../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-06-almacenamiento-local-cifrado.md) (cola cifrada), [HU-APP-16](../../../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-16-seguridad-de-la-app.md) (solo HTTPS con pinning) y [HU-APP-17](../../../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-17-release-firmado-y-guias.md) (build firmado). Dos notas quedaron desfasadas: el campo usa `/api/pack/pack_cobranza` (v2 camelCase, [SPEC-25](../../../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md) `design.md`) y el login de propietario sí está en la app (login unificado). Se conserva como historial; no se ejecuta.

**ID:** HU-ARCH-08

**Título:** APK de cobranza lista para producción

**Workstream:** Arquitectura/Prod

**Historia:** Como cobrador en la calle quiero una app instalada desde un build firmado que hable solo HTTPS con producción y guarde mi cola offline cifrada para cobrar sin poner en riesgo los datos de los clientes.

**Por qué importa (valor empresarial):** La APK offline de cobranza es un diferencial que casi nadie en la matriz tiene, pero hoy permite HTTP plano (`usesCleartextTraffic: true`) y guarda pagos y documentos sin cifrar en el teléfono. Un celular perdido no puede convertirse en una fuga de datos.

**Prioridad:** P0 go-live ★ (Hito 0B)

**Estimación:** M

**REQ mapeados:** REQ-ARCH-16, REQ-PLUS-04

**Dependencias:** [HU-ARCH-02](HU-ARCH-02-borde-tls-y-webhook-prod.md)

**Criterios de aceptación (Gherkin):**
- **Solo HTTPS.** Dado el build de producción, cuando intenta una URL `http://`, entonces la petición se bloquea.
- **API vigente.** Dado la APK, cuando llama al backend, entonces usa `/api/v1/gestor/*` (no el alias `/api/pack/pack_cobranza` en retiro, ADR-0077).
- **Cola cifrada.** Dado eventos offline pendientes, cuando se inspecciona el almacenamiento del teléfono, entonces están cifrados con una llave guardada en `expo-secure-store`.
- **Build firmado.** Dado el perfil `production` de EAS, cuando se construye, entonces genera un artefacto firmado instalable y su versión queda registrada.

**Evidencia / Definición de Terminado:**
- Build de EAS de producción con enlace y hash.
- Tests de la cola cifrada y de la URL base.
- `docs/ai/tasks/*` con estados actualizados (hoy dicen "pendiente" lo que ya está hecho).

**Riesgos/Notas:**
- El login de propietario en la APK queda fuera (el propietario usa el panel web).
- Requiere `openapi.json` con las rutas `/api/v1/gestor/*` publicadas.

---
id: HU-APP-16
titulo: "Seguridad de la app: certificate pinning y hardening"
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [confianza]
req: [REQ-APP-06]
dependencias: [HU-APP-06]
skills: [backend-design:security-discipline, backend-design:auth-and-authorization]
estado: terminada
---

# HU-APP-16 · Seguridad de la app: certificate pinning y hardening

> Estado SDD: Terminada — implementada 2026-10-06; pinning verificado en dispositivo (positivo y negativo) 2026-10-08; pins por perfil en [solvershub-apk #137](https://github.com/devrochy/solvershub-apk/pull/137).

**ID:** HU-APP-16

**Título:** Seguridad de la app: certificate pinning y hardening

**Workstream:** App móvil

**Historia:** Como responsable de seguridad quiero que la app valide el certificado del servidor con pinning, proteja tokens con biometría, no permita tráfico plano en producción y cumpla el checklist OWASP MASVS L1, para resistir interceptación y análisis en dispositivos de campo.

**Por qué importa (valor empresarial):** La app maneja dinero e información personal de clientes de terceros. El pinning y el hardening convierten el APK en un cliente confiable para negocios reales y son requisito de la [HU-ARCH-08](../../../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-08-apk-a-produccion.md) (APK lista para producción) y del discurso de venta de seguridad de la plataforma.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-06

**Dependencias:** [HU-APP-06](HU-APP-06-almacenamiento-local-cifrado.md)

**Criterios de aceptación (Gherkin):**
- **Pinning.** Dado un build de producción, cuando la app habla con la API, entonces valida el certificado contra dos pins (certificado actual + reserva) y falla la conexión ante un certificado distinto.
- **Perfiles.** Dado el build de staging o dev, cuando se configura el perfil, entonces el pin y el host se toman del perfil (override por build, sin código distinto).
- **HTTPS.** Dado un build de producción, cuando se intenta tráfico claro, entonces queda bloqueado (`usesCleartextTraffic` solo en dev).
- **MASVS L1.** Dado el APK preview, cuando se recorre el checklist MASVS L1 documentado, entonces los ítems de plataforma (storage, crypto, red, interacción) están verificados con evidencia.
- **Auditoría.** Dado una acción crítica (pago, abono, borrado, liquidación, cambio de plan), cuando se ejecuta (incluso offline), entonces se registra en auditoría local con usuario, dispositivo y timestamp, y se sincroniza al backend.

**Evidencia / Definición de Terminado:**
- Módulo local Expo `solvershub-pinning` (CertificatePinner OkHttp / TrustKit en iOS-ready) con configuración por perfil EAS; hardening de red; checklist MASVS L1 en `docs/seguridad.md` con resultados; auditoría local enlazada con `POST /api/v1/audit/mobile-events` (backend con idempotencia por event_id); tests del módulo y CI verde.

**Verificación en dispositivo real (2026-10-07):** smoke E2E completo en verde contra
`https://test.solvershub.site` (APK preview) — el login y todo el flujo de campo pasan por el
pin de la CA (LE YE2 / ISRG Root X2), lo que valida el pinning en positivo.

**Prueba negativa en dispositivo (2026-10-08, OPPO CPH2603):** con
[solvershub-apk #137](https://github.com/devrochy/solvershub-apk/pull/137) los pins salen del perfil
de EAS (`SOLVERSHUB_PINS`), lo que cumple el criterio *Perfiles*, y el perfil `preview-pin-negativo`
compila un pin ajeno. Misma red y mismas credenciales:
- APK negativo (EAS `c9b35466`, solo el pin ajeno en el XML compilado): el login falla con "Sin
  conexión con el servidor", un fallo de red/TLS y no 401/403. No llega al selector de negocio.
- Control (EAS `e005ae24`, LE YE2 + ISRG Root X2): el login entra a "Elige tu negocio".

Pins vigentes comprobados con `openssl` en `test.` y `app.solvershub.site`. La evidencia y el
procedimiento para repetirla en cada release están en `docs/seguridad.md` de la app. El checklist
MASVS L1 está documentado ahí con los ítems de plataforma en ✅; anti-tamper queda como deuda L2.
El runbook de rotación también se corrigió: el NSC es nativo y un OTA no cambia los pins.

**Implementada (2026-10-06):** [solvershub-apk #122](https://github.com/devrochy/solvershub-apk/pull/122) — pinning por CA (network security config) y auditoría de acciones críticas (603/603 tests). ~~Pendiente: prueba positiva/negativa del pinning~~ → hecha el 2026-10-08 (arriba).

**Riesgos/Notas:**
- Rotación de certificados: se publica la reserva como segundo pin en cada release; runbook de rotación documentado.
- El pinning en staging usa el certificado del túnel del entorno de test, no el de producción.
- La auditoría móvil reutiliza el patrón de cola idempotente; la UI de auditoría del panel ya existe (cobranza) y la del core se enriquece con `source=mobile` en esta HU.

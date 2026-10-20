---
id: HU-APP-17
titulo: Release firmado y guías de build
spec: SPEC-25
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: M
impacto: [operacion, confianza]
req: [REQ-APP-10, REQ-ARCH-16]
dependencias: [HU-APP-07, HU-APP-15, HU-APP-16]
skills: [release, adr]
estado: en-curso
---

# HU-APP-17 · Release firmado y guías de build

> Estado SDD: En curso — todo listo y verificado en dispositivo (2026-10-08); solo falta la cuenta de Play Console + `eas submit`.

**ID:** HU-APP-17

**Título:** Release firmado y guías de build

**Workstream:** App móvil

**Historia:** Como responsable de operación quiero un pipeline de release reproducible (dev/preview/staging/production vía EAS), firma gestionada en EAS con runbook de respaldo, publicación a Play Console y guías de build/rollback, para que cualquier versión de la app oficial se pueda reconstruir y revertir sin adivinanzas.

**Por qué importa (valor empresarial):** Un build reproducible y firmado es el requisito final de "APK lista para producción" (REQ-ARCH-16/HU-ARCH-08) y la garantía de que la app oficial se distribuye con la misma disciplina de release que el resto de repos.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-APP-10, REQ-ARCH-16

**Dependencias:** [HU-APP-07](HU-APP-07-cobranza-al-nucleo-sin-regresion.md), [HU-APP-15](HU-APP-15-sync-offline-por-modulos.md), [HU-APP-16](HU-APP-16-seguridad-de-la-app.md)

**Criterios de aceptación (Gherkin):**
- **Perfiles.** Dado el `eas.json`, cuando se construye, entonces existen perfiles `development`, `preview` (APK), `staging` (AAB, Internal Testing) y `production` (AAB, Play) con variables de entorno por perfil.
- **Firma.** Dado un build de producción, cuando se firma, entonces lo hace el keystore gestionado por EAS (nunca en el repo) y el runbook documenta respaldo y rotación; `com.solvershub.apk` y el projectId de EAS no cambian.
- **Reproducible.** Dado el mismo commit y perfil, cuando se reconstruye, entonces se obtiene el mismo AAB (lockfile commiteado, SDK pineado, fuentes documentadas).
- **Publicación.** Dado un AAB de producción, cuando se ejecuta `eas submit`, entonces llega a Play Console con nota de release desde el CHANGELOG.
- **Rollback.** Dado un release con defecto, cuando se revierte, entonces el runbook indica OTA (EAS Update a canal anterior) o re-publicación del AAB anterior, y el criterio para elegir uno u otro.

**Evidencia / Definición de Terminado:**
- `eas.json` con 4 perfiles y secrets vía EAS (nada en el repo); workflow de CI que corre `npm run check` y dispara el build de `preview` en PRs de release; `docs/build-release.md` (entornos, firma, reproducción, publicación, rollback) y `docs/arquitectura.md` actualizados; un AAB staging publicado en Internal Testing con evidencia en test.

**Implementada (2026-10-06):** [solvershub-apk #124](https://github.com/devrochy/solvershub-apk/pull/124) — perfiles EAS development/preview/staging/production, firma gestionada y `docs/build-release.md`. **Pendiente:** smoke Maestro con el build `preview` y la cuenta de Play Console + `eas submit`.

**Riesgos/Notas:**
- La firma en EAS requiere que las credenciales de EAS estén fuera del repo y con respaldo seguro (documentado, no versionado).
- OTA no puede cambiar código nativo: el runbook distingue releases que requieren AAB nuevo (cambios nativos/permisos) de los que se resuelven con EAS Update.
- El envío a Play queda supeditado a la cuenta de desarrollador y los trámites de Meta/legales en curso del plan (Semana 0).

**Listo para Play (2026-10-08):** [solvershub-apk #145](https://github.com/devrochy/solvershub-apk/pull/145).
- **EAS Update (OTA):** `runtimeVersion` por fingerprint y un canal por perfil. Se publica con
  `scripts/publicar-ota.sh`, que fija la API de cada canal porque `eas update` no usa el `env` de los
  perfiles. `fingerprint.config.js` ignora el `google-services.json` que inyecta EAS; sin eso, los
  fingerprints de local y EAS no coincidían y el build fallaba.
- **Verificado en el OPPO** (build `preview` `c6badbc0`): un OTA de prueba cambió el título del
  Resumen sin reinstalar, y `eas update:republish` lo revirtió.
- **Perfiles y submit:** `staging` y `production` como AAB de tienda con `autoIncrement`; `submit` a la
  pista interna y a producción, ambos en borrador.
- **`docs/build-release.md`:** OTA o AAB según el fingerprint, rollback real, firma y respaldo del
  keystore, pasos del dueño en Play Console y checklist de release.
- El smoke en dispositivo ya estaba cubierto (campo y dueño con Maestro, `e2e/`), igual que el
  pinning ([HU-APP-16](HU-APP-16-seguridad-de-la-app.md)).

**Falta (dueño):** la cuenta de Play Console, la primera subida manual a *Prueba interna* y la
cuenta de servicio en EAS para `eas submit`. También respaldar el keystore antes de publicar.

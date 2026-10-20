# 10 · Pendientes del dueño

Lo que solo puedes hacer tú (cuentas, secretos, trámites, aprobaciones y decisiones), al **2026-10-17**. Marca cada
casilla al terminar y anota la fecha.

Qué cambió desde la lista del 2026-10-09: ya están hechos el merge de panel #54, el despliegue a test (`develop`
`55b0075`, migraciones hasta la 0089, catálogos v5 y v6 importados), la URL de eventos de Wompi sandbox,
`PANEL_BASE_URL` en app, worker y beat, la app de Meta nueva cargada en test (`META_APP_ID`, `META_APP_SECRET`,
`META_CONFIG_ID` y `WHATSAPP_VERIFY_TOKEN`) y el dominio `solvershub.site` verificado en Meta. Las tandas 1 a 5 del
Agent OS están mergeadas (y la 7, [HU-AOS-23](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-23-consola-de-conexiones.md), 24 y 47, el 2026-10-18) ([bitácora](08-bitacora-de-ejecucion.md)) y el ciclo de pruebas «2026-10-13 · catálogo v5»
tiene su [informe](11-pruebas/informes/ciclo-2026-10-13.md).

El orden es el del plan del 2026-10-17: **A** destraba las pruebas de hoy, **B** son decisiones de una línea, **C** son
trámites que tardan y corren solos, **D** es producción, que no se trabaja ahora y solo se referencia. La configuración
de test y los puntos de producción viven en el panel de pruebas (Plataforma › Pruebas, pestañas «Configuración de
test» y «Paso a producción»); aquí se citan por su `id` del [catálogo](11-pruebas/catalogo.yaml) para no tener dos
listas.

## A · Para cerrar las pruebas ahora

1. [ ] **Enviar tu ejecución y cerrar el ciclo «2026-10-13 · catálogo v5»** en `/pruebas/ciclos` (genera el resumen y
   deja la foto fija), y pedirles a las dos testers que envíen la suya desde `/pruebas`. Con el ciclo cerrado, el
   artifact «Camino a producción» queda de solo lectura y se cierra [HU-QA-05](04-fase-1-competir/SPEC-30-centro-de-pruebas/hu/HU-QA-05-migrar-desde-el-artifact.md).
2. [ ] **Repetir en test las pruebas del Agent OS** por chat web con `solvershub` (v3 + procedimientos): **A** contratar
   Premium con el flujo nuevo (lista de datos, resumen único, pago), **B** cambio de opinión, **C** agendar una demo; y
   la **promesa de pago** por WhatsApp QR en `demo-cobranza-norte`. Cada una se registra en `/pruebas` como ítem nuevo
   del área Agentes (catálogo v7). Antes, con tu OK, Claude cancela las 4 tareas viejas de `contratar_plan` 1.1.0.
3. [ ] **OK para la medición pass^4** de los 4 procedimientos con LLM real (~1–3 USD): es la compuerta de
   [HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md) y de la tanda 6.
4. [ ] **Confirmar `WOMPI_BILLING_EVENTS_SECRET`** en test (última evidencia: firma inválida) junto con la URL de
   eventos `https://test.solvershub.site/webhooks/billing/wompi` (`test-url-de-eventos-en-el-dashboard-de-wompi-sandbox`).
   De paso, OK para que Claude revise que el playbook copiado sigue en el volumen del API y por qué los volúmenes
   `tenants-data` del worker y el beat están vacíos.
5. [ ] **SMTP de test, sin verificar:** `SYSTEM_SMTP_HOST/PORT/USERNAME/PASSWORD/FROM` en app y worker, y reiniciar
   (`test-smtp-del-sistema-en-app-y-worker`). Sin esto no llegan la invitación de un tester, el correo del informe ni
   el código de recuperación.
6. [ ] **Token permanente de System User** en la conexión de `solvershub`
   (`test-token-permanente-de-system-user-en-la-conexion-de-solvershub`): el temporal venció y el asistente no
   responde por WhatsApp.
7. [ ] **Plantilla de utilidad en español con el link de pago** aprobada en la WABA de test
   (`test-plantilla-de-utilidad-en-espanol-con-link-de-pago`): hoy solo sirve `hello_world`; sin ella no se prueban
   los avisos fuera de la ventana de 24 h ni el cobro por WhatsApp. El número de prueba sigue `NOT_VERIFIED`
   (`test-verificar-el-numero-de-prueba-de-solvershub`).
8. [ ] **Pendientes chicos de test que siguen abiertos**, todos en la pestaña «Configuración de test»: la app BYOK
   vieja `1593078865797352` (su App Secret salió en un log: rotarlo o, si la app ya no existe, marcar el ítem como
   «no aplica»; `test-rotar-el-app-secret-de-la-app-byok-1593078865797352`); los secretos del workflow de evals del
   repo comercial (`test-secretos-del-workflow-de-evals-repo-comercial`); `checkout_fields.plan` con `id_document` y
   `phone` y una versión **de prueba** de términos, privacidad y DPA en Tenants → Alta automática
   (`test-datos-del-negocio-solvershub-para-el-alta-automatica`); los 4 cargos viejos de `solvershub` sin
   `fecha_vencimiento` (`test-cargos-viejos-sin-fecha-de-vencimiento`).

## B · Decisiones cortas

Se cierran en el PR de docs como D-36, cada una con una línea tuya:

9. [ ] **¿Se descontinúa el panel clásico?** Tú y la tester 1 lo abrieron roto (estilos, «not found»). Si sí, se
   retiran la prueba y el enlace; si no, se arregla.
10. [ ] **Confirmar las cifras de los planes** del modelo de precios § 5 (PR de docs en paralelo): las dimensiones
    agentes publicados, crédito mensual y colaboradores ya las confirmaste; faltan los topes por plan (1 / 2 / 5 /
    ilimitados agentes, etc.), si entran conexiones adicionales por agente y back-office, y si clientes y retención
    quedan como topes o solo como «features».
11. [ ] **El matiz del Coordinador en D-35:** el Coordinador es **por conexión** (el modelo de los ADR) y se documenta
    como el agente core del negocio instanciado en cada conexión. Confirmar que eso es lo que llamas «agente core».
12. [ ] **Respaldo del verificador:** `deepseek-v4-pro` u OpenAI.
13. [ ] **Prueba real de `reasoning_content`** (con LLM real): sí o no, y cuándo.
14. [ ] **`verificador_referencias` en el panel:** ¿se expone, y a quién?
15. [ ] **Candidatas de plataforma:** ahora o con [HU-AOS-16](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-16-habilidades-con-procedimientos-y-scope.md).
16. [ ] **Plazo de 72 h:** confirmar (en los docs, 72 h es la muestra mínima del canary de
    [HU-AOS-32](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-32-canary-y-auto-rollback.md)).
17. [ ] **Pago tras cancelar** ([HU-AOS-20](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-20-colaboracion-con-pila-de-tareas.md)).
18. [ ] **Frase legal única** para el abogado.
19. [ ] `calendar_completion_check` (quedó de [HU-ARCH-29](03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-29-verificador-de-afirmaciones.md)):
    confirmar que se mide y se retira en una HU siguiente.

## C · Trámites largos que corren en paralelo

20. [ ] **Meta, en este orden:** verificación del portafolio (enviada el 2026-10-12) → acceso de **Tech Provider** →
    variación **«Registro insertado de WhatsApp»** en Configuraciones de Login for Business → **Embedded Signup de
    `solvershub`** con otra WABA y un número de prueba (`test-embedded-signup-otra-waba-y-numero-de-prueba`,
    `test-aprobacion-de-la-app-de-la-plataforma-en-meta`). Cierra [HU-SH-05](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md)
    y el criterio de Embedded Signup de [HU-CONN-01](03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-01-credenciales-por-conexion.md),
    y destraba las 37 pruebas de WhatsApp del catálogo. Mientras tanto, el Agent OS se prueba por chat web.
21. [ ] **Abogado (HU-GTM-02):**
    términos, privacidad y **DPA** definitivos. Se publican como versión nueva en Tenants → Alta automática, sin tocar
    código. Cierra [HU-SH-07](03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-07-antiabuso-y-cumplimiento.md)
    y es requisito para encender el alta en producción (ADR-0123 § 10, ADR-0125).
22. [ ] **VPS y DNS ([HU-ARCH-01](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md)):**
    contratar el VPS y apuntar el DNS; el runbook `docs/runbooks/produccion-vps.md` de agent-core ya está. Desbloquea
    [HU-ARCH-02](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-02-borde-tls-y-webhook-prod.md) (borde TLS y
    webhook de producción) y [HU-ARCH-03](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-03-backups-pitr-y-restauracion.md)
    (backups y restauración probada).
23. [ ] **Play Console ([HU-APP-17](04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-17-release-firmado-y-guias.md)):**
    cuenta y `eas submit` de la app móvil.
24. [ ] Opcional: `gh auth refresh -s project,read:project` para el GitHub Project.

## D · Producción, solo referenciado

No se trabaja ahora (plan del 2026-10-17, Fase 2.4). Queda una sola lista con referencia:

- **Pestaña «Paso a producción»** del panel de pruebas: los **31 ítems `prod`** del catálogo v6 (infraestructura y
  corte, variables del backend, panel y landing, cuentas externas, app móvil, release y seguridad). Lo que estaba
  aquí en P2 y P3 vive en esos ítems: BYOK de producción real y la app en Live (`prod-meta-app-de-produccion-en-live`,
  `prod-whatsapp-y-meta`), los pendientes de [HU-ARCH-04](03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-04-endurecer-acceso.md),
  el bypass de Access, el secreto de plataforma y la revisión de Security Guidance (`prod-seguridad-antes-del-corte`,
  `prod-tunel-de-cloudflare-y-reglas-de-access-de-produccion`), el WhatsApp de Roshi verificado
  (`prod-whatsapp-de-roshi-verificado`, HU-GTM-03),
  la plantilla de utilidad de producción para el aviso de cobro (`prod-whatsapp-y-meta`), la próxima release
  (`prod-proxima-release-a-produccion`) y el recorrido del criterio de salida del 0A
  (`prod-criterio-de-salida-del-0a-en-produccion`).
- **Runbook post-deploy del Agent OS** (agent-core), a correr en orden en la primera release que lo lleve: el `GRANT`
  manual de la migración 0072 (`purge_tenant` sin superusuario; `docs/despliegue-coolify.md`, «Gotchas conocidos»),
  `agent-core db backfill-conexiones` → `backfill-agentes` → `backfill-releases` (ADR-0113 y ADR-0115),
  `agent-core tenant memoria-importar-perfil` (ADR-0114), `VACUUM` de las tablas que tocan los backfills, y los crons
  de los packs que producción hoy no agenda (core #297).
- **`docs/despliegue-coolify.md`** de agent-core: topología, variables por recurso, secretos y su rotación, y la
  verificación post-despliegue.

## Lo que hace Claude sin ti

- Los PR de los 12 defectos del ciclo (core, panel, landing y APK, con tests) antes de la tanda 6; primero verificar
  la búsqueda y Negocios en el APK vigente.
- El catálogo v7 (claro para cualquiera, áreas Agentes · Superpoderes · Calidad), el informe por sección y las HU-QA
  a `terminada`.
- La tanda 6 del Agent OS ([HU-AOS-15](04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-15-migracion-sin-regresion.md), 16, 17 y 46) con el gate pass^4 cuando des el OK del punto 3.
- El rediseño de la navegación del panel ([D-37](02-vision-y-decisiones/decisiones.md#d-37--menú-v2-del-panel-por-tarea-con-fichas-por-objeto),
  [SPEC-12](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md)): el menú v2
  ([HU-UX-02](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-02-menu-v2.md)) y después las fichas y pestañas
  ([HU-UX-08](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-08-agenda-unificada.md), [HU-UX-09](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-09-ficha-de-conexion-por-tipo.md) y
  [HU-UX-10](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-10-cobranza-y-ventas-en-pestanas.md)) y el cajón de la app
  ([HU-UX-11](04-fase-1-competir/SPEC-12-arquitectura-de-informacion/hu/HU-UX-11-cajon-de-la-app-con-menu-v2.md)).
- Mantener este archivo y la bitácora al cerrar cada tanda.

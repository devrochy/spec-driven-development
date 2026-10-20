# Calendario estimado (D-17)

**Capacidad decidida (D-17)**: 1 persona apoyada por agentes de IA. Las fechas son un **rango**, no un
compromiso, y se recalibran al cerrar cada spec.

## Método

1. **Esfuerzo "sin IA"**: cada HU suma su tamaño en días-persona (S = 1,5 · M = 4 · L = 8), como si la
   hiciera una persona sin asistencia. Los totales salen del frontmatter de las HU
   ([06-backlog-resumen.md](../06-backlog-resumen.md)).
2. **Factor de aceleración con agentes de IA**: la muestra real ya está disponible y es alta; para no
   sobre-estimar se presentan dos escenarios: **4×** (prudente, el mismo del plan) y **10×**
   (anclado en la evidencia pero topado: la muestra son HUs de app y fixes, no infraestructura ni
   trámites externos).
3. **Dedicación**: 4 días efectivos por semana (80 % al roadmap, 20 % a soporte y operación).
4. **Pausa de fin de año**: 2 semanas (2026-12-21 a 2027-01-03), aplicada si el hito la cruza.
5. **Inicio**: ejecución real desde **2026-10-01** (Semana 0); recalibración al 2026-10-07.

### Muestra observada (al 2026-10-07)

| Spec cerrada | Esfuerzo "sin IA" | Días reales | Factor |
|---|---:|---:|---:|
| [SPEC-24](../04-fase-1-competir/SPEC-24-agenda-y-citas/spec.md) Agenda y citas (7 HU) | 40,0 | ~2 | **~20×** |
| [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md) App móvil (19 de 21 HU) | ~112,0 | ~3 | **~37×** |

Son HUs ejecutadas en ráfaga con varios agentes en paralelo; **no** representan el ritmo de
infraestructura, migraciones de datos ni trámites externos. De ahí el tope de 10× hacia adelante.

## Esfuerzo por spec y hito

| Spec | 0A | 0B | Fase 1 | Fase 2 |
|---|---:|---:|---:|---:|
| [SPEC-00](../03-fase-0-go-live/SPEC-00-reestructuracion/spec.md) Reestructuración | 1,5 | 15 | | |
| [SPEC-01](../03-fase-0-go-live/SPEC-01-produccion-segura/spec.md) Producción segura | 23 | 12 | | |
| [SPEC-02](../03-fase-0-go-live/SPEC-02-agente-confiable/spec.md) Agente confiable (incluye [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)/29, D-28) | 23 | 25,5 | | |
| SPEC-03 Billing por créditos | | 33,5 | | |
| [SPEC-04](../03-fase-0-go-live/SPEC-04-notas-de-voz-y-comprobantes/spec.md) Notas de voz y comprobantes | | 25,5 | | |
| [SPEC-05](../03-fase-0-go-live/SPEC-05-presets-y-flujos/spec.md) Presets y flujos | 9,5 | | | |
| SPEC-06 Planes y suscripciones | 31 | 32 | | |
| [SPEC-07](../03-fase-0-go-live/SPEC-07-asistente-solvershub/spec.md) Asistente SolversHub | 52 | 1,5 | | |
| [SPEC-08](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/spec.md) Conexión WhatsApp-Meta | 23 | 13,5 | | |
| [SPEC-09](../03-fase-0-go-live/SPEC-09-comercio-confiable/spec.md) Comercio confiable | 7 | 24 | | |
| [SPEC-10](../03-fase-0-go-live/SPEC-10-panel-confiable/spec.md) Panel confiable | 5,5 | 8 | | |
| SPEC-11 Lanzamiento comercial y legal | 11 | 5,5 | | |
| [SPEC-12](../04-fase-1-competir/SPEC-12-arquitectura-de-informacion/spec.md) a [SPEC-20](../04-fase-1-competir/SPEC-20-crecimiento/spec.md) | | | 240 | |
| [SPEC-24](../04-fase-1-competir/SPEC-24-agenda-y-citas/spec.md) Agenda y citas | | | 40 | |
| [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md) App móvil oficial | | | 120 | |
| [SPEC-21](../05-fase-2-plus/SPEC-21-agencia-e-internacional/spec.md) a [SPEC-23](../05-fase-2-plus/SPEC-23-voz-reportes-y-confianza/spec.md) | | | | 93,5 |
| [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) Agent OS de procedimientos | | | 217,5 | |
| [SPEC-27](../05-fase-2-plus/SPEC-27-agent-os-plus/spec.md) Agent OS Plus | | | | 48 |
| **Total (días-persona sin IA)** | **186,5** | **196** | **613,5** | **141,5** |
| HU | 48 | 48 | 123 | 22 |

La Fase 0 completa suma **382,5 días-persona sin IA**; el plan completo suma **1.137,5** (241 HU), con el Agent OS (D-27; [HU-AOS-35](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-35-cache-por-version.md) bajó de M a S el 2026-10-09).
Al 2026-10-07 están cerradas **35 HU (133 días-persona)** y quedan **159 HU (731 días-persona)**.

## Fechas en rango (desde 2026-10-07, trabajo restante)

| Hito | Días con IA (10× / 4×) | Semanas | Rango de fin (10× – 4×) |
|---|---|---|---|
| **0A** "SolversHub vende y cobra solo" | 15,0 – 37,5 | 3,8 – 9,4 | **2026-11-02 – 2026-12-12** |
| **0B** "Go-live amplio" | 19,5 – 48,6 | 4,9 – 12,2 | **2026-12-06 – 2027-03-21** |
| **Fase 1** "Competir" | 30,1 – 75,3 | 7,5 – 18,8 | **2027-02-11 – 2027-07-31** |
| **Fase 2** "Plus" | 8,6 – 21,4 | 2,1 – 5,3 | **2027-02-26 – 2027-09-06** |

Las fechas son acumuladas: cada hito empieza cuando termina el anterior, y las dos columnas son
**escenarios alternativos** (no se mezclan). La pausa de fin de año ya está aplicada donde corresponde.

## Plazos externos que corren en paralelo

No dependen de cuánto se programe; siguen siendo la ruta crítica real de la segunda mitad del 0A.

| Trámite | Plazo típico | HU que lo espera |
|---|---|---|
| Verificación del negocio de Roshi en Meta | 1–3 semanas | HU-GTM-03, [HU-SH-05](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md) |
| App Review y `config_id` para ser Tech Provider (Embedded Signup) | 2–6 semanas | [HU-SH-05](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-05-embedded-signup-real.md) |
| Aprobación de plantillas de WhatsApp | horas a días por plantilla | [HU-ARCH-13](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-13-plantillas-fuera-de-24h.md), HU-SUB-05 |
| Revisión del abogado (contrato, DPA, términos) | 1–3 semanas | HU-GTM-02 |
| Contratación de la infraestructura de producción (P-01) | días | [HU-ARCH-01](../03-fase-0-go-live/SPEC-01-produccion-segura/hu/HU-ARCH-01-produccion-fuera-de-dev.md) |
| Cuenta de Play Console + publicación | días a semanas | [HU-APP-17](../04-fase-1-competir/SPEC-25-app-movil-oficial/hu/HU-APP-17-release-firmado-y-guias.md) |

Si Meta tarda, el 0A puede cerrarse con **BYOK de producción** ([HU-CONN-06](../03-fase-0-go-live/SPEC-08-conexion-whatsapp-meta/hu/HU-CONN-06-byok-produccion.md)) como alta del primer
cliente y Embedded Signup entra apenas se apruebe (riesgo R-01).

## Cómo reducir el plazo

| Palanca | Efecto |
|---|---|
| Arrancar ya los trámites externos (Meta, abogado, Play Console) | Son la ruta crítica que el factor de IA no acelera |
| Segunda persona (aunque sea medio tiempo) en GTM, legal y trámites con Meta | Saca del desarrollador las HU de GTM del 0A (~11 días-persona) |
| Recortar el 0A a lo estrictamente necesario | Por ejemplo, [HU-SH-06](../03-fase-0-go-live/SPEC-07-asistente-solvershub/hu/HU-SH-06-onboarding-autoservicio.md) (onboarding) con un checklist mínimo y el tour en la Fase 1 |

## Recalibración

Al cerrar cada spec se registra: días reales, factor observado (`esfuerzo sin IA / días reales`) y
desvío. **Primera recalibración (2026-10-07)**: [SPEC-24](../04-fase-1-competir/SPEC-24-agenda-y-citas/spec.md) ~20× y [SPEC-25](../04-fase-1-competir/SPEC-25-app-movil-oficial/spec.md) ~37× (muestra en ráfaga con
agentes en paralelo); hacia adelante se usan 4× y 10× como escenarios. El próximo corte es al cerrar
[SPEC-05](../03-fase-0-go-live/SPEC-05-presets-y-flujos/spec.md) y [SPEC-00](../03-fase-0-go-live/SPEC-00-reestructuracion/spec.md) (bloque del 0A en curso), donde se medirá el factor de
backend/infra y se ajustará el rango.

## Agent OS (D-27 a D-29)

**Esfuerzo**: [HU-ARCH-28](../03-fase-0-go-live/SPEC-02-agente-confiable/hu/HU-ARCH-28-evals-de-consistencia-pass-k.md)/29 dentro del 0A (12 días-persona sin IA, D-28), [SPEC-26](../04-fase-1-competir/SPEC-26-agent-os/spec.md) (225,5, con [HU-AOS-46](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-46-presets-v2.md) de presets v2 y [HU-AOS-47](../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-47-mi-agente-y-su-data.md) «Mi agente y su data», D-35) y [SPEC-27](../05-fase-2-plus/SPEC-27-agent-os-plus/spec.md) (48). Con D-28, el 0A suma de 1,2 a 3 días de trabajo con IA. Por D-29 se muestran dos escenarios de capacidad. El código del Agent OS empieza al terminar el código del 0A, sin esperar el VPS ni al abogado ([D-30](decisiones.md#d-30--el-agent-os-arranca-al-terminar-el-código-del-0a)).

| Escenario | R0a (en el 0A) | R1 + R2 + R3 | 0B | R4 + R5 + R6 | Agent OS v1 vendible |
|---|---|---|---|---|---|
| 1 persona + IA (D-17) · 10× | +1,2 días (fin del 0A ≈ 2026-11-04) | → 2026-11-28 (3,4 sem) | → 2027-01-15 (4,9 sem, cruza la pausa) | → 2027-01-29 (2 sem) | **fin de ene-2027** |
| 1 persona + IA (D-17) · 4× | +3 días (fin del 0A ≈ 2026-12-17) | → 2027-03-01 (8,5 sem + pausa) | → 2027-05-25 (12,2 sem) | → 2027-06-29 (5 sem) | **fin de jun-2027** |
| 3 personas + IA · 10× | Igual | 2 personas en AOS y 1 en el 0B: ≈ 2,2 sem de código + ventanas ≈ 3 sem | En paralelo → 2026-12-09 | Incluido | **dic-2026** |
| 3 personas + IA · 4× | Igual | ≈ 5,4 sem de código + ventanas, con la pausa → ≈ 2027-03-01 | 1 persona → ≈ 2027-03-26 (BILL-05/06 primero) | Incluido | **mar–abr 2027** |

**Ventanas que la IA no comprime:**
- modo sombra del motor (1 semana por negocio piloto);
- modo sombra del enrutamiento (≥ 7 días);
- dogfooding (≥ 14 días + pass^4 tres noches);
- usabilidad con 3 dueños (≈ 1 semana);
- canary (≥ 72 h o 200 conversaciones).

**Más personas:** con más de 3 no se acorta en proporción, porque mandan el camino crítico (≈ 68 días-persona sin IA) y esas ventanas. La segunda y la tercera persona son SUPUESTO A VALIDAR (al cierre del 0A, con una semana de onboarding).


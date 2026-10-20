# Prueba moderada con 5 usuarios · shell del panel y Ctrl+K

> Parte de [SPEC-29](spec.md). Valida la métrica "Llegar a una sección" (mediana ≤ 3 s con Ctrl+K
> frente al menú) y el shell adaptativo de [HU-DS-04](hu/HU-DS-04-shell-adaptativo-del-panel.md)
> (ADR-0003 del panel), que se mergeó sin la variable `PANEL_SHELL_V2` con esta prueba pendiente.
> También cubre la paleta de [HU-DS-05](hu/HU-DS-05-paleta-de-comandos-y-atajos.md).

## Qué queremos saber

1. ¿Se llega más rápido a una sección con Ctrl+K que con el menú? Meta: mediana ≤ 3 s con Ctrl+K.
2. ¿Se entienden la barra lateral plegable, las migas y las pestañas sin explicarlas?
3. ¿Se entiende qué pasa al pausar el asistente antes de confirmar?
4. ¿Qué confunde? (nombres del menú, íconos de la barra plegada, resultados de la búsqueda).

## Participantes

| # | Perfil | Por qué |
|---|---|---|
| 1 | Dueño de un negocio con cobranza | Usuario principal del panel |
| 2 | Dueño de un negocio con comercio o agenda | Otro pack, otro menú |
| 3 | Supervisor o colaborador con permisos parciales | Ve un menú recortado |
| 4 | Operador de atención (bandeja, escalaciones) | Uso intensivo, muchas horas |
| 5 | Alguien que nunca vio el panel | Mide lo que se entiende solo |

Si no hay clientes disponibles, sirve gente del equipo que no haya trabajado en [SPEC-29](spec.md).

## Preparación (30 minutos, una vez)

- Panel de **test** (`test.solvershub.site`) desplegado con `main` (desde `6d087cd` ya trae la paleta).
- Una cuenta de prueba por perfil, con los permisos de su rol. El participante 3 necesita una
  cuenta **sin** permiso de cobranza.
- Negocio de prueba con datos: `Cobranza Demo` tiene a Juana Perez y Pedro Gomez.
- Computador con pantalla de 1280 px o más y un celular para la tarea 8.
- Cronómetro (o grabación de pantalla, con permiso del participante) y esta hoja impresa o abierta.
- Antes de cada sesión: cerrar sesión, borrar la cookie `panel_sidebar` (la barra vuelve al modo
  automático) y dejar los atajos encendidos.

## Guion del moderador (15 minutos por persona)

**Al empezar (1 min):** "Vamos a probar el panel, no a ti. Si algo cuesta, es un problema del panel.
Piensa en voz alta: di lo que buscas y lo que esperas que pase. Yo no voy a ayudarte salvo que te
trabes más de un minuto".

**Reglas:** no señalar la pantalla, no explicar nada hasta la tarea 2, anotar el tiempo desde que
terminas de leer la tarea hasta que la persona llega (o se rinde). Si pasa 1 minuto, se marca
"con ayuda" y se le muestra el camino.

| # | Tarea (léela tal cual) | Éxito cuando | Qué mide |
|---|---|---|---|
| 1 | "Entra a la lista de promesas de pago de cobranza". *(Al participante 3: "a las plantillas de WhatsApp")* | Ve la página Promesas (o Plantillas) | Tiempo con el **menú**, sin explicar nada |
| 2 | Explica en 10 s: "Con Ctrl+K se abre un buscador para ir a cualquier parte". Luego: "Ahora ve a Plantillas de WhatsApp" *(al 3: "a Escalaciones")* | Llega con la paleta | Tiempo con **Ctrl+K** |
| 3 | "Busca a la clienta Juana Perez y abre su ficha" | Ve la ficha de Juana | Búsqueda de registros |
| 4 | "Haz que el menú de la izquierda ocupe menos espacio, y después déjalo como estaba" | Pliega y expande | Descubrir el botón (o `[`) |
| 5 | Desde una cartera: "Vuelve al listado de carteras sin usar el menú" | Usa las migas | Migas |
| 6 | En Calendario › Citas: "Ve a los bloqueos de la agenda" | Usa las pestañas | Pestañas de sección |
| 7 | "Imagina que el asistente está respondiendo mal: detenlo un rato. Antes de confirmar, dime qué crees que va a pasar". Después: "Vuelve a activarlo" | Pausa con la confirmación y lo reactiva | Si la confirmación se entiende |
| 8 | En el celular: "Ve a las conversaciones" | Abre el menú y llega | Cajón móvil |

**Al cerrar (2 min):** "¿Qué fue lo más fácil? ¿Qué fue lo más confuso? ¿Usarías Ctrl+K en tu día
a día?".

Después de la tarea 7, si la persona no lo reactivó, **reactiva el asistente** del negocio de prueba.

## Hoja de registro (una por participante)

Participante: ____ · Perfil: ____ · Fecha: ____

| # | Tiempo (s) | Resultado (solo / con ayuda / no) | Clics equivocados | Facilidad 1–7 | Qué dijo o hizo |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | ¿Qué creyó que iba a pasar? |
| 8 | | | | | |

"Facilidad 1–7" es la pregunta "¿Qué tan fácil fue? 1 = muy difícil, 7 = muy fácil", hecha justo
después de cada tarea.

## Cómo se evalúa

| Qué | Pasa si | Si no pasa |
|---|---|---|
| Ctrl+K (tarea 2) | Mediana ≤ 3 s y menor que la de la tarea 1 | Revisar el orden de resultados y los nombres que buscó la gente |
| Barra plegable (tarea 4) | 4 de 5 la encuentran solos | Hacer más visible el botón del pie o enseñar `[` en el recorrido |
| Migas y pestañas (5 y 6) | 4 de 5 solos | Revisar contraste y tamaño en `PageHeader` |
| Pausa (tarea 7) | 4 de 5 describen bien la consecuencia antes de confirmar | Reescribir el texto de la confirmación |
| Celular (tarea 8) | 5 de 5 | Revisar el botón del menú y el cajón |

Una tarea con facilidad media ≤ 4 se trata como problema aunque la mayoría la complete.

## Después

Pasa las 5 hojas (fotos, planilla o texto) a una sesión de Claude Code: se calculan las medianas,
se agrupan los problemas por frecuencia y gravedad, y se abren las tareas que salgan. El resultado
se anota en la bitácora (sección [SPEC-29](spec.md)) y en ADR-0003, que hoy dice que la prueba está pendiente.

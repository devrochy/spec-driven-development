---
id: HU-DS-10
titulo: Cobranza de campo con el kit nuevo
spec: SPEC-29
fase: 1
hito: "1"
workstream: App móvil
prioridad: P1
critico: false
estimacion: L
impacto: [diferenciacion, confianza]
req: [REQ-APP-11]
dependencias: [HU-DS-09]
skills: ["frontend-design", "/code-review"]
estado: en-curso
---

# HU-DS-10 · Cobranza de campo con el kit nuevo

> Estado SDD: Lista para ejecutar — [SPEC-29](../spec.md) en Diseño aprobado (D-32).

**ID:** HU-DS-10

**Título:** Cobranza de campo con el kit nuevo

**Workstream:** App móvil

**Historia:** Como gestor de campo quiero que la app se vea más clara y legible sin cambiar dónde están las cosas ni cómo registro un pago, para seguir trabajando igual de rápido en la calle.

**Por qué importa (valor empresarial):** La app de campo es el diferencial casi único del producto (D-02). Llevarla al lenguaje del panel sin tocar su flujo la presenta como parte de una sola plataforma y no arriesga la operación de los gestores.

**Prioridad:** P1 competir

**Estimación:** L

**REQ mapeados:** REQ-APP-11

**Dependencias:** [HU-DS-09](HU-DS-09-kit-de-componentes-app.md)

**Criterios de aceptación (Gherkin):**
- **Mismas vistas.** Dado un gestor con dos carteras, cuando entra a la app, entonces el menú lateral muestra Inicio, Carteras, Clientes (con Todos, Al día, En mora y Sin préstamos) y Diario, como antes.
- **Mismo flujo de pago.** Dado un cliente con cuota pendiente y sin conexión, cuando registro un pago, entonces los pasos y las pantallas son los mismos de antes y el pago queda en la cola con el badge "Pendiente".
- **Sincronización visible.** Dado que no hay conexión y hay 3 cambios por enviar, cuando miro el header de campo, entonces el chip dice "Sin conexión · 3 cambios por enviar" y al volver la red cambia solo.
- **Confirmación.** Dado un pago confirmado, cuando termina, entonces veo un toast de éxito y siento un háptico, sin animación si "reducir movimiento" está activo.
- **Sin regresión.** Dado el CI de la app, cuando corre la suite, entonces todos los tests de comportamiento de cobranza siguen verdes sin cambiar sus aserciones de flujo.

**Evidencia / Definición de Terminado:**
- Capturas antes y después de cada vista de la tabla de design.md §5, desde el OPPO.
- Smoke con adb: login → cartera → pago sin conexión → sync.
- Publicación por EAS Update al 10 %, 50 % y 100 % con el registro de cada paso.

**Riesgos/Notas:**
- D-SPEC-29-6 es la regla: ningún cambio de ruta, de orden de pasos ni de lógica. Si aparece una mejora de flujo, va a otra HU.
- `ClienteScreen` tiene 2.547 líneas: se cambian componentes, no se refactoriza la lógica en esta HU.

---
id: HU-UX-13
titulo: Avisos y formularios en español
spec: SPEC-31
fase: 1
hito: "1"
workstream: UX/Onboarding
prioridad: P1
critico: false
estimacion: M
impacto: [confianza, operacion]
req: [REQ-UX-16]
dependencias: [HU-UX-12]
skills: ["panel-ui", "frontend-design", "backend-design:error-handling-as-design"]
estado: borrador
---

# HU-UX-13 · Avisos y formularios en español

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-31](../spec.md). Nace de las notas del dueño en el ciclo de pruebas [2026-10-13](../../../11-pruebas/informes/ciclo-2026-10-13.md) ([D-38](../../../02-vision-y-decisiones/decisiones.md#d-38--spec-31-mejoras-del-ciclo-de-pruebas)).

**ID:** HU-UX-13

**Título:** Avisos y formularios en español

**Workstream:** UX/Onboarding

**Historia:** Como usuario del panel quiero que cada aviso y cada error salga en español, con un ícono que diga si salió bien o mal, y que se cierre solo, para entender qué pasó sin leer jerga técnica.

**Por qué importa (valor empresarial):** El dueño y las testers marcaron avisos en inglés, avisos que no desaparecen y validaciones del navegador en inglés (captura de «Nuevo colaborador»). En un producto para pymes de habla hispana eso se lee como un error del sistema y genera tickets de soporte.

**Prioridad:** P1 competir

**Estimación:** M

**REQ mapeados:** REQ-UX-16

**Dependencias:** [HU-UX-12](HU-UX-12-arreglos-rapidos-del-ciclo.md)

**Criterios de aceptación (Gherkin):**
- **Aviso con ícono que se cierra.** Dado que guardo un formulario, cuando sale bien o sale mal, entonces veo un aviso con el ícono de su tipo (éxito, información, advertencia o error) que se cierra solo y que también puedo cerrar.
- **Error del servidor en español.** Dado que el servidor responde con un error que trae un mensaje en inglés, cuando el panel lo muestra, entonces veo un texto en español según su código, y nunca el mensaje en inglés.
- **Validación en español.** Dado el campo Correo de «Nuevo colaborador», cuando escribo «ana@» y guardo, entonces veo junto al campo «Escribe un correo completo, por ejemplo ana@negocio.com» y no la burbuja del navegador en inglés.
- **Ayuda de un campo.** Dado un campo con ícono de ayuda, cuando lo enfoco con el teclado o lo toco en el celular, entonces veo su explicación completa.
- **Vincular un dispositivo.** Dado que intento vincular un IMEI o un WhatsApp de gestor que no se puede vincular, cuando guardo, entonces el aviso dice por qué (ya vinculado, gestor inactivo, formato inválido) y qué hacer.

**Evidencia / Definición de Terminado:**
- `lib/toast-store.ts` y `components/ui/toaster.tsx` con 4 tipos; el error dura 8 s y tiene botón de cerrar.
- `lib/api/errores.ts`: mapa `código → mensaje` con fallback; `lib/api/server.ts` deja de pasar el `message` en inglés.
- `noValidate` y validación propia con `ui/field.tsx` en todos los formularios (hoy solo 3 tienen `noValidate`); test que recorre los formularios buscando textos en inglés.
- Avisos dentro de la página pasados a toast, empezando por Conexiones, Plantillas, Configuración y Colaboradores.
- Core: códigos de error estables en el flujo de vinculación de dispositivos de pack_cobranza, con su mensaje.

**Riesgos/Notas:**
- Notas que lo motivan: ítems 8, 9 y 10 del [inventario de SPEC-31](../design.md#inventario).
- Depende del tooltip con portal de [HU-UX-12](HU-UX-12-arreglos-rapidos-del-ciclo.md).

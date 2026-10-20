---
id: HU-AOS-39
titulo: "Federación entre negocios con consentimiento"
spec: SPEC-27
fase: 2
hito: "2"
workstream: Agent OS
prioridad: P2
critico: false
estimacion: L
impacto: [diferenciacion, ingreso]
req: [REQ-AOS-09]
dependencias: [HU-AOS-18, HU-AOS-37]
skills: ["backend-design:security-discipline", "auditor-multitenant", "backend-design:auth-and-authorization"]
estado: borrador
---

# HU-AOS-39 · Federación entre negocios con consentimiento

> Estado SDD: Borrador — sujeta a aprobación de [SPEC-27](../spec.md).

**ID:** HU-AOS-39

**Título:** Federación entre negocios con consentimiento

**Workstream:** Agent OS

**Historia:** Como negocio quiero permitir que un aliado consulte uno de mis agentes con mi consentimiento explícito y revocable, para colaborar sin compartir mis datos.

**Por qué importa (valor empresarial):** Abre un marketplace de agentes sin romper el aislamiento entre negocios.

**Prioridad:** P2 plus

**Estimación:** L

**REQ mapeados:** REQ-AOS-09

**Dependencias:** [HU-AOS-18](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-18-permisos-limites-y-ledger-a2a.md), [HU-AOS-37](../../../04-fase-1-competir/SPEC-26-agent-os/hu/HU-AOS-37-cuotas-y-planes.md)

**Criterios de aceptación (Gherkin):**
- **Doble consentimiento.** Dado una propuesta de federación, cuando solo una de las partes la aprueba, entonces sigue en `proposed` y no se puede usar.
- **Revocación.** Dado una federación activa, cuando una parte la revoca, entonces la siguiente llamada se deniega de inmediato.
- **Sin datos ajenos.** Dado una consulta federada, cuando se responde, entonces el consumidor solo recibe el resultado tipado y nunca memoria ni estado del proveedor.

**Evidencia / Definición de Terminado:**
- `a2a_federation_grants`; funciones SECURITY DEFINER; gateway de federación; `purge_tenant` extendido; tests de aislamiento.

**Riesgos/Notas:**
- Diferir hasta tener 2 interesados reales (P-15).

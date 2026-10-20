# SPEC-05 · Diseño

## Flujo compuesto

```
flow efectivo = core (saludo, escalamiento, memoria; siempre disponibles)
              + secciones de cada pack habilitado (namespace pack_x:...)
              + secciones "tenant" (propias del negocio; nunca las toca un re-seed)
```

- Las tools del core marcadas `always_available` se ofrecen aunque no estén en ninguna sección
  (memoria, perfil del cliente, escalamiento, correo). Las del core con predicado (`sub_*` de
  HU-SUB-01: solo con un proveedor de suscripciones habilitado) se ofrecen cuando su predicado lo permite.
- `saludo` y `escalamiento` existen una sola vez (core); los packs no los redefinen.
- El re-seed reemplaza solo las secciones del pack que se re-siembra, por ID con espacio de nombres.
- Migración: los flujos existentes se convierten; las secciones propias del tenant `solvershub`
  etiquetadas `pack_commerce` pasan a `tenant`.
- El `flow.json` del negocio deja de ser autoritativo sobre los packs: guarda solo las secciones
  `tenant` (y overrides explícitos); las de los packs habilitados se componen siempre, así un pack
  que se activa después aporta sus secciones.

**Estado del código al aprobar (2026-10-08, `develop`):** con un flujo declarado,
`core/orchestrator/loop.py` ofrece solo las tools listadas en él (quedan fuera
`update_customer_profile`, `remember_fact`, `send_email` y las `sub_*`); `saludo` existe en
`pack_commerce` y `pack_cobranza` y `_dedupe_sections` se queda con la primera por orden alfabético
(un negocio con ambos pierde `crear_lead`, `consultar_inventario`…); el `flow.json` del tenant es
autoritativo; `seed_tenant_flow` decide qué pisar por el campo `pack`.

## Presets (D-SPEC-05-1 = B: fragmentos por pack + manifiesto)

**Fragmentos que declara cada pack** (versionados con el pack):

- `flow.json`: sus secciones, con IDs `pack_x:...`;
- `seed_data(tenant, vertical)`: datos de ejemplo por vertical, idempotente;
- `default_config(vertical)`: config por defecto sin secretos (umbrales, campos de checkout…).

**Manifiesto del preset** (`core/presets/<vertical>.json`): solo referencias, sin copiar nada de
los packs y sin prompts:

```json
{
  "id": "restaurante", "version": 1, "plan_minimo": "basic",
  "packs": ["pack_commerce", "pack_payments"],
  "playbooks": ["ventas", "pagos"],
  "persona": {"tono": "calido", "split_style": "un_mensaje"},
  "conexiones_requeridas": ["whatsapp"],
  "pasos_de_activacion": ["conectar_whatsapp", "cargar_catalogo", "configurar_pagos"],
  "golden_set": "restaurante-base"
}
```

```
core/presets/
├── comercio.json
├── restaurante.json
├── cobranza.json
└── planes-y-suscripciones.json   (lo agrega HU-SUB-11)
```

`apply_preset(tenant, preset, version)`:

1. Valida que los packs existen y que el plan del negocio los permite.
2. Habilita los packs; los que exigen claves (payments) quedan **pendientes de configurar**, sin
   fallar el alta.
3. Escribe la config por defecto de cada pack (`default_config(vertical)`, sin secretos).
4. Llama `seed_data(tenant, vertical)` de cada pack (idempotente).
5. Compone el flujo (fragmentos de los packs + secciones `tenant`) y crea una versión nueva del AgentSpec.
6. Registra en `audit_log` el preset y su versión.

CLI: `agent-core tenant create --preset restaurante` (`solvershub` tras el renombre de [HU-REP-02](../SPEC-00-reestructuracion/hu/HU-REP-02-renombre-cosmetico.md)). El consumidor de aprovisionamiento ([HU-SH-03](../SPEC-07-asistente-solvershub/hu/HU-SH-03-aprovisionamiento-automatico.md))
llama a la misma función.

## ADR

- **ADR "Presets de agente"**: manifiesto y fragmentos por pack, versionado, aplicación, relación con `flow.json` y AgentSpec.
- **Enmienda a ADR-0054** ([HU-FWK-01](hu/HU-FWK-01-composicion-de-flujos.md)): IDs con namespace, secciones `tenant`, tools del core siempre disponibles o por predicado, flujo del negocio no autoritativo sobre los packs.

## Riesgos

| Riesgo | Mitigación |
|---|---|
| Migrar flujos rompe un negocio en producción | Migración con diff revisado por negocio y evals antes y después |

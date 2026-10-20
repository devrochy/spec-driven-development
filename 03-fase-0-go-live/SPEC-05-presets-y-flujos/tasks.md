# SPEC-05 · Tareas

| Orden | HU | Título | Tamaño | Depende de | Hito |
|---|---|---|---|---|---|
| 1 | [HU-FWK-01](hu/HU-FWK-01-composicion-de-flujos.md) ★ | Composición de flujos | M | — | 0A |
| 2 | [HU-FWK-02](hu/HU-FWK-02-adr-presets.md) ★ | ADR de presets | S | [HU-FWK-01](hu/HU-FWK-01-composicion-de-flujos.md) | 0A |
| 3 | [HU-FWK-03](hu/HU-FWK-03-registro-de-presets-y-seeds.md) ★ | Registro de presets y seeds | M | [HU-FWK-02](hu/HU-FWK-02-adr-presets.md) | 0A |

**Esfuerzo**: 1 S + 2 M ≈ 9,5 días-persona sin IA.

```mermaid
graph LR
  F01[HU-FWK-01 ★] --> F02[HU-FWK-02 ★] --> F03[HU-FWK-03 ★]
```

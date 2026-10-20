#!/usr/bin/env python3
"""Valida y regenera las partes generadas de solvershub-docs.

Uso (desde la raíz del repo):
    python3 herramientas/regenerar.py           # valida, regenera y enlaza
    python3 herramientas/regenerar.py --check   # solo valida (para CI); no escribe nada

Qué hace:
1. Valida cada HU: frontmatter (estado borrador | en-curso | terminada | parqueada), los 12 campos en orden, ID = archivo, REQ existentes,
   dependencias existentes, sin ciclos, nunca hacia una fase posterior, el Hito 0A solo
   depende del 0A, al menos 2 escenarios Gherkin con Dado/cuando/entonces.
2. Valida `tasks.md` de cada spec contra sus HU (lista, tamaños, dependencias, esfuerzo).
3. Valida que cada REQ del catálogo tenga al menos una HU (salvo cerrados o absorbidos).
4. Valida que cada decisión (D-…, P-…) tenga tabla de opciones con pros y contras y una recomendación.
5. Valida las skills recomendadas de cada HU contra `herramientas/catalogo-skills.yml` y que cada
   HU del Hito 0A tenga ola (1–4) y solo dependa de su ola o de una anterior.
5b. Valida el catálogo de pruebas `11-pruebas/catalogo.yaml`: versión, ids únicos, campos por sección,
   pasos (texto o `{accion, esperado}`) y que las HU citadas existan.
6. Regenera `06-backlog-resumen.md`, las tablas de los README de fase y las secciones generadas de
   `07-guia-de-ejecucion.md` (catálogo de skills y checklists de HU), todas entre marcadores. Las HU
   `parqueadas` se cuentan y listan aparte: no suman al calendario ni a los totales de pendientes.
7. Convierte menciones de HU-XXX-NN y SPEC-NN en enlaces relativos.
8. Verifica que todos los enlaces relativos y anclas resuelvan.

Dependencia: PyYAML (`pip install pyyaml`).
"""
from __future__ import annotations

import collections
import os
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
# Carpetas que no son del plan: dependencias de herramientas (OpenCode instala las de sus
# plugins en `.opencode/node_modules`) y entornos virtuales. Sus .md no se validan ni se tocan.
IGNORED_DIRS = {"node_modules", ".git", ".venv", ".venv-ci"}
LABELS = [
    "**ID:**", "**Título:**", "**Workstream:**", "**Historia:**",
    "**Por qué importa (valor empresarial):**", "**Prioridad:**", "**Estimación:**",
    "**REQ mapeados:**", "**Dependencias:**", "**Criterios de aceptación (Gherkin):**",
    "**Evidencia / Definición de Terminado:**", "**Riesgos/Notas:**",
]
WORKSTREAMS = {
    "Billing", "Framework/Plugins", "UX/Onboarding", "Flujo visual", "Arquitectura/Prod",
    "Multimodalidad", "GTM", "Comercio y suscripciones", "Canales y conexiones", "Asistente SolversHub",
    "Agenda", "App móvil", "Agent OS", "Verticales",
}
IMPACTO = {"ingreso": "💰", "confianza": "🛡️", "operacion": "⚙️", "diferenciacion": "🏆",
           "legal": "⚖️", "calidad_ia": "🤖"}
DIAS = {"S": 1.5, "M": 4.0, "L": 8.0}
HITOS = {"0A": "SolversHub vende y cobra solo", "0B": "Go-live amplio", "1": "Competir", "2": "Plus"}
# `parqueada` (D-35): la HU conserva su texto pero sale del calendario y de los totales de pendientes.
ESTADOS = {"borrador", "en-curso", "terminada", "parqueada"}

errors: list[str] = []
CATALOGO: dict = yaml.safe_load((ROOT / "herramientas/catalogo-skills.yml").read_text(encoding="utf-8"))


def num(x: float) -> str:
    return f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")


def parqueada(h: dict) -> bool:
    return h.get("estado") == "parqueada"


# ---------------------------------------------------------------- carga

def load_hus() -> dict:
    hus = {}
    for p in sorted(ROOT.glob("0[345]-*/SPEC-*/hu/HU-*.md")):
        text = p.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
        if not m:
            errors.append(f"{p.relative_to(ROOT)}: sin frontmatter")
            continue
        fm = yaml.safe_load(m.group(1))
        fm["_path"], fm["_body"], fm["hito"] = p, m.group(2), str(fm.get("hito"))
        hid = fm.get("id")
        if not p.name.startswith(f"{hid}-"):
            errors.append(f"{p.name}: el id {hid} no coincide con el archivo")
        if hid in hus:
            errors.append(f"{hid}: id duplicado")
        hus[hid] = fm
    return hus


def load_reqs() -> dict:
    text = (ROOT / "02-vision-y-decisiones/requerimientos.md").read_text(encoding="utf-8")
    return {m.group(1): line for line in text.splitlines()
            if (m := re.match(r"\| (REQ-[A-Z]+-\d+b?) \|", line))}


def spec_dirs() -> dict:
    return {"-".join(d.name.split("-")[:2]): d for d in ROOT.glob("0[345]-*/SPEC-*")}


# ---------------------------------------------------------------- validación

def validate_hus(hus: dict, reqs: dict) -> None:
    specs = spec_dirs()
    for hid, h in hus.items():
        body = h["_body"]
        pos = -1
        for lab in LABELS:
            i = body.find(lab)
            if i < 0:
                errors.append(f"{hid}: falta el campo {lab}")
            elif i < pos:
                errors.append(f"{hid}: el campo {lab} está fuera de orden")
            pos = max(pos, i)
        for k in ("titulo", "spec", "fase", "hito", "workstream", "prioridad", "critico",
                  "estimacion", "impacto", "req", "dependencias", "estado"):
            if k not in h:
                errors.append(f"{hid}: frontmatter sin {k}")
        if h.get("estado") not in ESTADOS:
            errors.append(f"{hid}: estado desconocido {h.get('estado')} (opciones: {', '.join(sorted(ESTADOS))})")
        if h.get("workstream") not in WORKSTREAMS:
            errors.append(f"{hid}: workstream desconocido {h.get('workstream')}")
        if h.get("estimacion") not in DIAS:
            errors.append(f"{hid}: estimación inválida {h.get('estimacion')}")
        for imp in h.get("impacto", []):
            if imp not in IMPACTO:
                errors.append(f"{hid}: impacto desconocido {imp}")
        if h.get("prioridad") != f"P{h['fase']}":
            errors.append(f"{hid}: prioridad {h.get('prioridad')} no coincide con la fase {h['fase']}")
        if h["fase"] == 0 and h["hito"] not in ("0A", "0B"):
            errors.append(f"{hid}: hito {h['hito']} inválido para la fase 0")
        if h["fase"] in (1, 2) and h["hito"] != str(h["fase"]):
            errors.append(f"{hid}: hito {h['hito']} inválido para la fase {h['fase']}")
        if h["fase"] > 0 and h.get("critico"):
            errors.append(f"{hid}: solo la fase 0 lleva camino crítico")
        if h["spec"] not in specs or h["_path"].parent.parent != specs[h["spec"]]:
            errors.append(f"{hid}: no está en la carpeta de {h['spec']}")
        m = re.search(r"\*\*Título:\*\* (.+)", body)
        if m and m.group(1).strip() != h["titulo"]:
            errors.append(f"{hid}: título distinto en frontmatter y cuerpo")
        if not h.get("req"):
            errors.append(f"{hid}: no mapea ningún REQ")
        for r in h.get("req", []):
            if r not in reqs:
                errors.append(f"{hid}: REQ inexistente {r}")
        line = re.search(r"\*\*REQ mapeados:\*\* (.+)", body)
        if line and sorted(set(re.findall(r"REQ-[A-Z]+-\d+b?", line.group(1)))) != sorted(h.get("req", [])):
            errors.append(f"{hid}: REQ del cuerpo distintos del frontmatter")
        line = re.search(r"\*\*Dependencias:\*\* (.+)", body)
        body_deps = sorted(set(re.findall(r"HU-[A-Z]+-\d+", line.group(1)))) if line else []
        if body_deps != sorted(h.get("dependencias", [])):
            errors.append(f"{hid}: dependencias del cuerpo distintas del frontmatter")
        for d in h.get("dependencias", []):
            if d not in hus:
                errors.append(f"{hid}: depende de {d}, que no existe")
                continue
            if hus[d]["fase"] > h["fase"]:
                errors.append(f"{hid} (fase {h['fase']}) depende de {d} (fase {hus[d]['fase']})")
            if h["hito"] == "0A" and hus[d]["hito"] != "0A":
                errors.append(f"{hid} (0A) depende de {d} ({hus[d]['hito']})")
        crit = body.split("**Criterios de aceptación (Gherkin):**")[-1].split("**Evidencia")[0]
        escenarios = [l for l in crit.splitlines() if l.startswith("- ")]
        if len(escenarios) < 2:
            errors.append(f"{hid}: menos de 2 escenarios Gherkin")
        for l in escenarios:
            if not ("Dado" in l and "cuando" in l and "entonces" in l):
                errors.append(f"{hid}: escenario sin Dado/cuando/entonces: {l[:60]}")
        skills = h.get("skills")
        if not skills:
            errors.append(f"{hid}: sin skills recomendadas")
        for sk in skills or []:
            if sk not in CATALOGO:
                errors.append(f"{hid}: skill desconocida {sk} (agrégala a herramientas/catalogo-skills.yml)")
        if h["hito"] == "0A":
            if h.get("ola") not in (1, 2, 3, 4):
                errors.append(f"{hid}: el Hito 0A exige ola 1–4")
            for d in h.get("dependencias", []):
                if d in hus and hus[d].get("ola", 9) > h.get("ola", 0):
                    errors.append(f"{hid} (ola {h.get('ola')}) depende de {d} (ola {hus[d].get('ola')})")
        elif "ola" in h:
            errors.append(f"{hid}: solo las HU del Hito 0A llevan ola")
    state: dict = {}

    def visit(n, stack):
        if state.get(n) == 1:
            errors.append("ciclo: " + " -> ".join(stack + [n]))
            return
        if state.get(n) == 2:
            return
        state[n] = 1
        for d in hus[n].get("dependencias", []):
            if d in hus:
                visit(d, stack + [n])
        state[n] = 2

    for n in hus:
        visit(n, [])


def validate_reqs(hus: dict, reqs: dict) -> None:
    covered = collections.defaultdict(list)
    for hid, h in hus.items():
        for r in h.get("req", []):
            covered[r].append(hid)
    for r, line in reqs.items():
        if r not in covered and "✅" not in line and "⤵" not in line:
            errors.append(f"{r}: ninguna HU lo cubre")
        for hid in set(re.findall(r"HU-[A-Z]+-\d+", line)):
            if hid not in hus:
                errors.append(f"{r}: el catálogo cita {hid}, que no existe")


def validate_tasks(hus: dict) -> None:
    by_spec = collections.defaultdict(list)
    for h in hus.values():
        by_spec[h["spec"]].append(h)
    for spec, d in spec_dirs().items():
        for f in ("spec.md", "design.md", "tasks.md"):
            if not (d / f).exists():
                errors.append(f"{d.name}: falta {f}")
        t = d / "tasks.md"
        if not t.exists():
            continue
        text = t.read_text(encoding="utf-8")
        listed = set(re.findall(r"^\| \d+ \| \[?(HU-[A-Z]+-\d+)", text, re.M))
        actual = {h["id"] for h in by_spec[spec]}
        if listed != actual:
            errors.append(f"{d.name}/tasks.md: diferencia con las HU {sorted(listed ^ actual)}")
        total = sum(DIAS[h["estimacion"]] for h in by_spec[spec])
        m = re.search(r"≈ ([\d,]+) días-persona", text)
        if m and abs(float(m.group(1).replace(",", ".")) - total) > 0.01:
            errors.append(f"{d.name}/tasks.md: esfuerzo {m.group(1)} ≠ {num(total)}")
        for hid, est, deps in re.findall(r"^\| \d+ \| \[?(HU-[A-Z]+-\d+)[^|]*\|[^|]*\| ([SML]) \| ([^|]*) \|", text, re.M):
            if hid in hus:
                if hus[hid]["estimacion"] != est:
                    errors.append(f"{d.name}/tasks.md: {hid} tamaño {est} ≠ {hus[hid]['estimacion']}")
                if sorted(set(re.findall(r"HU-[A-Z]+-\d+", deps))) != sorted(hus[hid].get("dependencias", [])):
                    errors.append(f"{d.name}/tasks.md: dependencias de {hid} distintas de la HU")


def validate_decisions() -> None:
    files = list(ROOT.glob("0[345]-*/SPEC-*/spec.md")) + [
        ROOT / "02-vision-y-decisiones/decisiones.md", ROOT / "02-vision-y-decisiones/preguntas-abiertas.md"]
    for f in files:
        text = f.read_text(encoding="utf-8")
        if f.name == "spec.md" and "## Decisiones" not in text:
            errors.append(f"{f.relative_to(ROOT)}: sin sección de decisiones")
        heads = list(re.finditer(r"^###? (?:D-[A-Z0-9-]+|P-\d+)[^\n]*$", text, re.M))
        for i, h in enumerate(heads):
            body = text[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(text)]
            rows = [l for l in body.splitlines() if l.startswith("| ") and not l.startswith(("| Opción", "|---"))]
            if "| Opción | Pros | Contras |" not in body or len(rows) < 2:
                errors.append(f"{f.relative_to(ROOT)}: {h.group(0)[:60]} sin tabla de opciones con pros y contras")
            if "Recomendación" not in body and "elegida" not in body:
                errors.append(f"{f.relative_to(ROOT)}: {h.group(0)[:60]} sin recomendación")


CATALOGO_PRUEBAS = ROOT / "11-pruebas/catalogo.yaml"
QA_SECCIONES = {"pruebas", "test", "prod", "datos"}
QA_MODULOS = {"Panel", "App móvil", "App de campo", "Cobranza", "Asistente y WhatsApp", "Cobros y suscripciones", "Comercio",
              "Agenda", "Plataforma", "Landing"}
QA_PLATAFORMAS = {"panel", "app", "whatsapp", "web", "api", "correo"}
QA_PRIORIDADES = {"P0", "P1", "P2"}
# Desde la v6 (HU-QA-08): dónde se ejecuta cada prueba y en qué sección. Las del panel siguen su menú; las de la
# APK, sus pantallas. El orden de cada lista es el de la lista lateral del centro de pruebas.
QA_AREAS = {
    "panel": ["Navegación y sesión", "Formularios y avisos", "Kit visual", "Primeros pasos", "Resumen", "Agentes",
              "Conversaciones", "Escalaciones", "Leads", "Conexiones", "Habilidades", "Colaboradores", "Configuración",
              "Costos", "Plan y consumo", "Cobranza", "Comercio", "Calendario", "Herramientas", "Negocios", "Pruebas",
              "Seguridad y calidad"],
    "apk": ["Sesión y permisos", "Inicio y búsqueda", "Conversaciones", "Notificaciones", "Negocio y configuración",
            "Comercio", "Agenda", "Cobranza del dueño", "Campo (gestor)"],
    "whatsapp": ["Asistente", "Ventas de SolversHub", "Alta automática", "Suscripciones", "Comercio", "Agenda",
                 "Operación"],
    "web": ["Landing", "Chat web"],
    "api": ["Seguridad", "Operación"],
}


def validate_test_catalog(hus: dict) -> int:
    """Valida `11-pruebas/catalogo.yaml` (esquema v1 y v2). Devuelve el número de ítems."""
    if not CATALOGO_PRUEBAS.exists():
        return 0
    rel = CATALOGO_PRUEBAS.relative_to(ROOT)
    data = yaml.safe_load(CATALOGO_PRUEBAS.read_text(encoding="utf-8")) or {}
    if not isinstance(data.get("version"), int):
        errors.append(f"{rel}: falta `version` entera")
    if not data.get("fecha"):
        errors.append(f"{rel}: falta `fecha`")
    items = data.get("items") or []
    v6 = isinstance(data.get("version"), int) and data["version"] >= 6
    guia = {it.get("id") for it in items if it.get("seccion") == "datos"}
    vistos: set = set()
    for n, it in enumerate(items):
        iid = it.get("id") or f"#{n}"
        donde = f"{rel}: {iid}"
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", str(it.get("id", ""))):
            errors.append(f"{donde}: id ausente o con caracteres no permitidos (minúsculas, números y guiones)")
        if iid in vistos:
            errors.append(f"{donde}: id duplicado")
        vistos.add(iid)
        sec = it.get("seccion")
        if sec not in QA_SECCIONES:
            errors.append(f"{donde}: seccion {sec!r} inválida")
            continue
        for k in ("grupo", "titulo"):
            if not it.get(k):
                errors.append(f"{donde}: falta {k}")
        if sec == "pruebas":
            pasos = it.get("pasos")
            if not isinstance(pasos, list) or not pasos:
                errors.append(f"{donde}: una prueba necesita `pasos`")
                pasos = []
            sin_esperado = False
            for i, paso in enumerate(pasos, 1):
                if isinstance(paso, str):
                    sin_esperado = True
                elif isinstance(paso, dict):
                    if not paso.get("accion"):
                        errors.append(f"{donde}: el paso {i} no tiene `accion`")
                    if not paso.get("esperado"):
                        sin_esperado = True
                    extra = set(paso) - {"accion", "esperado"}
                    if extra:
                        errors.append(f"{donde}: el paso {i} tiene campos desconocidos {sorted(extra)}")
                else:
                    errors.append(f"{donde}: el paso {i} debe ser texto o {{accion, esperado}}")
            if sin_esperado and not it.get("esperado"):
                errors.append(f"{donde}: sin `esperado` general y con pasos sin resultado esperado")
            for h in it.get("hu") or []:
                if h not in hus:
                    errors.append(f"{donde}: cita {h}, que no existe")
            if it.get("modulo") and it["modulo"] not in QA_MODULOS:
                errors.append(f"{donde}: modulo {it['modulo']!r} inválido")
            if it.get("prioridad") and it["prioridad"] not in QA_PRIORIDADES:
                errors.append(f"{donde}: prioridad {it['prioridad']!r} inválida")
            plat = it.get("plataforma") or []
            for pl in [plat] if isinstance(plat, str) else plat:
                if pl not in QA_PLATAFORMAS:
                    errors.append(f"{donde}: plataforma {pl!r} inválida")
            entorno, area = it.get("entorno"), it.get("area")
            if v6 and not (entorno and area):
                errors.append(f"{donde}: desde la v6 cada prueba lleva `entorno` y `area`")
            if entorno and entorno not in QA_AREAS:
                errors.append(f"{donde}: entorno {entorno!r} inválido (opciones: {', '.join(QA_AREAS)})")
            elif entorno and area and area not in QA_AREAS[entorno]:
                errors.append(f"{donde}: area {area!r} no existe en el entorno {entorno}")
            for r in it.get("requiere") or []:
                if r not in guia:
                    errors.append(f"{donde}: requiere {r!r}, que no está en la sección datos")
        else:
            for k in ("porque", "como"):
                if not it.get(k):
                    errors.append(f"{donde}: falta {k}")
    return len(items)


# ---------------------------------------------------------------- generación

def longest_chain(hus: dict, subset: set) -> tuple[float, list]:
    memo: dict = {}

    def walk(n):
        if n not in memo:
            best = (0.0, [])
            for d in sorted(hus[n].get("dependencias", [])):
                if d in subset and walk(d)[0] > best[0]:
                    best = walk(d)
            memo[n] = (best[0] + DIAS[hus[n]["estimacion"]], best[1] + [n])
        return memo[n]

    # orden fijo para que los empates den siempre el mismo resultado
    return max((walk(n) for n in sorted(subset)), key=lambda x: x[0])


def sort_key(h):
    return ({"0A": 0, "0B": 1, "1": 2, "2": 3}[h["hito"]], h["spec"], h["id"].split("-")[1], int(h["id"].split("-")[-1]))


def hu_table(hus_list, base: pathlib.Path, with_meta: bool) -> list[str]:
    if with_meta:
        rows = ["| ID | Título | Workstream | Prioridad | Est. | Dependencias | Hito | Spec | Impacto |",
                "|---|---|---|---|---|---|---|---|---|"]
    else:
        rows = ["| HU | Título | Est. | Depende de | Impacto |", "|---|---|---|---|---|"]
    for h in sorted(hus_list, key=sort_key):
        link = f"[{h['id']}]({os.path.relpath(h['_path'], base)})" + (" ★" if h.get("critico") else "")
        deps = ", ".join(h.get("dependencias", [])) or "—"
        imps = " ".join(IMPACTO[i] for i in h.get("impacto", []))
        if with_meta:
            rows.append(f"| {link} | {h['titulo']} | {h['workstream']} | {h['prioridad']} | {h['estimacion']} | {deps} | {h['hito']} | {h['spec']} | {imps} |")
        else:
            rows.append(f"| {link} | {h['titulo']} | {h['estimacion']} | {deps} | {imps} |")
    return rows


def mermaid(hus_list) -> list[str]:
    ids = {h["id"] for h in hus_list}
    out = ["```mermaid", "graph LR"]
    for h in sorted(hus_list, key=lambda x: x["id"]):
        out.append(f"  {h['id'].replace('-', '_')}[\"{h['id']}{' ★' if h.get('critico') else ''}\"]")
    for h in sorted(hus_list, key=lambda x: x["id"]):
        for d in h.get("dependencias", []):
            if d in ids:
                out.append(f"  {d.replace('-', '_')} --> {h['id'].replace('-', '_')}")
    out.append("```")
    return out


def write_backlog(hus: dict) -> None:
    total, dias, imp, ws = collections.Counter(), collections.Counter(), collections.Counter(), collections.defaultdict(collections.Counter)
    parq, parq_dias = collections.Counter(), collections.Counter()
    for h in hus.values():
        if parqueada(h):
            parq[h["hito"]] += 1
            parq_dias[h["hito"]] += DIAS[h["estimacion"]]
            continue
        total[h["hito"]] += 1
        dias[h["hito"]] += DIAS[h["estimacion"]]
        ws[h["workstream"]][h["hito"]] += 1
        for i in h.get("impacto", []):
            imp[i] += 1
    a = {k for k, h in hus.items() if h["hito"] == "0A" and not parqueada(h)}
    f0 = {k for k, h in hus.items() if h["fase"] == 0 and not parqueada(h)}
    ca, c0 = longest_chain(hus, a), longest_chain(hus, f0)
    L = ["# 06 · Backlog resumen", "",
         "> Generado por `herramientas/regenerar.py` desde el frontmatter de las HU. No se edita a mano.", "",
         "## Resumen por hito", "", "| Hito | Qué significa | HU | Días-persona sin IA | Parqueadas (fuera del calendario) |",
         "|---|---|---:|---:|---:|"]
    for k, name in HITOS.items():
        L.append(f"| {k} | {name} | {total[k]} | {num(dias[k])} | {parq[k]} ({num(parq_dias[k])}) |")
    L += [f"| **Total** | | **{sum(total.values())}** | **{num(sum(dias.values()))}** | **{sum(parq.values())}** ({num(sum(parq_dias.values()))}) |", "",
          "Las HU `parqueadas` (D-35) conservan su texto pero no suman al calendario ni a los totales de pendientes; "
          "se listan aparte al final y se retoman por decisión.", "",
          "## Impacto empresarial", "",
          "💰 ingreso · 🛡️ confianza y seguridad · ⚙️ operación · 🏆 diferenciación competitiva · ⚖️ legal y cumplimiento · 🤖 calidad de la IA", "",
          "| Impacto | HU que lo aportan |", "|---|---:|"]
    nombres = {"ingreso": "ingreso", "confianza": "confianza", "operacion": "operación", "diferenciacion": "diferenciación",
               "legal": "legal", "calidad_ia": "calidad de la IA"}
    for k, e in IMPACTO.items():
        L.append(f"| {e} {nombres[k]} | {imp[k]} |")
    L += ["", "## Camino crítico", "",
          f"- **Hito 0A** (cadena más larga de dependencias, {num(ca[0])} días-persona sin IA): " + " → ".join(ca[1]),
          f"- **Fase 0 completa** ({num(c0[0])} días-persona sin IA): " + " → ".join(c0[1]), "",
          "El camino crítico es el mínimo de calendario aunque sobre capacidad; con una sola persona manda el "
          "esfuerzo total. Fechas en [calendario-estimado.md](02-vision-y-decisiones/calendario-estimado.md).", "",
          "## Milestones y criterio de salida", "", "| Milestone | Criterio de salida medible |", "|---|---|",
          "| **Fase 0 · Hito 0A** \"SolversHub vende y cobra solo\" | Un prospecto real agenda una demo, compra un plan, paga (Free sin cobro), su negocio se crea solo con invitación, conecta WhatsApp por Embedded Signup y recibe el cobro del período siguiente con aviso por plantilla, sin intervención humana y con evidencia auditada. Golden E2E del asistente ≥95 % durante 3 noches. Producción fuera de la máquina de desarrollo con restauración probada. Ningún defecto 🔴 abierto en suscripciones, comercio o Conexiones |",
          "| **Fase 0 · Hito 0B** \"Go-live amplio\" | 1 cliente de pago de comercio y 1 de cobranza en producción. Alta en menos de 1 día. Créditos descontando y bloqueando de forma auditable. Notas de voz y comprobantes procesados. Golden sets por vertical ≥95 % durante 3 noches |",
          "| **Fase 1** \"Competir\" | 3–5 clientes de pago. Menú v2 y primeros pasos en producción. Bandeja y tickets en uso. Un negocio con dos agentes publicados operando con su Coordinador (D-35). Instagram o chat web operativo. Recargas solo si SPEC-14 se retoma (parqueada, D-35). Status page pública |",
          "| **Fase 2** \"Plus\" | 2 casos de estudio publicados. Al menos 3 integraciones MCP verificadas. Agencia y cobro en USD solo si SPEC-21 se retoma (parqueada, D-35) |",
          "", "## Backlog completo (por hito y spec)", ""]
    activas = [h for h in hus.values() if not parqueada(h)]
    parqueadas = [h for h in hus.values() if parqueada(h)]
    L += hu_table(activas, ROOT, with_meta=True)
    L += ["", "## Por workstream", "", "| Workstream | 0A | 0B | 1 | 2 | Total |", "|---|---:|---:|---:|---:|---:|"]
    for w in sorted(ws):
        c = ws[w]
        L.append(f"| {w} | {c['0A']} | {c['0B']} | {c['1']} | {c['2']} | {sum(c.values())} |")
    if parqueadas:
        L += ["", f"## HU parqueadas ({len(parqueadas)})", "",
              "Fuera del calendario y de los totales de arriba (D-35). Se retoman por decisión, no por orden del backlog.", ""]
        L += hu_table(parqueadas, ROOT, with_meta=True)
    (ROOT / "06-backlog-resumen.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def write_phase_readmes(hus: dict) -> None:
    sets = {
        "03-fase-0-go-live": [("HU del Hito 0A", [h for h in hus.values() if h["hito"] == "0A"], True),
                              ("HU del Hito 0B", [h for h in hus.values() if h["hito"] == "0B"], False)],
        "04-fase-1-competir": [("HU de la fase", [h for h in hus.values() if h["fase"] == 1], False)],
        "05-fase-2-plus": [("HU de la fase", [h for h in hus.values() if h["fase"] == 2], False)],
    }
    for folder, blocks in sets.items():
        p = ROOT / folder / "README.md"
        text = p.read_text(encoding="utf-8")
        gen = []
        for title, lst, graph in blocks:
            act = [h for h in lst if not parqueada(h)]
            par = [h for h in lst if parqueada(h)]
            gen += [f"## {title} ({len(act)})", ""] + hu_table(act, p.parent, with_meta=False) + [""]
            if graph:
                gen += ["### Dependencias dentro del Hito 0A", ""] + mermaid(act) + [""]
            if par:
                gen += [f"### HU parqueadas ({len(par)})", "", "Fuera del calendario y del total de arriba (D-35); se retoman por decisión.", ""]
                gen += hu_table(par, p.parent, with_meta=False) + [""]
        new = re.sub(r"<!-- GENERADO:inicio -->.*?<!-- GENERADO:fin -->",
                     "<!-- GENERADO:inicio -->\n" + "\n".join(gen).strip() + "\n<!-- GENERADO:fin -->", text, flags=re.S)
        p.write_text(new, encoding="utf-8")


def replace_block(text: str, name: str, content: str) -> str:
    pattern = re.compile(rf"<!-- GENERADO:{name}:inicio -->.*?<!-- GENERADO:{name}:fin -->", re.S)
    if not pattern.search(text):
        errors.append(f"07-guia-de-ejecucion.md: falta el marcador GENERADO:{name}")
        return text
    return pattern.sub(lambda m: f"<!-- GENERADO:{name}:inicio -->\n{content.strip()}\n<!-- GENERADO:{name}:fin -->", text)


def skill_label(sk: str) -> str:
    c = CATALOGO[sk]
    aviso = " ⚠️" if c.get("estado") == "desactualizada" else ""
    if c["tipo"] == "agente":
        return f"agente `{sk}`{aviso}"
    return f"`{sk}`{aviso}"


def hu_check_line(h, base: pathlib.Path) -> str:
    box = "[x]" if h.get("estado") == "terminada" else "[ ]"
    star = (" ★" if h.get("critico") else "") + (" ⏸️ parqueada" if parqueada(h) else "")
    deps = ", ".join(h.get("dependencias", []))
    deps_txt = f" · depende de {deps}" if deps else ""
    skills = ", ".join(skill_label(sk) for sk in h.get("skills", []))
    link = f"[{h['id']}]({os.path.relpath(h['_path'], base)})"
    return f"- {box} {link}{star} {h['titulo']} · {h['estimacion']}{deps_txt} — {skills}"


def write_guide(hus: dict) -> None:
    p = ROOT / "07-guia-de-ejecucion.md"
    if not p.exists():
        return
    text = p.read_text(encoding="utf-8")
    uso = collections.Counter(sk for h in hus.values() for sk in h.get("skills", []))
    # catálogo agrupado por origen, en el orden del YAML
    por_origen: dict = collections.OrderedDict()
    for sk, c in CATALOGO.items():
        por_origen.setdefault(c["origen"], []).append(sk)
    lines = []
    for origen, sks in por_origen.items():
        lines += [f"**{origen[0].upper() + origen[1:]}**", "", "| Nombre | Tipo | Para qué | Estado | HU que la recomiendan |",
                  "|---|---|---|---|---:|"]
        for sk in sks:
            c = CATALOGO[sk]
            estado = "⚠️ desactualizada" if c.get("estado") == "desactualizada" else "✅"
            lines.append(f"| `{sk}` | {c['tipo']} | {c['uso']} | {estado} | {uso.get(sk, 0)} |")
        lines.append("")
    text = replace_block(text, "catalogo", "\n".join(lines))

    olas = {1: "Ola 1 · Urgente y barato", 2: "Ola 2 · Fundamentos", 3: "Ola 3 · Capacidades",
            4: "Ola 4 · Alta automática y cierre"}
    a = [h for h in hus.values() if h["hito"] == "0A"]
    lines = []
    for o, titulo in olas.items():
        grupo = sorted((h for h in a if h.get("ola") == o and not parqueada(h)), key=sort_key)
        hechas = sum(1 for h in grupo if h.get("estado") == "terminada")
        lines += [f"**{titulo}** ({hechas}/{len(grupo)} terminadas, {num(sum(DIAS[h['estimacion']] for h in grupo))} días-persona sin IA)", ""]
        lines += [hu_check_line(h, ROOT) for h in grupo] + [""]
    text = replace_block(text, "hu-0A", "\n".join(lines))

    def by_spec(subset):
        out = []
        specs = spec_dirs()
        for spec in sorted({h["spec"] for h in subset}):
            grupo = sorted((h for h in subset if h["spec"] == spec), key=sort_key)
            act = [h for h in grupo if not parqueada(h)]
            par = [h for h in grupo if parqueada(h)]
            hechas = sum(1 for h in act if h.get("estado") == "terminada")
            nombre = specs[spec].name
            extra = f" · {len(par)} parqueadas" if par else ""
            out += [f"**[{spec}]({os.path.relpath(specs[spec] / 'spec.md', ROOT)})** · {nombre[len(spec) + 1:].replace('-', ' ')} ({hechas}/{len(act)}{extra})", ""]
            out += [hu_check_line(h, ROOT) for h in act] + [""]
            if par:
                out += [hu_check_line(h, ROOT) for h in par] + [""]
        return "\n".join(out)

    text = replace_block(text, "hu-0B", by_spec([h for h in hus.values() if h["hito"] == "0B"]))
    text = replace_block(text, "hu-1", by_spec([h for h in hus.values() if h["hito"] == "1"]))
    text = replace_block(text, "hu-2", by_spec([h for h in hus.values() if h["hito"] == "2"]))
    p.write_text(text, encoding="utf-8")


def plan_markdown() -> list[pathlib.Path]:
    """Todos los .md del repo, sin las carpetas de `IGNORED_DIRS`."""
    return [f for f in ROOT.rglob("*.md") if not IGNORED_DIRS.intersection(f.relative_to(ROOT).parts)]


def linkify() -> None:
    hu_path = {"-".join(p.name.split("-")[:3]): p for p in ROOT.glob("0[345]-*/SPEC-*/hu/HU-*.md")}
    spec_path = {k: d / "spec.md" for k, d in spec_dirs().items()}
    hu_re = re.compile(r"(?<![\[\w/-])(HU-[A-Z]+-\d{2})(?![\w\]-])")
    spec_re = re.compile(r"(?<![\[\w/-])(SPEC-\d{2})(?![\w\]-])")
    for f in plan_markdown():
        text = f.read_text(encoding="utf-8")
        self_id = "-".join(f.name.split("-")[:3]) if f.parent.name == "hu" else None
        out, in_fm, in_code = [], False, False
        for i, line in enumerate(text.split("\n")):
            if i == 0 and line == "---":
                in_fm = True
                out.append(line)
                continue
            if in_fm:
                in_fm = line != "---"
                out.append(line)
                continue
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code or line.lstrip().startswith("```") or line.startswith("#") or line.startswith("**ID:**"):
                out.append(line)
                continue
            parts = line.split("`")
            for j in range(0, len(parts), 2):
                parts[j] = hu_re.sub(
                    lambda m: m.group(1) if m.group(1) in (self_id,) or m.group(1) not in hu_path
                    else f"[{m.group(1)}]({os.path.relpath(hu_path[m.group(1)], f.parent)})", parts[j])
                parts[j] = spec_re.sub(
                    lambda m: m.group(1) if m.group(1) not in spec_path or spec_path[m.group(1)] == f
                    else f"[{m.group(1)}]({os.path.relpath(spec_path[m.group(1)], f.parent)})", parts[j])
            out.append("`".join(parts))
        new = "\n".join(out)
        if new != text:
            f.write_text(new, encoding="utf-8")


def slug(h: str) -> str:
    h = re.sub(r"[`*_~]", "", h.strip().lower())
    return "".join(ch for ch in h if ch.isalnum() or ch in "- ").replace(" ", "-")


def check_links() -> int:
    link = re.compile(r"\[([^\]]*)\]\(([^)\s]+)\)")
    anchors: dict = {}
    total = 0
    for f in plan_markdown():
        in_code = False
        for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_code = not in_code
            if in_code:
                continue
            for _, target in link.findall(line):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                total += 1
                path, _, anchor = target.partition("#")
                dest = (f.parent / path).resolve() if path else f
                if not dest.exists():
                    errors.append(f"enlace roto {f.relative_to(ROOT)}:{n} -> {target}")
                    continue
                if anchor and dest.suffix == ".md":
                    if dest not in anchors:
                        hs, code = set(), False
                        for l in dest.read_text(encoding="utf-8").splitlines():
                            if l.lstrip().startswith("```"):
                                code = not code
                            if not code and l.startswith("#"):
                                hs.add(slug(l.lstrip("#")))
                        anchors[dest] = hs
                    if anchor not in anchors[dest]:
                        errors.append(f"ancla rota {f.relative_to(ROOT)}:{n} -> {target}")
    return total


def main() -> int:
    check_only = "--check" in sys.argv
    hus, reqs = load_hus(), load_reqs()
    validate_hus(hus, reqs)
    validate_reqs(hus, reqs)
    validate_tasks(hus)
    validate_decisions()
    pruebas = validate_test_catalog(hus)
    if not errors and not check_only:
        write_backlog(hus)
        write_phase_readmes(hus)
        write_guide(hus)
        linkify()
    total_links = check_links()
    for e in errors:
        print("ERROR", e)
    print(f"HU: {len(hus)} · REQ: {len(reqs)} · pruebas del catálogo: {pruebas} · "
          f"enlaces relativos: {total_links} · errores: {len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

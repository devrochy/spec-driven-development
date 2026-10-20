# spec-driven-development

> **A spec-driven development system for a multi-tenant AI agent platform — 200+ user stories, ADRs, DoR/DoD and evals.**

This is the public mirror of the planning system behind [agent-core](https://github.com/devrochy/agent-core) and the SolversHub platform. It shows how I run a senior engineering process: nothing gets implemented without a spec, a user story and an architectural decision.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## What this is

A complete SDD (Spec-Driven Development) workspace: the constitution that defines
the engineering rules, the re-validation that grounded the plan in real code, the
decision records with options and trade-offs, and a backlog of **200+ user stories**
split into 3 phases and 20+ specs — each one with its business value, dependencies
and definition of done.

## Structure

| Directory | What it contains |
|---|---|
| [`00-constitucion.md`](00-constitucion.md) | Engineering invariants, SDD cycle, templates, DoR/DoD |
| [`01-revalidacion/`](01-revalidacion/) | Evidence: re-validation of the plan against the actual code |
| [`02-vision-y-decisiones/`](02-vision-y-decisiones/) | Executive summary, requirements, decisions (D-01…), risks, open questions |
| [`03-fase-0-go-live/`](03-fase-0-go-live/) | Phase 0 specs: production, reliability, agent confidence, media, presets, WhatsApp, commerce, panel |
| [`04-fase-1-competir/`](04-fase-1-competir/) | Phase 1 specs: architecture, professional views, channels, growth, Agent OS |
| [`05-fase-2-plus/`](05-fase-2-plus/) | Phase 2 specs: agency/international, voice and reports |
| [`06-backlog-resumen.md`](06-backlog-resumen.md) | Full backlog table with priorities, dependencies and status |
| [`07-guia-de-ejecucion.md`](07-guia-de-ejecucion.md) | Execution guide: checklists and skills per case |
| [`08-bitacora-de-ejecucion.md`](08-bitacora-de-ejecucion.md) | Execution log with the state of every story |
| [`09-linea-base.md`](09-linea-base.md) | Baseline taken before touching production (golden sets, backups) |
| [`11-pruebas/`](11-pruebas/) | Test data catalog and cycle reports |

## How the process works

- **Constitution first.** Invariants and rules are written before any story: no
  code without a spec and an approved design, ADRs for irreversible decisions,
  tests as part of done, small incremental changes.
- **Every story is a file.** A user story carries its acceptance criteria, its
  business value, its dependencies and its state — the backlog is the source of
  truth, not a task board.
- **Decisions are documented.** Each decision record presents the options, the
  pros/cons and the winner — so a reviewer can disagree with a decision but never
  with the reasoning behind it.
- **Evals are part of the plan.** Consistency metrics (pass^k) and golden sets are
  defined as first-class work items, not as an afterthought.

## What stays private

Billing, pricing and commercial/legal specs (the tariff, subscription plans and
the go-to-market legal work) live in the private planning repository. Everything
engineering-relevant is here.

## Related repositories

| Repo | What it is |
|---|---|
| [agent-core](https://github.com/devrochy/agent-core) | The multi-tenant Python runtime for production AI agents |
| [solvershub-panel](https://github.com/devrochy/solvershub-panel) | The admin panel (Next.js 16) |
| [solvershub-apk](https://github.com/devrochy/solvershub-apk) | The offline-first field app (Expo) |

## License

MIT. See [LICENSE](LICENSE).

## Contact

[LinkedIn](https://linkedin.com/in/robinson-aguilar-ramirez-8970a1129) · [Email](mailto:devrochy@gmail.com)

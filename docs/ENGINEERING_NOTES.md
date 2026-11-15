# Skills and verification

## What this repository demonstrates

A release checklist that requires a completed rollback drill, a named owner, and enough remaining error budget. It returns a proceed or hold recommendation with failed checks listed.

## Reproduce the result

The fixture holds the release because the remaining SLO budget is below its configured minimum. Reproduce the primary fixture with `python3 agent.py example.json`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The CLI checks supplied evidence fields. It does not validate their provenance, approve a release, or deploy it.

Review the missing checks individually. Hold until rollback evidence, accountable ownership, and the configured error budget are present.

[agent.py](../agent.py) · [examples/Bundled scenario.stdout.txt](../examples/Bundled%20scenario.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)

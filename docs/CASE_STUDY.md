# Production Release Readiness walkthrough

## Business problem

Evaluate whether a production release has enough operational evidence to proceed.

## Reproduce the workflow

Run `python3 agent.py example.json` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
{
  "decision": "hold",
  "missing": [
    "slo_budget"
  ]
}
```

The sample supplies these fields. `rollback_drill`, `owner`, `slo_budget_remaining`, `minimum_budget`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.

## Regression scenario

Proceed when rollback evidence, ownership, and the minimum error budget are all present.

`make verify` runs this scenario and compares the result with the checked-in expected JSON.

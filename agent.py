import argparse
import json
from pathlib import Path


def evaluate(data):
    checks = {"rollback_drill": data["rollback_drill"] is True,
              "owner": bool(data["owner"].strip()),
              "slo_budget": data["slo_budget_remaining"] >= data["minimum_budget"]}
    missing = [name for name, passed in checks.items() if not passed]
    return {"decision": "hold" if missing else "proceed", "missing": missing}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input.read_text(encoding="utf-8"))
        print(json.dumps(evaluate(data), indent=2))
    except (KeyError, TypeError, ValueError, OSError) as exc:
        parser.exit(2, f"Invalid input: {exc}\n")


if __name__ == "__main__":
    main()

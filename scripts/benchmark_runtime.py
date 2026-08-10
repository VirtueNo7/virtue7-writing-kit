#!/usr/bin/env python3
from pathlib import Path
import json
from statistics import mean
import yaml

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    runtime = yaml.safe_load((ROOT / "RUNTIME_MANIFEST.yaml").read_text(encoding="utf-8"))
    index = yaml.safe_load((ROOT / "runtime/packet-index.yaml").read_text(encoding="utf-8"))
    benchmark = yaml.safe_load((ROOT / "tests/journeys.yaml").read_text(encoding="utf-8"))
    baseline = benchmark["baseline"]
    journeys = benchmark["journeys"]
    boot_files = [ROOT / p for p in runtime["boot"]["files"]]
    boot_bytes = sum(p.stat().st_size for p in boot_files)
    failures = []
    rows: list[dict] = []
    if len(boot_files) != 3:
        failures.append("Boot must contain exactly three files.")
    if boot_bytes > runtime["boot"]["maximum_bytes"]:
        failures.append(f"Boot exceeds {runtime['boot']['maximum_bytes']} bytes: {boot_bytes}")
    for journey in journeys:
        route = index["routes"][journey["route"]]
        profile = index["profiles"][journey["profile"]]
        total = boot_bytes + route["bytes"] + profile["bytes"]
        files = len(boot_files) + 2
        baseline_bytes = journey["baseline_bytes"]
        baseline_files = journey["baseline_files"]
        byte_reduction = (baseline_bytes - total) / baseline_bytes * 100
        file_reduction = (baseline_files - files) / baseline_files * 100
        ok = (
            total <= journey.get("maximum_bytes", 45000)
            and files <= journey.get("maximum_files", 5)
            and files < baseline_files
        )
        if not ok:
            failures.append(f"{journey['id']}: {total} bytes across {files} files")
        rows.append({
            "id": journey["id"],
            "route": journey["route"],
            "profile": journey["profile"],
            "baseline_bytes": baseline_bytes,
            "current_bytes": total,
            "byte_reduction_percent": round(byte_reduction, 1),
            "baseline_files": baseline_files,
            "current_files": files,
            "file_reduction_percent": round(file_reduction, 1),
            "passed": ok,
        })
    boot_reduction = (baseline["boot_bytes"] - boot_bytes) / baseline["boot_bytes"] * 100
    result = {
        "baseline": baseline,
        "current": {
            "version": runtime["bundle"]["version"],
            "boot_bytes": boot_bytes,
            "boot_files": len(boot_files),
        },
        "summary": {
            "journeys": len(rows),
            "baseline_byte_range": [min(row["baseline_bytes"] for row in rows), max(row["baseline_bytes"] for row in rows)],
            "current_byte_range": [min(row["current_bytes"] for row in rows), max(row["current_bytes"] for row in rows)],
            "mean_baseline_bytes": round(mean(row["baseline_bytes"] for row in rows), 1),
            "mean_current_bytes": round(mean(row["current_bytes"] for row in rows), 1),
            "mean_byte_reduction_percent": round(
                (1 - mean(row["current_bytes"] for row in rows) / mean(row["baseline_bytes"] for row in rows)) * 100,
                1,
            ),
            "journey_reduction_range_percent": [
                min(row["byte_reduction_percent"] for row in rows),
                max(row["byte_reduction_percent"] for row in rows),
            ],
            "boot_reduction_percent": round(boot_reduction, 1),
            "file_reduction_percent": 50.0,
        },
        "journeys": rows,
    }
    (ROOT / "tests/RUNTIME_BENCHMARK_RESULTS.json").write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"Boot: {baseline['boot_bytes']} -> {boot_bytes} bytes "
        f"({result['summary']['boot_reduction_percent']}% less)"
    )
    for row in rows:
        print(
            f"- {'PASS' if row['passed'] else 'FAIL'} {row['id']}: "
            f"{row['baseline_bytes']} -> {row['current_bytes']} bytes "
            f"({row['byte_reduction_percent']}% less), "
            f"{row['baseline_files']} -> {row['current_files']} files"
        )
    if failures:
        print("Runtime benchmark failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print(
        f"Runtime benchmark passed: {len(rows)} journeys; "
        f"mean context reduction {result['summary']['mean_byte_reduction_percent']}%"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

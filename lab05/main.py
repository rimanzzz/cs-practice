
import sys
from pathlib import Path

from logstats import count_levels, format_report, top_errors


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Использование: python {Path(sys.argv[0]).name} <файл-журнала>", file=sys.stderr)
        return 2

    log_path = Path(sys.argv[1])
    counts = {}
    total = 0
    error_count = 0
    broken_count = 0
    errors = []

    try:
        with log_path.open("r", encoding="utf-8") as log:
            for line in log:
                total += 1
                if not line.strip():
                    continue
                try:
                    from logstats import parse_event
                    event = parse_event(line)
                    counts[event["level"]] = counts.get(event["level"], 0) + 1
                    if event["level"] == "ERROR":
                        error_count += 1
                except ValueError:
                    counts["BROKEN"] = counts.get("BROKEN", 0) + 1
                    broken_count += 1

        with log_path.open("r", encoding="utf-8") as log:
            errors = top_errors(log, 3)

    except (OSError, UnicodeError) as exc:
        print(f"Не удалось прочитать журнал: {exc}", file=sys.stderr)
        return 1

    print(total)
    print(error_count)
    print(broken_count)

    report = format_report(counts, errors)
    report_path = Path("report.txt")
    try:
        report_path.write_text(report, encoding="utf-8")
    except OSError as exc:
        print(f"Не удалось записать report.txt: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import sys
from pathlib import Path

from logstats import count_levels, format_report, parse_event, top_errors


def main() -> int:
    if len(sys.argv) > 1:
        filename = sys.argv[1].strip()
    else:
        filename = sys.stdin.readline().strip()

    if not filename:
        print("Не указано имя файла журнала", file=sys.stderr)
        return 2

    log_path = Path(filename)
    counts = {}
    total = 0
    error_count = 0
    broken_count = 0

    try:
        with log_path.open("r", encoding="utf-8") as log:
            for line in log:
                total += 1
                if not line.strip():
                    continue
                try:
                    event = parse_event(line)
                    level = event["level"]
                    counts[level] = counts.get(level, 0) + 1
                    if level == "ERROR":
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
    try:
        Path("report.txt").write_text(report, encoding="utf-8")
    except OSError as exc:
        print(f"Не удалось записать report.txt: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

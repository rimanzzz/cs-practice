from collections import Counter
from typing import Iterable


def parse_event(line: str) -> dict:

    parts = line.strip().split(maxsplit=2)
    if len(parts) != 3:
        raise ValueError("Ожидались время, уровень и сообщение")

    timestamp, level, message = parts
    if not timestamp or not level or not message:
        raise ValueError("Пустое поле в записи журнала")

    valid_levels = {"DEBUG", "INFO", "WARNING", "ERROR"}
    if level not in valid_levels:
        raise ValueError(f"Неизвестный уровень: {level}")

    return {"time": timestamp, "level": level, "message": message}


def count_levels(lines: Iterable[str]) -> dict:
    counts = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            counts[event["level"]] += 1
        except ValueError:
            counts["BROKEN"] += 1
    return dict(counts)


def top_errors(lines: Iterable[str], n: int) -> list:
    if n < 0:
        raise ValueError("n не может быть отрицательным")

    errors = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            errors[event["message"]] += 1

    return [[message, count] for message, count in
            sorted(errors.items(), key=lambda item: (-item[1], item[0]))[:n]]


def format_report(counts: dict, errors: list) -> str:
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")

    lines.extend(["", "Частые ошибки:"])
    if errors:
        for message, count in errors:
            lines.append(f"- {message} — {count}")
    else:
        lines.append("- Нет ошибок")

    return "\n".join(lines) + "\n"

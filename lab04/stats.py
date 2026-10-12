def parse_record(line: str) -> dict:
    parts = line.strip().split(";")
    if len(parts) != 3:
        raise ValueError("ожидалось ровно три поля: город;температура;дата")

    city, temp_text, date = (part.strip() for part in parts)
    if not city:
        raise ValueError("не указан город")
    if not date:
        raise ValueError("не указана дата")
    if not temp_text:
        raise ValueError("не указана температура")

    try:
        temperature = float(temp_text.replace(",", "."))
    except ValueError as exc:
        raise ValueError(
            f"температура должна быть числом: {temp_text!r}"
        ) from exc


def read_valid(lines: list[str]) -> list[dict]:
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            continue
    return records


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for record in records:
        city = record["city"]
        totals[city] = totals.get(city, 0.0) + record["temperature"]
        counts[city] = counts.get(city, 0) + 1

    return {
        city: round(totals[city] / counts[city], 1)
        for city in totals
    }


def warmest_city(records: list[dict]) -> str:
    averages = average_by_city(records)
    if not averages:
        raise ValueError("нет корректных записей для вычисления средней температуры")

    highest_average = max(averages.values())
    return min(city for city, average in averages.items()
               if average == highest_average)

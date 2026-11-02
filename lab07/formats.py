import json


def csv_to_records(text):
    res = text.strip().split('\n')
    res1 = [x.strip() for x in res[0].split(',')]
    records = []

    for s in res[1:]:
        s = [x.strip() for x in s.split(',')]
        records.append(dict(zip(res1, s)))
    return records


def parse_settings(lines):
    settings = {}
    current_list = None

    for line in lines:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        if line.startswith("- ") and current_list is not None:
            settings[current_list].append(line[2:].strip())
            continue

        if "#" in line:
            line = line.split("#", 1)[0].strip()

        if not line or ":" not in line:
            continue

        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()

        if not value:
            settings[key] = []
            current_list = key
            continue

        current_list = None

        if value in ("true", "yes"):
            value = True
        elif value in ("false", "no"):
            value = False
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass

        settings[key] = value

    return settings

def merge_by_key(rows, extra, key="id"):
    result = []

    for row in rows:
        row_key = str(row.get(key, ""))
        extra_row = extra.get(row_key, {})

        merged = row | extra_row
        result.append(merged)

    return result


def records_to_json(records):
    result = json.dumps(
        records,
        ensure_ascii=False,
        indent=2,
        sort_keys=True
    )
    return result

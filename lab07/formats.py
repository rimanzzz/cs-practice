def csv_to_records(text):
    res = text.split('\n')
    res1 = res[0].split(',')
    records = []

    for s in res[1:]:
        s = s.split(',')
        records.append(dict(zip(res1, s)))
    return records

def parse_settings(lines):
    settings = {}
    for v in lines:
        v = v.split(':')
        key = v[0].strip()
        value = v[1].strip()
        if value.isdigit():
            value = int(value)
        elif '.' in value:
            value = float(value)
        elif value == 'true':
            value = True
        elif value == 'false':
            value = False
        settings[key] = value
    return settings

def merge_by_key(rows, extra, key):
    result = []
    for row in rows:
        for item in extra:
            if row[key] == item[key]:
                merged = row | item
                result.append(merged)
    return result
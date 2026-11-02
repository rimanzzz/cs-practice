def csv_to_records(text):
    res = text.split('\n')
    res1 = res[0].split(',')
    records = []

    for s in res[1:]:
        s = s.split(',')
        records.append(dict(zip(res1, s)))
    return records
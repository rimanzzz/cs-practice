import sys

from stats import average_by_city, read_valid, warmest_city


def main() -> None:
    lines = sys.stdin.read().splitlines()
    records = read_valid(lines)

    skipped = 0
    for line in lines:
        if not line.strip():
            continue
        from stats import parse_record
        try:
            parse_record(line)
        except ValueError:
            skipped += 1

    print(len(records))
    print(skipped)
    if records:
        city = warmest_city(records)
        print(f"{average_by_city(records)[city]:.1f}")
    else:
        print("Нет данных")


if __name__ == "__main__":
    main()

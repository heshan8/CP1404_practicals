"""
Write a program to read this file, process the data and display processed information.

Displays the champions and how many times they have won.
Displays the countries of the champions in alphabetical order
"""
FILENAME = "wimbledon.csv"
COUNTRY = 1
CHAMPION = 2


def main():
    records = get_records(FILENAME)
    champion_to_count, countries = get_records(records)
    display_results(champion_to_count, countries)


def display_results(champion_to_count, countries):
    """displays champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"These {len(countries)} have won Wimbledon")
    print(",".join(country for country in sorted(countries)))


def process_records(records):
    """Process data taken from get_records function"""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[COUNTRY])
        champion_to_count[record[CHAMPION]] += 1
    return champion_to_count, countries


def get_records(FILENAME):
    """Get data from file"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()

from guitar import Guitar

GUITAR_FILENAME = 'guitars.csv'


def main():
    guitars = []
    in_file = open('guitars.csv', 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add)

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        print(guitars)
        name = input("Name: ")

    with open(GUITAR_FILENAME, 'w', encoding="utf-8-sig") as in_file:
        for item in guitars:
            print(*item, sep=',', file=in_file)


main()

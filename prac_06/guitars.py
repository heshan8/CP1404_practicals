from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    guitar_name = input("Guitar name: ")
    while guitar_name != "":
        guitar_year = int(input("Guitar year: "))
        guitar_cost = float(input("Guitar cost: $ "))
        new_guitar = [guitar_name, guitar_year, guitar_cost]
        guitars.append(new_guitar)
        print(f"{new_guitar[0]} ({new_guitar[1]}) : ${new_guitar[2]} added.")
        guitar_name = input("Guitar name: ")

    guitars.append(Guitar("Test Guitar", 2000, 5000.0))
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))

    if guitars:
        guitars.sort()
        print("These are my guitars")
        for i, guitar in enumerate(guitars, start=1):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(Vintage)"
            # max_length = max(len(guitars[0]) for guitar in guitars)
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage}")
    else:
        print("No guitars found!")


main()

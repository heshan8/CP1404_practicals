from prac_06.guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    guitar_name = input("Guitar name: ")
    while guitar_name != "":
        guitar_year = int(input("Guitar year: "))
        guitar_cost = int(input("Guitar cost: "))
        new_guitar = [guitar_name, guitar_year, guitar_cost]
        guitars.append(new_guitar)
        guitar_name = input("Guitar name: ")


main()

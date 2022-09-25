"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    """converts celsius to fahrenheit and vice versa """
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            celsius_result = convert_celsius(celsius)
            print(f"Result {celsius_result:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            fahrenheit_result = convert_fahrenheit(fahrenheit)
            print(f"Result {fahrenheit_result:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius(celsius):
    """converts celsius to fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit(fahrenheit):
    """converts fahrenheit to celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


main()

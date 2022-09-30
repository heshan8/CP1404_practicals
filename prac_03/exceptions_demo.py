"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when a non integer is entered
2. When will a ZeroDivisionError occur?
when 0 is entered as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Using a boolean
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = safe_div(numerator, denominator)
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
    print("Finished.")


def safe_div(numerator, denominator):
    if denominator == 0:
        return denominator
    return numerator / denominator


main()

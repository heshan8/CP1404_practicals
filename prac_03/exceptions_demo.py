"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when a non integer is entered
2. When will a ZeroDivisionError occur?
when 0 is entered as the denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Using an If, Else function
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = zero_div(numerator, denominator)
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    # except ZeroDivisionError:
    #     print("Cannot divide by zero!")
    print("Finished.")


def zero_div(numerator, denominator):
    """check user input for zero to avoid ZeroDivisionError"""
    if denominator == 0:
        return denominator
    else:
        return numerator / denominator


main()

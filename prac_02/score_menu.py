"""score menu program"""


menu = """ - (V) get valid number
 - (P) print score
 - (S) print stars
 - (Q) Quit """


def main():
    """print user score and stars"""
    print(menu)
    number = int
    choice = input(">").upper()
    while choice != "Q":
        if choice == "V":
            number = get_valid_num()
        elif choice == "P":
            print(f" Score {number} is {(check_score(number))}")
        elif choice == "S":
            print_line(number)
        else:
            print("Invalid Choice: ")
        print(menu)
        choice = input(">").upper()
    print("Good Bye!")


def get_valid_num():
    """get valid number form user input"""
    number = int(input("Enter num: "))
    while number < 0 or number > 100:
        print("Invalid number")
        number = int(input("Enter number: "))
    return number


def check_score(score):
    """determine given score category"""
    if score < 0:
        return "invalid score"
    elif score > 100:
        return "invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "passable"
    elif score >= 90:
        return "Excellent"


def print_line(length):
    """prints a line of stars"""
    print("*" * length)


main()

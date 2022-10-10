"""program that outputs information about a list of user entered numbers """


def main():
    numbers = []
    number_of_numbers = int(input("How many numbers: "))

    for number in range(1, number_of_numbers + 1):
        user_input = int(input(f"Enter number: "))
        numbers.append(user_input)
    print(f"Numbers Entered: {numbers}")
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The largest number is {max(numbers)}")
    print(f"The smallest number is {min(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {float(average):2}")


main()

"""Security checker"""
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
security_checker = input("Enter username: ")

while security_checker not in usernames:
    print("Access denied!")
    security_checker = input("Enter username: ")
print("Access Granted")

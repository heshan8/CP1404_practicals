"""password with error checking"""


def main():
    """program to get password and print asterisk"""
    password = input("password: ")
    while password != "Q":
        if (len(password)) < 5:
            print("Too short")
            password = input("Password: ")
        else:
            print_asterisk(password)
            password = input("Password: ")
    print("Quit")


def print_asterisk(password):
    """function get print asterisk"""
    count = len(password)
    print("*" * count)


main()

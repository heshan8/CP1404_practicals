"""password with error checking"""


def main():
    min_length = 5
    password = input("Password: ").upper()
    while password != "Q":
        if (len(password)) < min_length:
            print("Too short")
            password = input("Password: ")
        else:
            print("*" * len(password))
        password = input("Password: ")


main()

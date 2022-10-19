"""program that stores users' emails (unique keys) and names (values) in a dictionary"""


def main():
    name_to_email = {}
    email = input("Enter email: ")
    while email != "":
        name = get_name_from_email(email)
        check_name = input(f"is your name {name}? (Y/N): ")
        if check_name.upper() != "Y" and check_name != "":
            name = input("Enter your name: ")
        name_to_email[email] = name
        email = input("Enter email: ")
    max_length = max(len(name) for name in list(name_to_email))
    for email, name in name_to_email.items():
        print(f"{name:{max_length}} - ({email})")


def get_name_from_email(email):
    """get email from user input and splits it at '@'"""
    parts = email.split('@')[0]
    return parts.title()


main()

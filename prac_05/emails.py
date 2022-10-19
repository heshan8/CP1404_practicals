"""program that stores users' emails (unique keys) and names (values) in a dictionary"""


def main():
    name_to_email = {}
    email = input("Enter email: ")
    while email != "":
        name = get_name_from_email(email)



def get_name_from_email(email):
    parts = email.split('@')[0]
    return parts


main()

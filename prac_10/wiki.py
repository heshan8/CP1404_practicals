"""A script to get a summary of page based on user input"""

import wikipedia

user_input = input("Enter page title or search phrase: ").title()
while user_input != "":
    print(wikipedia.summary(user_input))
    user_input = input("Enter page title or search phrase: ").title()
print("Good bye")

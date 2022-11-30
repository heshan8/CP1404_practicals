"""A script to get a summary of page based on user input"""

import wikipedia

user_input = input("Enter page title or search phrase: ").title()
while user_input != "":
    try:
        get_data = wikipedia.page(user_input)
        print(f"Page title: {get_data.title}")
        print(f"Page URL: {get_data.url}")
        print(wikipedia.summary(user_input))
        user_input = input("Enter page title or search phrase: ").title()

    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
print("Good bye")

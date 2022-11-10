"""Program incomplete"""

from project import Projects

PROJECTS_FILENAME = 'projects.txt'
MENU = "Menu:\n(L)oad projects\n(S)ave projects\n(D)isplay projects" \
       "\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit\n>>> "


def main():
    menu_choice = input(MENU).upper()
    while menu_choice != 'Q':
        if menu_choice == 'L':
            pass
        elif menu_choice == 'S':
            pass
        elif menu_choice == 'D':
            pass
        elif menu_choice == 'F':
            pass
        elif menu_choice == 'A':
            pass
        elif menu_choice == 'U':
            pass
        elif menu_choice == 'Q':
            pass
        else:
            print("Invalid menu choice")
            menu_choice = input(MENU).upper()


main()


# def load_projects_file():
projects = []
with open(PROJECTS_FILENAME, 'r', encoding="utf-8-sig") as in_file:
    for line in in_file:
        parts = line.strip().split()
        projects.append(Projects(parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]))
        print(parts)



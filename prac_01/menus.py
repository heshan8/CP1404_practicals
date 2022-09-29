
menu = """(H)hello
(G)goodbye
(Q)quit"""
name = input("Enter name: ")
print(menu)
choice = input("Pick option: ").upper()
while choice != "Q":  # while input is bad (not Q)
    if choice == "H":
        print("hello!", name)
        print(menu)
        choice = input("").upper()
    elif choice == "G":
        print("goodbye!", name)
        print(menu)
        choice = input("").upper()
    else:
        print("invalid choice!")
        print(menu)
        choice = input("").upper()

print("Finished")



"""
CP1404/CP5632 - Practical
Writing to files
"""
# 1
out_file = open("name.txt", "w")
name = input("Name: ")
print(name, file=out_file)
out_file.close()

# 2
in_file = open("name.txt", "r")
text = in_file.read()
in_file.close()
print(f"Your name is {text}")

# 3
in_file = open("numbers.txt", "r")
total = in_file.readlines()
in_file.close()
print(int(total[0]) + int(total[1]))

# 4
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    total += int(line)
in_file.close()
print(total)



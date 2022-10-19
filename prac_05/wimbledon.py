"""
Write a program to read this file, process the data and display processed information.

Displays the champions and how many times they have won.
Displays the countries of the champions in alphabetical order
"""
FILENAME = "wimbledon.csv"


def main():
    data = get_data(FILENAME)
    print(data)




def get_data(FILENAME):
    """Get data from file"""
    data = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            data.append(parts)
    return data


main()

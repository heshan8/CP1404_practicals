"""
# program that asks the user how many "quick picks" they wish to generate.
# The program then generates that many lines of output.
# Each line consists of 6 random numbers between 1 and 45.
"""

import random

NUMBERS_IN_LINE = 6
MIN = 1
MAX = 45


def main():
    number_of_picks = int(input("How many quick picks? "))
    random_numbers = []
    for i in range(number_of_picks):
        for j in range(NUMBERS_IN_LINE):
            generate_number = random.randint(MIN, MAX)
            while generate_number in random_numbers:
                generate_number = random.randint(MIN, MAX)
            random_numbers.append(generate_number)
        random_numbers.sort()
        print(" ".join(f"{generate_number}" for generate_number in random_numbers))


main()

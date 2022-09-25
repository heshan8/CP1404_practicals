"""
2.
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    """program to get and check user score"""
    score = float(input("Enter score: "))
    print(f"Entered score {score} is {check_score(score)}")
    random_score = random.randint(1, 100)
    print(f"Random score {random_score} is {check_score(random_score)}")


def check_score(score):
    """determine give score category"""
    if score < 0:
        return "invalid score"
    elif score > 100:
        return "invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "passable"
    elif score >= 90:
        return "Excellent"


main()

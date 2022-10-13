"""
Program to look up colours by hexadecimal colour codes
"""

COLOUR_TO_CODE = {"Candy Apple Red": "#ff0800", "Aquamarine1": "#7fffd4", "Baby Blue": "#89cff0",
                  "Bubble Gum": "#ffc1cc", "Crimson": "#dc143c", "Lapis Lazuli": "#26619c", "Jade": "#00a86b",
                  "Vanilla Ice": "#f38fa9", "LimeGreen": "#32cd32", "Mango Tango": "#ff8243"}

for colour, code in COLOUR_TO_CODE.items():
    print(colour, code)

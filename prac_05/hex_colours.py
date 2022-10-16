"""
Program to look up colours by hexadecimal colour codes
"""

COLOUR_TO_CODE = {"candyapplered": "#ff0800", "aquamarine1": "#7fffd4",
                  "babyblue": "#89cff0", "bubblegum": "#ffc1cc",
                  "crimson": "#dc143c", "lapislazuli": "#26619c",
                  "jade": "#00a86b", "vanillaice": "#f38fa9",
                  "limegreen": "#32cd32", "mangotango": "#ff8243", }

colour_name = input("Enter Colour: ").replace(" ", "").lower()
while colour_name != "":
    if colour_name in COLOUR_TO_CODE:
        print(f"Hex code for {colour_name.title()} is {COLOUR_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter Colour: ").replace(" ", "").lower()



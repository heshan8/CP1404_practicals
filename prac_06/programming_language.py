class ProgrammingLanguage:
    """Programming language information"""

    def __init__(self, name, typing, reflection, year):
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.name = name

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"


def run_tests():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print(ruby)


if __name__ == "__main__":
    run_tests()

class Guitar:
    """Guitar information"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, ({self.year}) : ${self.cost}"

    def get_age(self, current_year=2017):
        return current_year - self.year

    def is_vintage(self, vintage=50):
        return self.get_age() >= vintage

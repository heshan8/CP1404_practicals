"""Projects class"""


class Projects:
    """Represent information about a project"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        self.name = name
        self.date = start_date
        self.priority = priority
        self.cost = cost_estimate
        self.completion = completion_percentage

    def __str__(self):
        return f"{self.name}, {self.date}, {self.priority}, {self.cost}, {self.completion}"

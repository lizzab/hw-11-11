# Ben Lizza
# 11/11/19


class Trucks:
    def __init__(self, color, company, model, year, doors):
        self.color = color
        self.company = company
        self.model = model
        self.year = year
        self.doors = doors

    def description(self):
        print(f"This truck is made by {self.company} it is a {self.year}, {self.model}.")
        print(f"It comes in {self.color} and it's a {self.doors} door.")

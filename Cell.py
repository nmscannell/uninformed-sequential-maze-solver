"""
This class represents a cell in a maze, or a state.

Each cell stores not only its own cost, but the cost of the path up to it, and the path leading toward it.

"""


class Cell:

    def __init__(self, row, col, loc, value, cost, path_cost, path):
        self.parent = None
        self.row = row
        self.col = col
        self.loc = loc
        self.value = value
        if value == '*':
            self.interpreted_value = value
        self.cost = cost
        self.path_cost = path_cost
        self.path = path

    def update_interpreted_value(self, new_interpreted_value):
        if self.value != '*':
            raise ValueError
        self.interpreted_value = new_interpreted_value

    def __str__(self):
        return "<" + str(self.loc) + "," + str(self.value) + ">"

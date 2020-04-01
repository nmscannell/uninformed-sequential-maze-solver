"""
This class represents a maze made up of cell objects.

"""

from Cell import Cell


class Maze:

    def __init__(self, n, list_of_chars):
        self.num_rows = n
        self.num_col = n
        self.maze = [['' for row in range(n)] for col in range(n)]
        self.prev_state = None
        list_index = 0
        for i in range(self.num_rows):
            for j in range(self.num_col):
                cost = 1
                if list_of_chars[list_index] == '*':
                    cost = 2
                self.maze[i][j] = Cell(i, j, list_index+1, list_of_chars[list_index], cost, 0, [])
                list_index += 1
        self.current_state = self.maze[0][0]
        self.goal_state = self.maze[n-1][n-1]

    """
    This method returns a list of valid cells to visit next. Searches cannot backtrack.
    :return: List of cells/states
    """
    def get_possible_states(self):
        state_list = []
        if self.current_state.row-1 >= 0:
            cell = self.maze[self.current_state.row-1][self.current_state.col]
            state_list.append(Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path))
        if self.current_state.row+1 < self.num_rows:
            cell = self.maze[self.current_state.row+1][self.current_state.col]
            state_list.append(Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path))
        if self.current_state.col-1 >= 0:
            cell = self.maze[self.current_state.row][self.current_state.col-1]
            state_list.append(Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path))
        if self.current_state.col+1 < self.num_col:
            cell = self.maze[self.current_state.row][self.current_state.col+1]
            state_list.append(Cell(cell.row, cell.col, cell.loc, cell.value, cell.cost, cell.path_cost, cell.path))

        removed = []
        for i in state_list:
            i.parent = self.current_state
            if i.parent is not None:
                i.path_cost = i.parent.path_cost + i.cost
                i.path = i.parent.path + [i]
            if not self.verify_neighbor(i):
                removed.append(i)

            if i not in removed:
                cnt = 4
                while cnt*2 <= len(i.path):
                    string_value = ""
                    for c in range(1, cnt+1):
                        string_value += i.path[-c].value
                    string_value_2 = ""
                    for c in range(cnt+1, cnt*2+1):
                        string_value_2 += i.path[-c].value
                    if string_value == string_value_2:
                        if i not in removed:
                            removed.append(i)
                            break
                    else:
                        cnt += 2

        for i in removed:
            state_list.remove(i)

        return state_list

    """
    This method updates the previous state to where we are, and the current to our next destination.
    :param prev: Where we are currently.
    :param current: Where we are going next.
    :return: None
    """
    def update_states(self, prev, current):
        self.prev_state = prev
        self.current_state = current


    """
    This is a helper method to verify that a neighbor is an appropriate next state.
    """
    def verify_neighbor(self, neighbor):
        i = neighbor
        if len(self.current_state.path) > 1:
            if self.current_state.path[len(self.current_state.path)-2].loc == i.loc:
                return False
        if self.current_state.value is '*':
            state = self.current_state.interpreted_value
            if state is 'a' and i.value is not 'b':
                if i.value is '*':
                    i.interpreted_value = 'b'
                else:
                    return False
            elif state is 'b' and i.value is not 'c':
                if i.value is '*':
                    i.interpreted_value = 'c'
                else:
                    return False
            elif state is 'c' and i.value is not 'a':
                if i.value is '*':
                    i.interpreted_value = 'a'
                else:
                    return False
        elif self.current_state.value is 'a':
            if i.value is not 'b':
                if i.value is '*':
                    i.interpreted_value = 'b'
                else:
                    return False
        elif self.current_state.value is 'b':
            if i.value is not 'c':
                if i.value is '*':
                    i.interpreted_value = 'c'
                else:
                    return False
        elif self.current_state.value is 'c':
            if i.value is not 'a':
                if i.value is '*':
                    i.interpreted_value = 'a'
                else:
                    return False
        return True

    def display_maze(self):
        for i in range(self.num_rows):
            for j in range(self.num_col):
                print(self.maze[i][j].value, end=" ")
            print()

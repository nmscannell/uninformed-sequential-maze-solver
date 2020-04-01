from collections import deque
from Maze import Maze

"""
This class contains search functions as well as a display function to aid in writing data to files.
"""

class Search:

    """
    This function performs breadth_first search on a given maze, m.
    """
    @staticmethod
    def breadth_first(m):
        state = m.current_state
        goal = m.goal_state
        visited = deque()
        frontier = deque()
        frontier.append(state)
        state.path += [state]
        if state.loc is goal.loc:
            return Search.display_solution("BFS", 1, 0, [state])
        while len(frontier) > 0:
            state = frontier.popleft()
            if state is not m.current_state:
                m.update_states(m.current_state, state)
            visited.append(state)
            neighbors = m.get_possible_states()
            for i in neighbors:
                if i.loc is goal.loc:
                    return Search.display_solution("BFS", len(i.path), len(visited), i.path)
                frontier.append(i)
        return Search.display_solution("BFS", 0, len(visited), None)

    """
    This function performs depth_first search on a given maze, m. It also takes in a depth limit 
    to allow the function to also be used for iterative deepening without redundant code.
    """
    @staticmethod
    def depth_first(m, limit):
        state = m.current_state
        goal = m.goal_state
        visited = deque()
        frontier = deque()
        frontier.append(state)
        if len(state.path) == 0:
            state.path += [state]
            if state.loc is goal.loc:
                return Search.display_solution("DFS", 1, 0, [state])
        while len(frontier) > 0:
            if len(state.path) == limit:
                if state.loc is goal.loc:
                    return Search.display_solution("DFS", len(state.path), len(visited), state.path)
                else:
                    return "limit"
            state = frontier.pop()
            if state is not m.current_state:
                m.update_states(m.current_state, state)
            visited.append(state)
            neighbors = m.get_possible_states()
            for i in neighbors:
                if i.loc is goal.loc:
                    return Search.display_solution("DFS", len(i.path), len(visited), i.path)
                frontier.append(i)
        return Search.display_solution("DFS", 0, len(visited), None)

    """
    This is the primary method to call when doing regular depth first search. It passes a very large depth limit to the 
    helper function.
    """
    @staticmethod
    def depth_first_backtrack(m):
        return Search.depth_first(m, 10000000)

    """
    This function performs iterative deepening, repeatedly setting a depth limit and calling depth_first() 
    with that limit.
    """
    @staticmethod
    def iterative_deepening(n, list_of_chars):
        for i in range(1, 10000000):
            result = Search.depth_first(Maze(n, list_of_chars), i)
            if result != "limit":
                return result + "  " + str(i)

    """
    This function performs uniform cost search, deciding on paths based on cost. It uses a priority queue.
    """
    @staticmethod
    def uniform_cost(m):
        state = m.current_state
        goal = m.goal_state
        visited = deque()
        frontier = PriorityQueue()
        frontier.push(Node(state, 0))
        state.path += [state]
        if state.loc is goal.loc:
            return Search.display_solution("Uniform Cost", 1, 0, [state])
        while frontier.size() > 0:
            node = frontier.pop()
            state = node.data
            if state is not m.current_state:
                m.update_states(m.current_state, state)
            visited.append(state)
            neighbors = m.get_possible_states()
            for i in neighbors:
                if i.loc is goal.loc:
                    visited.append(i)
                    num_visited = len(visited)
                    return Search.display_solution("Uniform Cost", len(i.path), num_visited, i.path)
                frontier.push(Node(i, i.path_cost))
        return Search.display_solution("Uniform Cost", 0, len(visited), None)

    """
    This method returns a string of the values returned from the search methods to aid in file writing.
    """
    @staticmethod
    def display_solution(search, sol_length, visited, solution):
        solution_str = "" + search + ", " + str(sol_length) + ", " + str(visited) + ", "
        if solution is not None:
            for i in solution:
                solution_str += str(i)
                solution_str += ", "
        else:
            solution_str += "Nil  "
        return solution_str


"""
Tried to use heapq and priority queue with tuples and it just wasn't working for me.
"""


class Node:

    def __init__(self, data, priority):
        self.data = data
        self.priority = priority


class PriorityQueue:

    def __init__(self):
        self.queue = list()

    def push(self, node):
        if self.size() == 0:
            self.queue.append(node)
        else:
            for i in range(self.size()):
                if node.priority >= self.queue[i].priority:
                    if i == self.size()-1:
                        self.queue.insert(i+1, node)
                    else:
                        continue
                else:
                    self.queue.insert(i, node)

    def pop(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

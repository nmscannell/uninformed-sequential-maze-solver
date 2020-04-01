from Search import Search
from Maze import Maze
from timeit import default_timer as timer


def read_matrix(file_n):
    f = open(file_n)
    n = f.readline()
    num_lines = str(n)
    list_chars = []
    l = f.readline()
    for c in l:
        list_chars.append(c)
    return num_lines, list_chars


if __name__ == "__main__":

    for i in range(31):
        file_name = "Mazes/Maze" + str(i) + ".txt"
        num, list_of_chars = read_matrix(file_name)
        n = int(num)
        write_file = "Mazes/Maze" + str(i) + "results.csv"
        with open(write_file, 'w') as file:
            file.write("Search Type, Solution Length, Visited Cells, Path, Total Time\n")
            searches = [Search.breadth_first(Maze(n, list_of_chars)), Search.depth_first_backtrack(Maze(n, list_of_chars)), Search.iterative_deepening(n, list_of_chars), Search.uniform_cost(Maze(n, list_of_chars))]
            for s in searches:
                start = timer()
                description = s
                end = timer()
                time = end-start
                file.write(description + "  " + str(time) + "\n")

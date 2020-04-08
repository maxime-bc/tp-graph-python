import sys
from timeit import default_timer
from typing import List, Tuple
from random import randrange, sample
from statistics import mean
import matplotlib.pyplot as plt

""" ---------- Plot Roy Warshall exec times ---------- """


def main() -> None:
    min_graph_size = 1
    max_graph_size = 21
    number_of_executions = 1000

    print("{} executions".format(number_of_executions))

    line1 = []
    line2 = []
    line3 = []

    for i in range(min_graph_size, max_graph_size):
        sys.stdout.write('{0:.1f}% processed ({1} vertices) \r'.format(i / max_graph_size * 100, i))
        sys.stdout.flush()

        line1.append(get_n_exec_time(roy_warshall_1, number_of_executions, i))
        line2.append(get_n_exec_time(roy_warshall_1_bis, number_of_executions, i))
        line3.append(get_n_exec_time(roy_warshall_2, number_of_executions, i))

    sys.stdout.write('100% processed ({} vertices) \r'.format(max_graph_size - 1))
    vertices_number = [*range(1, max_graph_size)]

    plt.plot(vertices_number, line1, label='Roy Warshall 1')
    plt.plot(vertices_number, line2, label='Roy Warshall 1 Bis')
    plt.plot(vertices_number, line3, label='Roy Warshall 2')

    plt.grid()

    plt.ylabel('Average exec time (in µs)')
    plt.xlabel('Number of vertices')
    plt.title('Average exec time of the 3 different Roy Warshall algorithms ({} execs)'.format(number_of_executions))
    plt.legend()
    plt.show()


""" ---------- Performance Tests ---------- """


def get_exec_time(function, *args):
    start = default_timer()
    function(*args)
    return default_timer() - start


def get_n_exec_time(algorithm, n, size):
    exec_times = []

    for i in range(n):
        adjacency_list = generate_adjacency_list(size)
        exec_times.append(get_exec_time(algorithm, adjacency_list))

    return mean(exec_times) * 10 ** 6  # Convert seconds to microseconds


""" ---------- Roy Warshall Algorithm ---------- """


def roy_warshall_1(adjacency_list: List[List[int]]) -> List[List[int]]:
    # here we convert the adjacency list to an adjacency matrix
    matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
    vertices_number = len(adjacency_list)
    for k in range(0, vertices_number):
        for i in range(0, vertices_number):
            for j in range(0, vertices_number):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

    return matrix


# Another implementation of Roy Warshall's algorithm, more efficient than roy_warshall_1
def roy_warshall_1_bis(adjacency_list: List[List[int]]) -> List[List[int]]:
    matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 1:
                for x in range(0, len(matrix[j])):
                    if matrix[j][x] == 1:
                        matrix[i][x] = matrix[j][x]
    return matrix


def roy_warshall_2(adjacency_list: List[List[int]]):
    matrix = adjacency_list
    vertices_number = len(matrix)
    for i in range(vertices_number):
        for j in range(vertices_number):
            if i in matrix[j]:
                matrix[j].extend(matrix[i])
                matrix[j] = list(set(matrix[j]))

    return matrix


""" ---------- Depth First Search Algorithm ---------- """


# return a tuple of visited vertices list and scc list using tarjan algorithm
def depth_first_search(adjacency_list: List[List[int]]) -> Tuple[List[int], List[List[int]]]:
    visited_vertices = [False for i in range(len(adjacency_list))]
    visit_stack = []
    res_visit_stack = []

    index = {}
    low_index = {}
    scc = []
    global_index = 0

    def _depth_first_search(vertex: int, glob_index: int):

        if visited_vertices[vertex]:
            return

        visited_vertices[vertex] = True
        visit_stack.append(vertex)
        res_visit_stack.append(vertex)

        index[vertex] = glob_index
        low_index[vertex] = glob_index
        glob_index += 1
        result = []

        for i in adjacency_list[vertex]:
            if not visited_vertices[i]:
                _depth_first_search(i, glob_index)
                low_index[vertex] = min(low_index[vertex], low_index[i])
            elif i in visit_stack:
                low_index[vertex] = min(low_index[vertex], index[i])

        if low_index[vertex] == index[vertex]:
            w = visit_stack.pop()
            while w != vertex:
                result.append(w)
                w = visit_stack.pop()
            result.append(vertex)
            scc.append(result)

    for i in range(len(adjacency_list)):
        if not visited_vertices[i]:
            _depth_first_search(i, global_index)

    for component in scc:
        component.reverse()

    return res_visit_stack, scc


""" ---------- Utility functions ---------- """


def generate_adjacency_list(vertices_number):
    adjacency_list = [[] for i in range(vertices_number)]

    for i in range(vertices_number):
        # actual vertex can be linked to itself
        successors_number = randrange(vertices_number + 1)
        adjacency_list[i].extend(sample(range(vertices_number), successors_number))

    return adjacency_list


def adjacency_list_to_adjacency_matrix(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_number = len(adjacency_list)
    matrix = [[0 for x in range(vertices_number)] for x in range(vertices_number)]

    for i in range(0, len(adjacency_list)):
        for j in range(0, len(adjacency_list[i])):
            matrix[i][adjacency_list[i][j]] = 1

    return matrix


def transpose_adjacency_list(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_number = len(adjacency_list)
    transposed_adjacency_list = [[] for i in range(vertices_number)]

    for i in range(vertices_number):
        for j in range(len(adjacency_list[i])):
            transposed_adjacency_list[adjacency_list[i][j]].append(i)

    return transposed_adjacency_list


def print_matrix(matrix: List[List[int]]) -> None:
    print('    ', end='')
    for i in range(0, len(matrix)):
        print(i, end=' ')

    print('\n', end='')
    print('    ', end='')

    for i in range(0, len(matrix)):
        print('_', end=' ')

    print('\n', end='')

    i = 0
    for row in matrix:
        print('{} |'.format(i), end=' ')
        for val in row:
            print(val, end=' ')
        print('\n', end='')
        i += 1
    print('')


if __name__ == "__main__":
    main()

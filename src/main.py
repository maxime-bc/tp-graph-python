from timeit import default_timer
from typing import List, Tuple
from random import randrange, sample
from statistics import mean

GRAPH_MAX_VERTICES = 10  # Used to generate adjacency lists in function `generate_adjacency_list()`

""" ---------- Main ---------- """


def main():
    number_of_executions = 10000

    print('On a basis of {0} executions, {1} runs in {2:.2f} µs for a {3} vertices graph.'
          .format(number_of_executions, roy_warshall_1.__name__,
                  get_n_exec_time(roy_warshall_1, number_of_executions), GRAPH_MAX_VERTICES))

    print('On a basis of {0} executions, {1} runs in {2:.2f} µs for a {3} vertices graph.'
          .format(number_of_executions, roy_warshall_1_bis.__name__,
                  get_n_exec_time(roy_warshall_1_bis, number_of_executions), GRAPH_MAX_VERTICES))

    print('On a basis of {0} executions, {1} runs in {2:.2f} µs for a {3} vertices graph.'
          .format(number_of_executions, roy_warshall_2.__name__,
                  get_n_exec_time(roy_warshall_2, number_of_executions), GRAPH_MAX_VERTICES))

    adjacency_list = generate_adjacency_list(size=GRAPH_MAX_VERTICES)
    print('depth_first_search : {}'.format(get_exec_time(depth_first_search, adjacency_list)))
    print('adjacency_list_to_adjacency_matrix : {}'
          .format(get_exec_time(adjacency_list_to_adjacency_matrix, adjacency_list)))
    print('transpose_graph : {}'.format(get_exec_time(transpose_graph, adjacency_list)))


""" ---------- Performance Tests ---------- """


def get_exec_time(function, *args):
    start = default_timer()
    function(*args)
    return default_timer() - start


def get_n_exec_time(algorithm, n):
    exec_times = []

    for i in range(n):
        adjacency_list = generate_adjacency_list(size=GRAPH_MAX_VERTICES)
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


def generate_adjacency_list(size=None):
    if size is None:
        vertices_number = randrange(1, GRAPH_MAX_VERTICES + 1)
    else:
        vertices_number = size

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


def transpose_graph(adjacency_list: List[List[int]]) -> List[List[int]]:
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


main()

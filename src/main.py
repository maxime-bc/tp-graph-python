import timeit
from typing import List, Tuple
from statistics import mean


def main():
    exec_number = 1
    show_logs = False
    data_set = [[[], [], [], [], []],

                [[1, 2], [2], [3], [4], []],

                [[3], [2], [], [4], [0]],

                [[1], [2], [0], [2], [3]],

                [[1], [], [1], [0, 2, 6, 4], [5], [3], []],

                [[0, 2, 3, 4], [1, 2, 4], [0, 2, 3, 4], [1, 2, 3, 4], [0, 2, 4]],

                [[1], [2], [0], [1, 2, 5], [2, 6], [3, 4], [4], [5, 6, 7]],

                [[4, 6, 8, 9], [1, 2, 7, 9], [0, 2, 9], [1, 4, 5, 6, 8, 9], [1, 8, 9], [3, 4, 6, 9], [2, 3, 5, 6, 8, 9],
                 [3, 4, 5, 6, 8, 9], [0, 1, 3, 6, 8, 9], [0, 1, 2, 5, 7, 9]],

                [[0, 1, 2, 6, 7, 9], [1, 8, 9], [1, 3, 5, 8, 9], [0, 2, 3, 4, 6, 9], [1, 3, 4, 7, 9], [1, 4, 9],
                 [4, 6, 7, 9], [1, 2, 5, 9], [0, 3, 5, 6, 9], [2, 5, 9]],

                [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]]
                ]

    mean_time_gain = []
    for i in range(exec_number):
        for adjacency_list in data_set:
            mean_time_gain.append(exec_time(adjacency_list, show_logs))

    print('\nIn average, RW2 is {0:.2f} times faster than RW1'.format(mean(mean_time_gain)))


def exec_time(adjacency_list: List[List[int]], log=False) -> float:
    if log:
        print('\nRunning with {} vertices {}'.format(len(adjacency_list), adjacency_list))

    start = timeit.default_timer()
    adjacency_list_to_adjacency_matrix(adjacency_list)
    if log:
        print('adjacency_list_to_adjacency_matrix : {}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    roy_warshall_1(adjacency_list)
    time_rw1 = timeit.default_timer() - start
    if log:
        print('roy1_matrix : {}'.format(time_rw1))

    start = timeit.default_timer()
    roy_warshall_2(adjacency_list)
    time_rw2 = timeit.default_timer() - start
    if log:
        print('roy2_matrix : {}'.format(time_rw2))

    diff = time_rw1 / time_rw2
    if log:
        print('RW2 is {0:.2f} times faster than RW1'.format(diff))

    start = timeit.default_timer()
    depth_first_search(adjacency_list)
    if log:
        print('depth_first_search : {}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    transpose_graph(adjacency_list)
    if log:
        print('transpose_graph : {}'.format(timeit.default_timer() - start))

    return diff


def adjacency_list_to_adjacency_matrix(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_number = len(adjacency_list)
    matrix = [[0 for x in range(vertices_number)] for x in range(vertices_number)]

    for i in range(0, len(adjacency_list)):
        for j in range(0, len(adjacency_list[i])):
            matrix[i][adjacency_list[i][j]] = 1

    return matrix


def roy_warshall_1(adjacency_list: List[List[int]]) -> List[List[int]]:
    # here we convert the adjacency list to an adjacency matrix
    adjacency_matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
    vertices_number = len(adjacency_list)
    for k in range(0, vertices_number):
        for i in range(0, vertices_number):
            for j in range(0, vertices_number):
                adjacency_matrix[i][j] = adjacency_matrix[i][j] or (adjacency_matrix[i][k] and adjacency_matrix[k][j])

    return adjacency_matrix


def roy_warshall_2(adjacency_list: List[List[int]]):
    vertices_number = len(adjacency_list)
    for i in range(vertices_number):
        for j in range(vertices_number):
            if i in adjacency_list[j]:
                adjacency_list[j].extend(adjacency_list[i])
                adjacency_list[j] = list(set(adjacency_list[j]))

    return adjacency_list


def transpose_graph(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_number = len(adjacency_list)
    transposed_adjacency_list = [[] for i in range(vertices_number)]

    for i in range(vertices_number):
        for j in range(len(adjacency_list[i])):
            transposed_adjacency_list[adjacency_list[i][j]].append(i)

    return transposed_adjacency_list


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

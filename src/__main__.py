import timeit
from typing import List


def main():
    adjacency_list_1 = [[1, 2], [2], [3], [4], []]
    adjacency_list_2 = [[0, 2, 3, 4], [1, 2, 4], [0, 2, 3, 4], [1, 2, 3, 4], [0, 2, 4]]

    adjacency_list_3 = [[4, 6, 8, 9], [1, 2, 7, 9], [0, 2, 9], [1, 4, 5, 6, 8, 9], [1, 8, 9], [3, 4, 6, 9],
                        [2, 3, 5, 6, 8, 9],
                        [3, 4, 5, 6, 8, 9], [0, 1, 3, 6, 8, 9], [0, 1, 2, 5, 7, 9]]

    adjacency_list_4 = [[0, 1, 2, 6, 7, 9], [1, 8, 9], [1, 3, 5, 8, 9], [0, 2, 3, 4, 6, 9], [1, 3, 4, 7, 9], [1, 4, 9],
                        [4, 6, 7, 9], [1, 2, 5, 9], [0, 3, 5, 6, 9], [2, 5, 9]]

    exec_time(adjacency_list_2)


def exec_time(adjacency_list: List[List[int]]) -> None:
    start = timeit.default_timer()
    adjacency_list_to_adjacency_matrix(adjacency_list)
    print('adjacency_list_to_adjacency_matrix : {}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    roy_warshall_1(adjacency_list)
    print('roy1_matrix : {}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    roy_warshall_2(adjacency_list)
    print('roy2_matrix : {}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    depth_first_search(adjacency_list)
    print('depth_first_search : {}'.format(timeit.default_timer() - start))

    start = timeit.default_timer()
    transpose_graph(adjacency_list)
    print('transpose_graph : {}'.format(timeit.default_timer() - start))


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

        list(set(adjacency_list[i]))

    return adjacency_list


def depth_first_search(adjacency_list: List[List[int]]) -> List[int]:
    visited_vertexes = [False for i in range(len(adjacency_list))]
    visit_order = []

    def _depth_first_search(v: int, visited: List[bool]):
        visited[v] = True
        visit_order.append(v)

        for i in range(len(adjacency_list[v])):

            if not visited[adjacency_list[v][i]]:
                _depth_first_search(adjacency_list[v][i], visited)

    for i in range(len(visited_vertexes)):
        if not visited_vertexes[i]:
            _depth_first_search(i, visited_vertexes)

    return visit_order


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
        y = 0
        print('{} |'.format(i), end=' ')
        for val in row:
            print(val, end=' ')
        print('\n', end='')
        i += 1
    print('')


if __name__ == '__main__':
    main()

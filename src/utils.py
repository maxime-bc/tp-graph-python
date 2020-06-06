import sys
from random import randrange, sample
from typing import List, Tuple


def check_args(args: List[str]) -> Tuple[int, int, int]:
    if len(args) != 4:
        sys.exit("Usage : <min_graph_size> <max_graph_size> <number_of_executions>")

    min_graph_size = int(args[1])
    max_graph_size = int(args[2])
    number_of_executions = int(args[3])
    if min_graph_size < 1 or max_graph_size <= min_graph_size or number_of_executions < 1:
        sys.exit("Invalid arguments.")
    return min_graph_size, max_graph_size + 1, number_of_executions


def generate_adjacency_list(vertices_number: int) -> List[List[int]]:
    adjacency_list = [[] for _ in range(vertices_number)]

    for i in range(vertices_number):
        # actual vertex can be linked to itself
        successors_number = randrange(vertices_number + 1)
        adjacency_list[i].extend(sample(range(vertices_number), successors_number))

    return adjacency_list


def generate_adjacency_list_without_cycles(vertices_number: int) -> List[List[int]]:
    adjacency_list = [[] for _ in range(vertices_number)]

    for i in range(vertices_number):
        successors_number = randrange(vertices_number - i)
        adjacency_list[i].extend(sample(range(i + 1, vertices_number), successors_number))

    return adjacency_list


def print_adjacency_matrix_csv(adjacency_matrix: List[List[int]]) -> None:
    vertices_number = len(adjacency_matrix)
    for i in range(vertices_number):
        for j in range(vertices_number):
            print(adjacency_matrix[i][j], end='')
            if j != (vertices_number - 1):
                print(', ', end='')
        print('\n', end='')
    print('\n', end='')


def adjacency_list_to_adjacency_matrix(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_number = len(adjacency_list)
    matrix = [[0 for _ in range(vertices_number)] for _ in range(vertices_number)]

    for i in range(len(adjacency_list)):
        for j in range(len(adjacency_list[i])):
            matrix[i][adjacency_list[i][j]] = 1

    return matrix


def transpose_adjacency_list(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_number = len(adjacency_list)
    transposed_adjacency_list = [[] for i in range(vertices_number)]

    for i in range(vertices_number):
        for j in range(len(adjacency_list[i])):
            transposed_adjacency_list[adjacency_list[i][j]].append(i)

    return transposed_adjacency_list


def get_vertices_degree(adjacency_list: List[List[int]]):
    # 0: vertex index
    # 1: vertex degree

    vertices_degree = [[0, 0] for i in range(len(adjacency_list))]

    for i in range(len(adjacency_list)):
        for j in range(len(adjacency_list[i])):
            vertices_degree[adjacency_list[i][j]][0] = adjacency_list[i][j]
            vertices_degree[adjacency_list[i][j]][1] += 1

    return vertices_degree


def adjacency_list_to_line_graph_list(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_num = len(adjacency_list)
    lines_list = []

    for i in range(vertices_num):
        for j in range(len(adjacency_list[i])):
            vertex_to_add = [i, adjacency_list[i][j]]
            reversed_vertex_to_add = [adjacency_list[i][j], i]

            if reversed_vertex_to_add not in lines_list:
                lines_list.append(vertex_to_add)

    lines_list_len = len(lines_list)
    line_graph_adjacency_list = [[] for i in range(lines_list_len)]

    for i in range(lines_list_len):
        for j in range(lines_list_len):

            if lines_list[i] != lines_list[j]:
                if lines_list[i][0] in lines_list[j] or lines_list[i][1] in lines_list[j]:
                    line_graph_adjacency_list[i].extend([j])

    return line_graph_adjacency_list


def print_adjacency_matrix(adjacency_matrix: List[List[int]]) -> None:
    print('    ', end='')
    for i in range(len(adjacency_matrix)):
        print(i, end=' ')

    print('\n', end='')
    print('    ', end='')

    for i in range(len(adjacency_matrix)):
        print('_', end=' ')

    print('\n', end='')

    i = 0
    for row in adjacency_matrix:
        print('{} |'.format(i), end=' ')
        for val in row:
            print(val, end=' ')
        print('\n', end='')
        i += 1
    print('')

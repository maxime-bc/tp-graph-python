from random import randrange, sample
from typing import List


def generate_adjacency_list(vertices_number: int) -> List[List[int]]:
    adjacency_list = [[] for i in range(vertices_number)]

    for i in range(vertices_number):
        # actual vertex can be linked to itself
        successors_number = randrange(vertices_number + 1)
        adjacency_list[i].extend(sample(range(vertices_number), successors_number))

    return adjacency_list


def generate_adjacency_list_without_cycles(vertices_number: int) -> List[List[int]]:
    adjacency_list = [[] for i in range(vertices_number)]

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
    matrix = [[0 for x in range(vertices_number)] for x in range(vertices_number)]

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

import sys
from typing import List, Tuple

from src.performance import plot_performances
from src.utils import adjacency_list_to_adjacency_matrix, generate_adjacency_list


def main() -> None:
    functions_to_plot = [roy_warshall_1, roy_warshall_1_bis, roy_warshall_2]
    graph_labels = {
        'title': 'Average exec time of the 3 different Roy Warshall algorithms',
        'xlabel': 'Number of vertices',
        'ylabel': 'Average exec time (in seconds)',
    }
    plot_performances(sys.argv, functions_to_plot, graph_labels, generate_adjacency_list)


""" ---------- Roy Warshall Algorithm ---------- """


def roy_warshall_1(adjacency_list: List[List[int]]) -> List[List[int]]:
    # here we convert the adjacency list to an adjacency matrix
    matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
    vertices_number = len(adjacency_list)
    for k in range(vertices_number):
        for i in range(vertices_number):
            for j in range(vertices_number):
                matrix[i][j] = matrix[i][j] or (matrix[i][k] and matrix[k][j])

    return matrix


def roy_warshall_1_bis(adjacency_list: List[List[int]]) -> List[List[int]]:
    matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                for x in range(len(matrix[j])):
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


if __name__ == "__main__":
    main()

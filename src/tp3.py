from operator import itemgetter
from typing import List

from src.utils import adjacency_list_to_adjacency_matrix, print_adjacency_matrix_csv, get_vertices_degree


def main():
    graph = [[1, 2], [2], [3], [4], []]
    # graph = [[1], [0, 2], [1, 3], [2]]
    # graph = [[3, 5, 7], [6, 2, 4], [5, 7, 1], [0, 4, 6], [1, 3, 7], [0, 2, 6], [1, 3, 5], [0, 2, 4]]
    # graph = [[5, 6, 7], [4, 6, 7], [4, 5, 7], [4, 5, 6], [1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
    # graph = [[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
    # print(welsh_powell_2(adjacency_list_to_line_list(graph)))
    print(welsh_powell_2(graph))
    print(welsh_powell_1(graph))


def welsh_powell_1(adjacency_list: List[List[int]]) -> List[int]:
    def _get_vertex_neighbours(vertex: int, adjacency_list: List[List[int]]) -> List[int]:
        adjacency_matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
        vertex_neighbours = []

        for i in range(len(adjacency_matrix[vertex])):
            if adjacency_matrix[vertex][i] == 1 or adjacency_matrix[i][vertex] == 1:
                vertex_neighbours.extend([i])

        return vertex_neighbours

    def _check_neighbours_color(color: int, vertex_neighbours: List[int], vertices_colors: List[int]) -> bool:
        for i in range(len(vertex_neighbours)):
            if vertices_colors[vertex_neighbours[i]] == color:
                return False
        return True

    color = 1
    # 0 = not colored
    vertices_num = len(adjacency_list)
    vertices_color = [0 for i in range(vertices_num)]

    vertices_degree = sorted(get_vertices_degree(adjacency_list), key=itemgetter(1), reverse=True)

    for j in range(vertices_num):
        for i in range(vertices_num):
            vertex_neighbours = _get_vertex_neighbours(vertices_degree[i][0], adjacency_list)

            if vertices_color[vertices_degree[i][0]] == 0:
                if _check_neighbours_color(color, vertex_neighbours, vertices_color):
                    vertices_color[vertices_degree[i][0]] = color

        color += 1

    return vertices_color

def welsh_powell_2(adjacency_list: List[List[int]]) -> List[int]:
    def _get_vertex_neighbours(vertex: int, adjacency_list: List[List[int]]) -> List[int]:
        adjacency_matrix = adjacency_list_to_adjacency_matrix(adjacency_list)
        vertex_neighbours = []

        for i in range(len(adjacency_matrix[vertex])):
            if adjacency_matrix[vertex][i] == 1 or adjacency_matrix[i][vertex] == 1:
                vertex_neighbours.extend([i])

        return vertex_neighbours

    def _check_neighbours_color(color: int, vertex_neighbours: List[int], vertices_colors: List[int]) -> bool:
        for i in range(len(vertex_neighbours)):
            if vertices_colors[vertex_neighbours[i]] == color:
                return False
        return True

    color = 1
    # 0 = not colored
    vertices_num = len(adjacency_list)
    vertices_color = [0 for i in range(vertices_num)]

    for j in range(vertices_num):
        for i in range(vertices_num):
            if vertices_color[i] == 0:

                vertex_neighbours = _get_vertex_neighbours(i, adjacency_list)
                if _check_neighbours_color(color, vertex_neighbours, vertices_color):
                    vertices_color[i] = color

        color += 1

    return vertices_color


def adjacency_list_to_line_list(adjacency_list: List[List[int]]) -> List[List[int]]:
    vertices_num = len(adjacency_list)
    lines_list = []

    for i in range(vertices_num):
        for j in range(len(adjacency_list[i])):
            vertex_to_add = [i, adjacency_list[i][j]]
            reversed_vertex_to_add = [adjacency_list[i][j], i]

            if reversed_vertex_to_add not in lines_list:
                lines_list.append(vertex_to_add)

    adjacency_lines_list = [[] for i in range(len(lines_list))]

    for i in range(len(lines_list)):
        for j in range(len(lines_list)):

            if lines_list[i] != lines_list[j]:
                if lines_list[i][0] in lines_list[j] or lines_list[i][1] in lines_list[j]:
                    adjacency_lines_list[i].extend([j])

    return adjacency_lines_list


if __name__ == "__main__":
    main()

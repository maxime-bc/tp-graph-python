import sys
from operator import itemgetter
from typing import List

from src.performance import plot_performances
from src.utils import adjacency_list_to_adjacency_matrix, get_vertices_degree, adjacency_list_to_line_graph_list, \
    generate_undirected_adjacency_list


def main():
    functions_to_plot = [welsh_powell_1, welsh_powell_2]
    graph_labels = {
        'title': 'Average exec time of Welsh Powell algorithm',
        'xlabel': 'Number of vertices',
        'ylabel': 'Average exec time (in seconds)',
    }
    plot_performances(sys.argv, functions_to_plot, graph_labels, generate_undirected_adjacency_list)


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


# welsh powell with sorting vertices by their degree
def welsh_powell_1(adjacency_list: List[List[int]]) -> List[int]:
    color = 1
    # 0 = not colored
    vertices_num = len(adjacency_list)
    vertices_color = [0 for i in range(vertices_num)]

    vertices_degree = sorted(get_vertices_degree(adjacency_list), key=itemgetter(1), reverse=True)

    for i in range(vertices_num):
        for j in range(vertices_num):
            if vertices_color[vertices_degree[j][0]] == 0 and \
                    _check_neighbours_color(color, _get_vertex_neighbours(vertices_degree[j][0], adjacency_list),
                                            vertices_color):
                vertices_color[vertices_degree[j][0]] = color

        color += 1

    return vertices_color


# welsh powell without sorting vertices by their degree
def welsh_powell_2(adjacency_list: List[List[int]]) -> List[int]:
    color = 1
    # 0 = not colored
    vertices_num = len(adjacency_list)
    vertices_color = [0 for i in range(vertices_num)]

    for i in range(vertices_num):
        for j in range(vertices_num):
            if vertices_color[j] == 0 and \
                    _check_neighbours_color(color, _get_vertex_neighbours(j, adjacency_list), vertices_color):
                vertices_color[j] = color

        color += 1

    return vertices_color


def color_edges(adjacency_list: List[List[int]]) -> List[int]:
    return welsh_powell_2(adjacency_list_to_line_graph_list(adjacency_list))


if __name__ == "__main__":
    main()

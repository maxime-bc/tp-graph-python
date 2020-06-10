import sys
from operator import itemgetter
from typing import List

from src.performance import plot_performances
from src.utils import generate_adjacency_list_without_cycles


def main():
    functions_to_plot = [grundy]
    graph_labels = {
        'title': 'Average exec time of grundy value algorithm',
        'xlabel': 'Number of vertices',
        'ylabel': 'Average exec time (in seconds)',
    }
    plot_performances(sys.argv, functions_to_plot, graph_labels, generate_adjacency_list_without_cycles)


def leveling(adjacency_list: List[List[int]]) -> List[int]:
    vertices_num = len(adjacency_list)
    no_successor_vertices = []
    graph_leveling = [0] * vertices_num

    for i in range(vertices_num):
        if not adjacency_list[i]:
            no_successor_vertices.append(i)

    i = 0
    while i < len(no_successor_vertices):
        for j in range(vertices_num):
            for k in range(len(adjacency_list[j])):

                if adjacency_list[j][k] == no_successor_vertices[i]:
                    no_successor_vertices.append(j)  # <-- à optimiser ?

                    if graph_leveling[j] < (graph_leveling[no_successor_vertices[i]] + 1):
                        graph_leveling[j] = graph_leveling[no_successor_vertices[i]] + 1
        i += 1
    return graph_leveling


def get_association_list(adjacency_list: List[List[int]]) -> List[List[int]]:
    leveling_list = leveling(adjacency_list)
    association_list = [[] for i in range(len(adjacency_list))]

    for i in range(len(adjacency_list)):
        association_list[i].extend([i, leveling_list[i]])

    return sorted(association_list, key=itemgetter(1))


def grundy(adjacency_list: List[List[int]]) -> List[List[int]]:
    def _find_grundy_value(complete_list, elem):
        grundy_value = -1
        for sub_list in complete_list:
            if elem == sub_list[0]:
                grundy_value = sub_list[1]
                break
        return grundy_value

    grundy_list = []
    association_list = get_association_list(adjacency_list)

    for i in range(len(association_list)):
        if association_list[i][1] == 0:
            grundy_list.append(association_list[i])
        else:
            successors_list = adjacency_list[association_list[i][0]]
            grundy_values = []

            for j in range(len(successors_list)):
                grundy_values.append(_find_grundy_value(grundy_list, successors_list[j]))

            k = 0
            while k in grundy_values:
                k += 1

            grundy_list.append([association_list[i][0], k])

    return grundy_list


if __name__ == "__main__":
    main()

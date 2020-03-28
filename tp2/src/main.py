from operator import itemgetter
from typing import List


def main():
    # graph = [[1, 2], [2], [3], [4], []]
    graph = [[1, 2], [2], [3], [4, 5], [], [6], []]

    tmp_list = get_vertices_levels_association(graph)

    print(grundy(tmp_list, graph))


def get_graph_leveling(adjacency_list: List[List[int]]) -> List[int]:
    vertices_num = len(adjacency_list)
    no_successor_vertices = []
    levels = [0] * vertices_num

    for i in range(vertices_num):
        if not adjacency_list[i]:
            no_successor_vertices.append(i)

    i = 0
    while i < len(no_successor_vertices):
        for j in range(vertices_num):
            for k in range(len(adjacency_list[j])):

                if adjacency_list[j][k] == no_successor_vertices[i]:
                    no_successor_vertices.append(j)

                    if levels[j] < (levels[no_successor_vertices[i]] + 1):
                        levels[j] = levels[no_successor_vertices[i]] + 1
        i += 1
    return levels


def get_vertices_levels_association(adjacency_list: List[List[int]]) -> List[List[int]]:
    leveling = get_graph_leveling(adjacency_list)
    list_complete = [[] for i in range(len(adjacency_list))]

    for i in range(len(adjacency_list)):
        list_complete[i].extend([i, leveling[i]])

    return sorted(list_complete, key=itemgetter(1))


def find_grundy_value(list_complete, elem):
    grundy_value = -1

    for sub_list in list_complete:
        if elem == sub_list[0]:
            grundy_value = sub_list[1]
            break

    return grundy_value


def grundy(list_complete: List[List[int]], adjacency_list: List[List[int]]) -> List[List[int]]:
    tmp_list = []

    for i in range(len(list_complete)):

        if list_complete[i][1] == 0:
            tmp_list.append(list_complete[i])
        else:
            successors_list = adjacency_list[list_complete[i][0]]
            grundy_values = []

            for j in range(len(successors_list)):
                grundy_values.append(find_grundy_value(tmp_list, successors_list[j]))

            k = 0
            while k in grundy_values:
                k += 1

            tmp_list.append([list_complete[i][0], k])

    return tmp_list

from typing import List


def main():
    # graph = [[1, 2], [2], [3], [4], []]
    # graph = [[0, 2, 3, 4], [1, 2, 4], [0, 2, 3, 4], [1, 2, 3, 4], [0, 2, 4]]

    graph = [[4, 6, 8, 9], [1, 2, 7, 9], [0, 2, 9], [1, 4, 5, 6, 8, 9], [1, 8, 9], [3, 4, 6, 9], [2, 3, 5, 6, 8, 9],
             [3, 4, 5, 6, 8, 9], [0, 1, 3, 6, 8, 9], [0, 1, 2, 5, 7, 9]]

    # graph = [[0, 1, 2, 6, 7, 9], [1, 8, 9], [1, 3, 5, 8, 9], [0, 2, 3, 4, 6, 9], [1, 3, 4, 7, 9], [1, 4, 9],
    #         [4, 6, 7, 9], [1, 2, 5, 9], [0, 3, 5, 6, 9], [2, 5, 9]]

    # matrix = graph_to_matrix(graph)
    # roy_warshall_2(graph)

    # print_matrix(roy_warshall_2(graph))

    depth_first_search(graph)

    # transitive_closure_matrix = roy_warshall_1(graph)
    # print_matrix(transitive_closure_matrix)


def graph_to_matrix(graph: List[List[int]]) -> List[List[int]]:
    vertices_number = len(graph)
    matrix = [[0 for x in range(vertices_number)] for x in range(vertices_number)]

    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            matrix[i][graph[i][j]] = 1

    return matrix


def roy_warshall_1(graph: List[List[int]]):
    # here we convert the graph to an adjacency matrix
    adjacency_matrix = graph_to_matrix(graph)
    vertices_number = len(graph)
    for k in range(0, vertices_number):
        for i in range(0, vertices_number):
            for j in range(0, vertices_number):
                adjacency_matrix[i][j] = adjacency_matrix[i][j] or (adjacency_matrix[i][k] and adjacency_matrix[k][j])

    return adjacency_matrix


def roy_warshall_2(graph: List[List[int]]):
    vertices_number = len(graph)
    for i in range(vertices_number):
        for j in range(vertices_number):
            if i in graph[j]:
                graph[j].extend(graph[i])
                graph[j] = list(set(graph[j]))

        list(set(graph[i]))

    print(graph)
    return graph


def depth_first_search(graph: List[List[int]]):
    visited_vertexes = [False for i in range(len(graph))]

    def _depth_first_search(v: int, visited: List[bool]):
        visited[v] = True
        print("Visiting {}".format(v))

        for i in range(len(graph[v])):

            if not visited[graph[v][i]]:
                print("{} --> {}".format(v, graph[v][i]))
                _depth_first_search(graph[v][i], visited)

    for i in range(len(visited_vertexes)):
        if not visited_vertexes[i]:
            print("Starting at {}".format(i))
            _depth_first_search(i, visited_vertexes)


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

import sys
from statistics import mean
from timeit import default_timer
from typing import List, Dict

import matplotlib.pyplot as plt

from src.utils import check_args


def plot_performances(args: List[str], functions, labels: Dict[str, str], graph_generation):
    min_graph_size, max_graph_size, number_of_executions = check_args(args)
    print("{} execution(s)".format(number_of_executions))
    lines = [[] for i in range(len(functions))]
    counter = 0

    for i in range(min_graph_size, max_graph_size):
        sys.stdout.write(
            '{0:.1f}% processed (w/ {1} vertices) \r'.format((counter + 1) / (max_graph_size - min_graph_size) * 100,
                                                             i))
        sys.stdout.flush()

        for j in range(len(functions)):
            lines[j].append(get_n_exec_time(functions[j], number_of_executions, graph_generation(i)))

        counter += 1

    vertices_number = [*range(min_graph_size, max_graph_size)]

    for k in range(len(functions)):
        line_label = functions[k].__name__
        plt.plot(vertices_number, lines[k], label='{} algorithm'.format(line_label.replace("_", " ").title()))

    plt.grid()
    plt.ylabel(labels['ylabel'])
    plt.xlabel(labels['xlabel'])
    plt.title(labels['title'] + ' ({} execution(s))'.format(number_of_executions))
    plt.legend()
    plt.show()


def get_exec_time(function, *args) -> float:
    start = default_timer()
    function(*args)
    return default_timer() - start


def get_n_exec_time(algorithm, n, adjacency_list) -> int:
    exec_times = []

    for i in range(n):
        exec_times.append(get_exec_time(algorithm, adjacency_list))

    return mean(exec_times)

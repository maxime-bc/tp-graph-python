from statistics import mean
from timeit import default_timer

from src.utils import generate_adjacency_list


def get_exec_time(function, *args) -> float:
    start = default_timer()
    function(*args)
    return default_timer() - start


def get_n_exec_time(algorithm, n, size) -> int:
    exec_times = []

    for i in range(n):
        adjacency_list = generate_adjacency_list(size)
        exec_times.append(get_exec_time(algorithm, adjacency_list))

    return mean(exec_times) * 10 ** 6  # Convert seconds to microseconds

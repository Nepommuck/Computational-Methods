from task1 import test_task1
from task2 import test_task2


graph = [
    [2, 4],
    [0, 2, 4],
    [3],
    [0],
    [1, 2, 3],
]
iterations = 15


# test_task1(graph, iterations)
test_task2(graph, iterations, d=0.75)
# test_task2(graph, iterations, d=0.8)
# test_task2(graph, iterations, d=0.9)

import os

from sknetwork.data import from_adjacency_list
from sknetwork.ranking import PageRank


def read_edges_from_file(filename):
    file = open(filename, mode='r')
    edges = []
    for line in file.readlines():
        # line = file.readline()
        verticles = [int(v) for v in line.split()]
        edges.append(verticles)
    return edges


def calculate_pagerank(edges):
    adjacency = from_adjacency_list(edges, directed=True)
    pagerank = PageRank()
    scores = pagerank.fit_transform(adjacency)
    return scores


def save_results_to_file(filename, results):
    file = open(filename, mode='w')
    for result in results:
        file.write(f'{result}\n')
    file.close()


def get_result_sum(results):
    total = 0
    for value in results:
        total += value
    return total


def read_and_save_results(graph_path, result_path):
    edges = read_edges_from_file(graph_path)
    result = calculate_pagerank(edges)
    save_results_to_file(result_path, result)
    return result


def main():
    # result = read_and_save_results(
    #     graph_path=os.path.join("graphs", "graph_A_1_500_000_nodes.txt"),
    #     result_path=os.path.join("results", "graph_A_results.txt")
    # )
    result = read_and_save_results(
        graph_path=os.path.join("graphs", "graph_B_5_100_000_nodes.txt"),
        result_path=os.path.join("results", "graph_B_results.txt")
    )
    print(f"Sum of all pagerank values: {get_result_sum(result)}")


main()

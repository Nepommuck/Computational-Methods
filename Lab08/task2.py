from task1 import plot_pagerank, plot_verticle_change


def recalc_rank_with_random_jump(graph, rank, d):
    new_rank = [0 for _ in rank]
    verticles = len(graph)
    for v in range(len(graph)):
        neibours = len(graph[v])
        new_rank[v] += (1-d) / verticles
        for neib in graph[v]:
            new_rank[neib] += d * (rank[v] / neibours)
    return new_rank


def calculate_rank_with_random_jump(graph, iterations, d):
    v = len(graph)
    rank = [1/v for _ in range(v)]
    results = [rank]

    for i in range(iterations):
        rank = recalc_rank_with_random_jump(graph, rank, d)
        results.append(rank)
    return results[-1], results


def test_task2(graph, iterations, d):
    _, results = calculate_rank_with_random_jump(graph, iterations, d)
    title = "d = " + str(d)
    plot_pagerank(results, title)
    plot_verticle_change(results, title)

from matplotlib import pyplot as plt


def display_rank(rank):
    for i in range(len(rank)):
        print(f"{i}: {rank[i]}")


def recalc_rank(graph, rank):
    new_rank = [0 for _ in rank]
    for v in range(len(graph)):
        neibours = len(graph[v])
        for neib in graph[v]:
            new_rank[neib] += rank[v] / neibours
    return new_rank


def calculate_rank(graph, iterations):
    v = len(graph)
    rank = [1/v for _ in range(v)]
    results = [rank]

    for i in range(iterations):
        rank = recalc_rank(graph, rank)
        results.append(rank)
    return results[-1], results


def plot_pagerank(results, title):
    v = len(results[0])
    x_axis = [chr(ord('A') + i) for i in range(v)]
    plt.plot(x_axis, results[-1])

    plt.title("Final Pagerank for verticles: " + title)
    plt.xlabel("Vertex")
    plt.ylabel("Pagerank")
    plt.show()


def plot_verticle_change(results, title):
    iterations = len(results)
    verticles = len(results[0])
    x_axis = [i for i in range(iterations)]
    labels = []
    for v in range(verticles):
        label = plt.plot(x_axis,
                 [iteration[v] for iteration in results])
        labels.append(label)

    plt.legend([lab[0] for lab in labels], [chr(ord('a') + v) for v in range(verticles)], loc=1)

    plt.title("Pagerank for all verticles over time: " + title)
    plt.xlabel("Iteration")
    plt.ylabel("Pagerank")
    plt.show()


def test_task1(graph, iterations):
    _, results = calculate_rank(graph, iterations)
    title = "Simplified version"
    plot_pagerank(results, title)
    plot_verticle_change(results, title)


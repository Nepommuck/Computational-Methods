from random import randrange, random, uniform
import matplotlib.pyplot as plt


SIZE = (100, 100)
N = 30
MAX_ITER = 1000


def get_random_point():
    return uniform(0, SIZE[0]), uniform(0, SIZE[1])


points = [get_random_point() for _ in range(N)]

distances = [[None for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        distances[i][j] = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def distance(i, j):
    return distances[min(i, j)][max(i, j)]


def temperature(i):
    # return 1 - i/MAX_ITER
    return max(1 - 2*i/MAX_ITER, 0)


order = [i for i in range(N)]
def total_distance(order):
    result = 0
    for i in range(N):
        result += distance(order[i], order[(i+1) % N])
    return result


# print(points)
# for row in distances:
#     print(row)


def two_randrange(stop, start=0):
    a = randrange(start, stop)
    b = a
    while a == b:
        b = randrange(start, stop)
    return a, b


def outcome(propability):
    return random() < propability


def simulation():
    results = []
    current_distance = total_distance(order)
    temp = 1

    for i in range(MAX_ITER):
        print(f'Iter {i}:  SCORE = {current_distance}')
        a, b = two_randrange(N)
        # print(a, b)
        order[a], order[b] = order[b], order[a]
        # temp = temperature(i)
        temp = 0.995*temp
        madman = outcome(temp)

        print(madman)
        new_distance = total_distance(order)

        if madman or new_distance < current_distance:
            current_distance = new_distance
        # Revert changes
        else:
            order[a], order[b] = order[b], order[a]

        results.append(current_distance)
    return results


results = simulation()
plt.plot([i for i in range(len(results))], results)
plt.show()

xs = [points[o][0] for o in order]
ys = [points[o][1] for o in order]

plt.plot(xs, ys, marker="s")
#
plt.show()
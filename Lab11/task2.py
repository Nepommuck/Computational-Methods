import numpy as np
from numpy.linalg import inv
from matplotlib import pyplot as plt


POINTS = [
    (-5, 2),
    (-4, 7),
    (-3, 9),
    (-2, 12),
    (-1, 13),
    (0, 14),
    (1, 14),
    (2, 13),
    (3, 10),
    (4, 8),
    (5, 4),
]


def plot_points(points):
    plt.scatter(*zip(*points))


def solve(points):
    n = len(points)
    A = np.zeros(shape=(n, 3))
    for i, (x, _y) in enumerate(points):
        A[i, :] = [x**2, x, 1]

    y = np.array([y for (_x, y) in POINTS])

    Q, R = np.linalg.qr(A)

    return inv(R) @ Q.T @ y


result = solve(POINTS)
print(result)

[a, b, c] = result
f = lambda x: a * x**2 + b*x + c

L, U = -5, 5
N = 1000

x_values = [L + i/N * (U - L) for i in range(N)]
y_values = [f(x) for x in x_values]

plot_points(POINTS)
plt.plot(x_values, y_values)
plt.show()

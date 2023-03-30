import matplotlib.pyplot as plt
import numpy as np
from math import pi, sin, cos

from numpy import linalg


def transpose_vector(vector):
    return [
        [element] for element in vector
    ]


def get_elipse_from_matrix(matrix, sphere):
    elipse = [
        np.matmul(point, matrix) for point in sphere
    ]
    x_elipse = [point[0] for point in elipse]
    y_elipse = [point[1] for point in elipse]
    z_elipse = [point[2] for point in elipse]

    return x_elipse, y_elipse, z_elipse


def get_partial_ellipse(sphere, matrix, steps=3):
    U, Sigma, V = linalg.svd(matrix)
    print(U)
    print(Sigma)
    print(V)
    V = np.transpose(V)
    # V = transpose_vector(V)
    if steps == 1:
            matrix = V
    elif steps == 2:
        matrix = np.matmul(Sigma, V)
    elif steps == 3:
        matrix = np.matmul(
                np.matmul(U, Sigma),
                V)
    else:
        return None

    print()
    elipse = [
        np.matmul(point, matrix) for point in sphere
    ]
    x_elipse = [point[0] for point in elipse]
    y_elipse = [point[1] for point in elipse]
    z_elipse = [point[2] for point in elipse]

    return x_elipse, y_elipse, z_elipse


def plot3d(ellipse):
    ax.scatter3D(ellipse[0], ellipse[1], ellipse[2])

# print(
#     np.transpose([1, 2, 3], axes=1)
# )
ax = plt.axes(projection='3d')

# Data for a three-dimensional line


# Data for three-dimensional scattered points

N = 30
s_arr = [i / N * 2 * pi for i in range(N)]
t_arr = [i / N * pi for i in range(N)]

inputs = []
for s in s_arr:
    for t in t_arr:
        inputs.append((s, t))

x_data = [cos(s) * sin(t) for s, t in inputs]
y_data = [sin(s) * sin(t) for s, t in inputs]
z_data = [cos(t) for s, t in inputs]

points = [(x, y, z) for x, y, z in zip(x_data, y_data, z_data)]
plot3d(ellipse=(x_data, y_data, z_data))
# plt.show()

for _ in range(3):
    rand_matrix = np.random.uniform(low=0, high=1, size=(3, 3))
    ellipse = get_elipse_from_matrix(matrix=rand_matrix, sphere=points)

    plot3d(ellipse)
    # for i in range(1, 2 + 1):
    #     plot3d(
    #         get_partial_ellipse(points, rand_matrix, i)
    #     )
# plt.show()

plt.show()



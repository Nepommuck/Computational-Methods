import numpy as np
import time
from matplotlib import pyplot as plt


def get_biggest_eigenvector(matrix, eps):
    n = matrix.shape[0]
    v = np.array(
        [[1] for _ in range(n)]
    )

    i = 1
    while True:
        new_v = np.matmul(
            matrix, v
        )
        # new_v /= np.linalg.norm(new_v)
        dv = np.linalg.norm(np.add(v, -new_v))
        v = new_v
        if abs(dv) < eps:
            break
        i += 1
    return v / np.linalg.norm(new_v), v.max(), i


def plot_time(min=100, max=500):
    sizes = [i for i in range(min, max)]
    time_measurements = []
    for i in sizes:
        start_time = time.time()
        get_biggest_eigenvector(matrix=100*np.random.random(size=(i, i)), eps=10 ** -10)
        end_time = time.time()
        time_measurements.append(1000*(end_time - start_time))
    plt.plot(sizes, time_measurements)
    plt.xlabel("Matrix size")
    plt.ylabel("Time elapsed [ms]")
    plt.show()


N = 4
eps = 10 ** -5

matrix = np.random.random(size=(N, N)) * 100

print("Matrix: ")
print(matrix)

result, val, iterations = get_biggest_eigenvector(matrix, eps)
print(f"Calculated result in {iterations} iterations:")
print(result)
print(f"val: {val}")

print("Correct answer::")
print(np.linalg.eig(matrix)[1][:, 0])

# plot_time(min=100, max=500)

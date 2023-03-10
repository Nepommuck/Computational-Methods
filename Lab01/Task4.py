import numpy as np
import matplotlib.pyplot as plt


def logistic_map_generate_n(x0, r, n, data_type=np.single):
    def x_next(x_prev):
        return r * x_prev * (1 - x_prev)

    results = np.zeros(shape=n, dtype=data_type)
    results[0] = x0

    for i in range(1, n):
        results[i] = x_next(results[i-1])

    return results


def plot(r_list, x0_list, n, save_as=None):
    legend = []
    figure, axis = plt.subplots(2, 2)

    i = 0
    for r in r_list:
        legend.append([])
        for x0 in x0_list:
            y = logistic_map_generate_n(x0=x0, r=r, n=n)
            axis[i // 2][i % 2].plot([i for i in range(N)], y)
            legend[-1].append(f'x0 = {x0}, r = {r}')
        axis[i // 2][i % 2].legend(legend[-1])
        i += 1

    if save_as is not None:
        plt.savefig(save_as, dpi=1200)
    plt.show()


N = 100

plot(
    r_list = [1, 2, 3, 4],
    x0_list = [0.25, 0.5, 0.75],
    n = N,
    save_as="task4a.png"
)

plot(
    r_list = [3.75, 3.7667, 3.7833, 3.8],
    x0_list = [0.5],
    n = N,
    save_as="task4b.png"
)
import numpy as np


class Series:
    def __init__(self, function, s, n, precision_type=np.single):
        self.function = function
        self.s = s
        self.n = n
        self.precision_type = precision_type

    def __calculate(self, forward=True):
        result = self.precision_type(0)
        start, stop, step = (1, self.n + 1, 1) if forward else (self.n, 0, -1)
        for i in range(start, stop, step):
            result += self.function(k=i, s=self.s)

        return result

    def calculate_forward(self):
        return self.__calculate(forward=True)

    def calculate_backward(self):
        return self.__calculate(forward=False)


def dzeta_partial(k, s):
    return 1 / k ** s

def eta_partial(k, s):
    return (-1) ** (k-1) / k ** s


def main():
    s_list = [2, 3.6667, 5, 7.2, 10]
    n_list = [50, 100, 200, 500, 1_000]

    for (f, function_name) in [(dzeta_partial, "Riemann's Dzeta"), (eta_partial, "Dirichlet's Eta")]:
        for s in s_list:
            for n in n_list:
                for is_forward in [True, False]:
                    series = Series(function=f, s=s, n=n)
                    print(f'function: {function_name} \n'
                          f's = {s} \n'
                          f'n = {n} \n'
                          f'direction = {"Forward" if is_forward else "Backward"} \n'
                          f'result = {series.calculate_forward() if is_forward else series.calculate_backward()} \n\n'
                          )


if __name__ == "__main__":
    main()
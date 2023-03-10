import numpy as np

from Summator import Summator
from Task1 import naive_summ


def kahan_summ(arr, step=None):
    result = np.single(0)
    error = np.single(0)

    for el in arr:
        y = np.single(el - error)
        temp = np.single(result + y)
        error = np.single(
            np.single(temp - result) - y
        )
        result = temp

    return result, None


def main():
    n = 10 ** 7
    v = np.single(0.53125)

    naive_summator = Summator(summ_function=naive_summ, number_of_elements=n, value=v, name="Naive algorithm")
    kahan_summator = Summator(summ_function=kahan_summ, number_of_elements=n, value=v, name="Kahan algorithm")

    naive_summator.present()
    kahan_summator.present()


if __name__ == "__main__":
    main()

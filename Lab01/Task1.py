import numpy as np
from matplotlib import pyplot
from Summator import Summator


def naive_summ(arr, step=None):
    result = np.single(0)
    result_rapport = []

    i = 0
    for el in arr:
        result += el
        if step is not None and i >= step:
            result_rapport.append(result)
            i -= step
        i += 1

    return result, result_rapport


def recursive_summ(arr, first=0, last=None, step=None):
    if last is None:
        last = len(arr) - 1

    if first == last:
        return arr[first], None

    central = first + (last - first) // 2
    return np.single(
        recursive_summ(arr, first=first, last=central)[0] + recursive_summ(arr, first=central + 1, last=last)[0]
    ), None


def main():
    n = 10 ** 7
    v = np.single(0.53125)
    s = 25_000

    naive_summator = Summator(summ_function=naive_summ, number_of_elements=n, value=v, rapport_step=s,
                              name="Naive algorithm")
    recursive_summator = Summator(summ_function=recursive_summ, number_of_elements=n, value=v, rapport_step=None,
                                  name="Recursive algorithm")

    naive_summator.present()
    recursive_summator.present()

    pyplot.plot([i for i in range(s, n, s)], naive_summator.get_error_rapport())
    pyplot.savefig("task1.png", dpi=1200)
    pyplot.show()

    print("Error even in recursive: ")
    n = 10 ** 6
    sorted_arr = [np.single(i) for i in range(n)]
    right_summ = n / 2 * n
    result = recursive_summ(sorted_arr)[0]
    absolute_error = abs(result - right_summ)

    print(f'n = {n} \n' 
          f'Right result = {right_summ} \n' 
          f'Calculated result: {result} \n' 
          f'Absolute error: {absolute_error} \n' 
          f'Relative error: {100 * absolute_error / right_summ}%')


if __name__ == "__main__":
    main()

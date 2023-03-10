import numpy as np
import time


class Summator:
    def __init__(self, summ_function, number_of_elements, value, rapport_step=None, name="Unnamed algorithm"):
        self.__summ_function = summ_function
        self.__number_of_elements = number_of_elements
        self.__value = value
        self.__array = np.array([value for _ in range(number_of_elements)])
        self.name = name

        self.__summ = None
        self.__calculation_rapport = None
        self.__error_rapport = None
        self.__rapport_step = rapport_step

    def get_summ(self):
        if self.__summ is None:
            self.__summ, self.__calculation_rapport = self.__summ_function(arr=self.__array, step=self.__rapport_step)
        return self.__summ

    def get_average(self):
        return self.get_summ() / self.__number_of_elements

    def get_absolute_error(self):
        return np.single(
            abs(self.get_summ() - self.__value * self.__number_of_elements)
        )

    def get_relative_error(self):
        return self.get_absolute_error() / (self.__value * self.__number_of_elements)

    def get_text_results(self):
        return f'v = {self.__value} \n' \
               f'avg = {self.get_average()} \n' \
               f'Absolute error: {self.get_absolute_error()} \n' \
               f'Relative error: {format(100 * self.get_relative_error(), ".2f")}%'

    def get_error_rapport(self):
        if self.__rapport_step is None:
            return None

        if self.__error_rapport is None:
            if self.__calculation_rapport is None:
                self.__summ, self.__calculation_rapport = self.__summ_function(
                    arr=self.__array, step=self.__rapport_step
                )
            self.__error_rapport = []
            for i in range(len(self.__calculation_rapport)):
                true_val = (i + 1) * self.__rapport_step * self.__value
                self.__error_rapport.append(
                    abs(self.__calculation_rapport[i] - true_val) / true_val
                )

        return self.__error_rapport

    def present(self):
        start_time = time.time()
        print(f'{self.name}:')
        print(self.get_text_results())
        end_time = time.time()

        print(f'\nTime elapsed: {format(end_time - start_time, ".2f")} seconds \n\n')

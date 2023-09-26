import numpy as np
from numpy import pi, dot, conjugate, concatenate
from numpy.linalg import norm

import time


def cosine_similarity(a, b):
    return dot(a, b)/(norm(a)*norm(b))


def dft(vector):
    n = vector.shape[0]
    s = np.exp(-2j*pi/n)
    F = np.array([
        [
            np.power(s, j*k) for k in range(n)
        ] for j in range(n)
    ])
    return F @ vector


def idft(vector):
    n = vector.shape[0]
    return conjugate(
        dft(conjugate(vector))
    ) / n


def get_fft_matrix(n):
    if n == 2:
        return np.array([
            [1, 1],
            [1, -1]
        ])
    s = np.exp(-2j*pi/n)
    S_n_2 = np.diag([s ** i for i in range(n//2)])
    F_n_2 = get_fft_matrix(n//2)

    A = F_n_2
    B = S_n_2 @ F_n_2
    C = F_n_2
    D = -S_n_2 @ F_n_2
    return concatenate((
            concatenate((A, B), axis=1),
            concatenate((C, D), axis=1)
        ), axis=0
    )


def fft(vector):
    n = vector.shape[0]
    return get_fft_matrix(n) @ vector


def test(vector, name, own_f, lib_f, display=True, measure_time=False):
    n = vector.shape[0]
    print("Test for n =", n, end='\n\n')
    print(name)
    start = time.time()
    a = own_f(vector)
    end = time.time()
    time1 = end - start

    start = time.time()
    b = lib_f(vector)
    end = time.time()
    time2 = end - start

    if display:
        print("Own implementation:")
        print(a)
        print("Library implementation:")
        print(b)
    print("Similarity:")
    print(cosine_similarity(a, b))

    if measure_time:
        print(f"Time elapsed 1: {time1}s")
        print(f"Time elapsed 2: {time2}s")


test(
    vector=np.random.uniform(low=0, high=100, size=4),
    own_f=dft, lib_f=np.fft.fft, name="DFT", display=True
)
test(
    vector=np.random.uniform(low=0, high=100, size=4),
    own_f=idft, lib_f=np.fft.ifft, name="IDFT", display=True
)
print(
    fft(np.array([2, 1, 3, 7]))
)

test(
    vector=np.random.uniform(low=0, high=100, size=4),
    own_f=fft, lib_f=np.fft.fft, name="IDFT", display=True
)

test(
    vector=np.random.uniform(low=0, high=100, size=2**10),
    own_f=fft, lib_f=dft, name="Time comparison", display=False, measure_time=True
)
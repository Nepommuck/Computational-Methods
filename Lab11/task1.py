import numpy as np


def qr_gram_schmidt(A):
    n = A.shape[0]

    # Q matrix
    Q = np.zeros(shape=(n, n))
    Q[:, 0] = A[:, 0] / np.linalg.norm(A[:, 0])

    for k in range(1, n):
        summ = 0
        for i in range(k):
            summ += np.dot(Q[:, i], A[:, k]) * Q[:, i]

        Q[:, k] = A[:, k] - summ
        Q[:, k] /= np.linalg.norm(Q[:, k])

    # R matrix
    R = np.zeros(shape=(n, n))
    for y in range(n):
        for x in range(n):
            if x >= y:
                R[y, x] = np.dot(Q[:, y], A[:, x])
    return Q, R


N = 6
matrix = np.random.random(size=(N, N))

Q_lib, R_lib = np.linalg.qr(matrix)
Q_own, R_own = qr_gram_schmidt(matrix)

print(matrix, end="\n\n")

print("Q:")
print(Q_lib, end="\n\n")
print(Q_own, end="\n\n")

print("R:")
print(R_lib, end="\n\n")
print(R_own, end="\n\n")

print(Q_lib @ R_lib, end="\n\n")
print(Q_own @ R_own, end="\n\n")

# print(Q_own[0:3, 0:5])
# print(Q_lib[0:3, 0:5])

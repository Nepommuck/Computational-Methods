import math
from math import pi


def sgn(x):
    return math.copysign(1, x)


def sec(x):
    return 1 / math.cos(x)


def bisection(function, borders, eps=10**-4, delta=10**-4):
    beg, end = borders
    beg += 10**-20
    end -= 10**-20
    # print(beg, end)
    if sgn(function(beg)) == sgn(function(end)):
        return None

    iterations = 0
    mid = beg + (end - beg) / 2

    while end - beg > delta and abs(function(mid)) > eps:
        mid = beg + (end - beg) / 2
        if sgn(function(beg)) == sgn(function(mid)):
            beg = mid
        else:
            end = mid
        iterations += 1

    return beg + (end - beg) / 2, iterations


def newton(function, df, borders, eps=10**-4, delta=10**-4):
    beg, end = borders
    beg += 10**-20
    end -= 10**-20

    x0 = math.inf
    x1 = end
    iterations = 0
    while abs(x0 - x1) > delta and abs(function(x1)) > eps:
        a = df(x1)
        b = function(x1) - a * x1
        # print(a)
        x0 = x1
        x1 = -b/a
        iterations += 1
    return x1, iterations


def secant(function, borders, eps=10**-4, delta=10**-4):
    beg, end = borders
    beg += 10**-20
    end -= 10**-20
    derivative = lambda f, x1, x2: (f(x2) - f(x1)) / (x2 - x1)

    iterations = 0
    while abs(beg - end) > delta and abs(function(beg)) > eps:
        a = derivative(function, beg, end)
        b = function(end) - a * end
        # print(a)
        beg = end
        end = -b/a
        iterations += 1
    return end, iterations


def hybrid(function, borders, eps=10**-4, delta=10**-4):
    required = 10**-1
    initial = bisection(function, borders, required, required)
    resultant = secant(function, (initial[0] - required/2, initial[0] + required/2), eps, delta)
    return resultant[0], initial[1] + resultant[1]


f1 = lambda x: math.cos(x) * math.cosh(x) - 1
df1 = lambda x: math.cos(x) * math.sinh(x) - math.cosh(x) * math.sin(x)
b1 = (3/2 * pi, 2*pi)

f2 = lambda x: 1/x - math.tan(x)
df2 = lambda x: -(sec(x))**2 - 1 / x**2
b2 = (0, pi/2)

f3 = lambda x: 2**(-x) + math.e**x + 2 * math.cos(x) - 6
df3 = lambda x: -2 * math.sin(x) + math.e**x - math.log(2) / 2**x
b3 = (1, 3)

print("Bisection:")
print(
    bisection(f1, b1)
)
print(
    bisection(f2, b2)
)
print(
    bisection(f3, b3)
)

print("Newton:")
print(
    newton(f1, df1, b1)
)
print(
    newton(f2, df2, b2)
)
print(
    newton(f3, df3, b3)
)

print("Secant:")
print(
    secant(f1, b1)
)
print(
    secant(f2, b2)
)
print(
    secant(f3, b3)
)

print("Hybrid:")
print(
    hybrid(f1, b1)
)
print(
    hybrid(f2, b2)
)
print(
    hybrid(f3, b3)
)
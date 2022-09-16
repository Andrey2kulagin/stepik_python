import math


def f1(a):
    return a ** 2


def f2(a):
    return abs(a)


def f3(a):
    return a ** 3


def f4(a):
    return math.sqrt(a)


def f5(a):
    return math.sin(a)


funcs = {"квадрат": f1, "модуль": f2, "куб": f3, "корень": f4, "синус": f5}
num = int(input())
inp = input().lower()
print(funcs[inp](num))

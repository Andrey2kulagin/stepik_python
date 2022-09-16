def func1(a):
    return a[0]


def f2(a):
    return a[1]


def func3(a):
    return a[2]


def f4(a):
    return a[3]


athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
param = int(input())
params = [func1, f2, func3, f4]
athletes.sort(key=params[param-1])
for i in athletes:
    print(*i)

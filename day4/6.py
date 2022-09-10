n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
sum_el_1 = 0
sum_el_2 = 0
sum_el_3 = 0
sum_el_4 = 0
for i in range(n):
    for j in range(n):
        if j < i < n - 1 - j:
            sum_el_4 += a[i][j]
        elif n - 1 - j < i < j:
            sum_el_2 += a[i][j]
        elif i < j and i < n - 1 - j:
            sum_el_1 += a[i][j]
        elif i > j and i > n - 1 - j:
            sum_el_3 += a[i][j]
print("Верхняя четверть:", sum_el_1)
print("Правая четверть:", sum_el_2)
print("Нижняя четверть:", sum_el_3)
print("Левая четверть:", sum_el_4)

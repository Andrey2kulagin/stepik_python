n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
sum_d_1 = a[0][0]
sum_d_2 = a[0][n - 1]
cure_sum = sum(a[0])
all_str = ""
for i in range(n):
    for j in range(n):
        all_str += str(a[i][j])
for i in "123456789":
    if not (i in all_str):
        exit(print("NO"))
for i in range(1, n):
    if sum(a[i]) != cure_sum:
        exit(print("NO"))
    sum_d_1 += a[i][i]
    sum_d_2 += a[i][n - 1 - i]
for i in range(n):
    cure_sum_1 = 0
    for j in range(n):
        cure_sum_1 += a[j][i]
    if cure_sum_1 != cure_sum:
        exit(print("NO"))
if sum_d_2 == sum_d_1 == cure_sum:
    print("YES")
else:
    print("NO")

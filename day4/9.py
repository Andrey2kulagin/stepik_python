n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
flag = True
for i in range(n):
    for j in range(n):
        flag = a[i][j] == a[j][i]
        if not flag:
            exit(print("NO"))
print("YES")


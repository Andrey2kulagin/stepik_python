n = int(input())
m = int(input())
a = [[] for x in range(n)]
for i in range(n):
    for j in range(m):
        a[i].append(i*j)
for i in range(n):
    print(*a[i])

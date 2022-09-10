n = int(input())
m = int(input())
a = [[] for x in range(n)]
max_coord = [0, 0]
for i in range(n):
    a[i] = list(map(int, input().split()))
max_el = a[0][0]
for i in range(n):
    for j in range(m):
        if max_el < a[i][j]:
            max_el = a[i][j]
            max_coord = [i, j]
print(*max_coord)

n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    a[i][i], a[n-1-i][i] = a[n-1-i][i], a[i][i]
for i in range(n):
    print(*a[i])

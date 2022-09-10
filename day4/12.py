n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
for i in range(n):
    b = []
    for j in range(n):
        b.append(a[j][i])
    b.reverse()
    print(*b)

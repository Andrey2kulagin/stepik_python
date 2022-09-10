n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
max_el = a[0][0]
for i in range(n):
    for j in range(i+1):
        max_el = max(max_el, a[i][j])
print(max_el)

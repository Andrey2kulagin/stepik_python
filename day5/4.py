inp = input().split()
n = int(inp[0])
m = int(inp[1])
a = [[]for x in range(n)]
for i in range(n):
    for j in range(m):
        a[i].append(i+j*n+1)
for i in range(n):
    print(*a[i])

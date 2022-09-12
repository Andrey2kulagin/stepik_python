inp = input().split()
n = int(inp[0])
m = int(inp[1])
a = [[]for x in range(n)]
for i in range(n):
    if i%2==0:
        k = 1
    else: k = 2
    for j in range(m):
        if k%2==0:
            a[i].append('*')
        else:
            a[i].append('.')
        k+=1
for i in range(n):
    print(*a[i])

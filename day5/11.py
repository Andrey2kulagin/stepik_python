n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or i == (n-1-j) or i == (n//2) or j == (n//2):
            a[i].append('*')
        else:
            a[i].append('.')
for i in range(n):
    print(*a[i])

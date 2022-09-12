n = int(input())
a = [[]for x in range(n)]
for i in range(n):
    for j in range(n):
        if i < n-1-j:
            a[i].append(0)
        elif i == n-1-j:
            a[i].append(1)
        else:
            a[i].append(2)
for i in range(n):
    print(*a[i])

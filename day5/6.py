n = int(input())
a = [[]for x in range(n)]
for i in range(n):
    for j in range(n):
        if (i <= j and i <= n-1-j) or (i >= n-1-j and i>=j):
            a[i].append('1'.ljust(3," ")) 
        else: a[i].append('0'.ljust(3," "))
for i in range(n):
    print(*a[i])

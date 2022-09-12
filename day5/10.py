n = int(input())
a = [[]for x in range(n)]
for i in range(n):
    a[i]= list(map(int,input().split()))
max_el = a[n-1][n-1]
for i in range(n):
    for j in range(n):
        if i >= n-1-j:
            max_el = max(max_el, a[i][j])
print(max_el)

n = int(input())
m = int(input())
a = [[] for x in range(n)]
for i in range(n):
    for j in range(m):
        a[i].append(input())
for i in range(n):
    print(*a[i])
print()
for i in range(m):
    for j in range(n):
        print(a[j][i],end=" ")
    print()


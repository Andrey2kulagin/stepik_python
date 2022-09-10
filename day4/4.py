n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

for i in range(n):
    count_el = 0
    ar_mean = sum(a[i])/len(a[i])
    for j in range(n):
        if a[i][j] > ar_mean:
            count_el += 1
    print(count_el)

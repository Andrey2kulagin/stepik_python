n = int(input())
a = [[] for x in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))
sum_diagonal = 0
for i in range(n):
    sum_diagonal += a[i][i]
print(sum_diagonal)

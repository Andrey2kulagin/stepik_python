inp = input().split()
n = int(inp[0])
m = int(inp[1])
a = [[]for x in range(n)]
count = 1
for i in range(n):
    a[i]=[str(x).ljust(3,' ')for x in range(count,count+m)]
    count+=(m)
for i in range(n):
    print(*a[i])

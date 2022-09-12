inp = input().split()
n = int(inp[0])
m = int(inp[1])
count = 1
a = [[]for x in range(n)]
nums_arr  = [str(x).ljust(3," ") for x in range(1,m+1)]
for i in range(n):
    for j in range(m):
        a[i].append(str(count).ljust(3," "))
        count+=1
for i in range(n):
    if i%2==0:
        print(*a[i])
    else:
        a[i].reverse()
        print(*a[i])

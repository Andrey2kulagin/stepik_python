inp = input().split()
n = int(inp[0])
m = int(inp[1])
a = [[]for x in range(n)]
nums_arr  = [str(x).ljust(3," ") for x in range(1,m+1)]
for i in range(n):
    for j in range(i,m+i):
        a[i].append(nums_arr[j%(m)])
for i in range(n):
    print(*a[i])

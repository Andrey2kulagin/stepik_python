n = int(input())
a = []
i = 1
while i<=n:
    cure_arr = [x for x in range(1,i+1)]
    a.append(cure_arr)
    i+=1
for i in a:
    print(i)

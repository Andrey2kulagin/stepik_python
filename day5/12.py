n = int(input())
a = [[]for i in range(n)]
for i in range(n):
    a[i] = input().replace(" ","")
cure_str =""
for i in range(1,n+1):
    cure_str += str(i)
for i in a:
    for j in cure_str:
        if not(j in i):
            exit(print("NO"))
cure_str_1 = ""
for i in range(n):
    for j in range(n):
        cure_str_1 += a[j][i]
    for j in cure_str:
        if not(j in cure_str_1):
            exit(print("NO"))
print("YES")

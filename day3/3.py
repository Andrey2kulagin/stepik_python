import math
n = int(input())
flag = False
a = [1]
m = 1
if n==0:
    flag = True
while not flag:
    cure_el = math.factorial(n)/(math.factorial(m)*math.factorial(n-m))
    if cure_el ==1:
        flag = True
    a.append(int(cure_el))
    m+=1
print(a)

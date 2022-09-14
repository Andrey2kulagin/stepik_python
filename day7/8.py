import random
n = int(input())
inp = []
rand_set = set()
for i in range(n):
    inp.append(input())
flag = True
while flag:
    pair_arr = inp.copy()
    random.shuffle(pair_arr)
    for i in range(n):
        if inp[i]==pair_arr[i]:
            flag = True
            break
        flag = False
for i in range(n):
    print(inp[i]+" - "+pair_arr[i])
        


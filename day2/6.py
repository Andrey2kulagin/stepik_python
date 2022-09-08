inp = input().split()
swap_el = inp[-1]
for i in range(len(inp)-1,0,-1):
    inp[i] = inp[i-1]
inp[0] = swap_el
print(*inp)

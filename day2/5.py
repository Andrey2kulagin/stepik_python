inp = input().split()
inp_len = len(inp)
if inp_len%2!=0:
    inp_len-=1
for i in range(0,inp_len,2):
    inp[i],inp[i+1] = inp[i+1], inp[i]
print(*inp)

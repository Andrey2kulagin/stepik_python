inp = input().replace(" ","")
len_str = len(inp)
n = int(input())
out_arr = [[]for x in range(n)]
for i in range(n):
    for j in range(len_str):
        if j%n==0:
            
            out_arr[i].append(inp[j])
    inp = inp[1::]
    len_str-=1
print(out_arr)

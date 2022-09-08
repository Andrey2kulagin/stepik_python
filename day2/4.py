inp_arr = input().split()
len_arr = len(inp_arr)
bigger_count = 0
for i in range(len_arr-1):
    if int(inp_arr[i])<int(inp_arr[i+1]):
        bigger_count+=1
print(bigger_count)

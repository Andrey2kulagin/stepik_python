def massivchiki(inp, step):
    out_arr = []
    for i in range(0,len(inp)-step+1):
        cure_arr = []
        for j in range(step):
            cure_arr.append(inp[i+j])
        out_arr.append(cure_arr)
    return out_arr       
inp = input().replace(" ","")
out_arr = [[]]
for step in range(1,len(inp)+1):
    cure_arr = massivchiki(inp,step)
    out_arr.extend(cure_arr)
print(out_arr)

def chunked(inp, n):
    out_arr = []
    count = 0
    cure_arr = []
    for i in inp:
        count+=1
        cure_arr.append(i)
        if count == n:
            out_arr.append(cure_arr)
            cure_arr = []
            count = 0 
    if len(cure_arr)!=0:
        out_arr.append(cure_arr)
    return out_arr

inp = input().split()
n = int(input())
print(chunked(inp,n))

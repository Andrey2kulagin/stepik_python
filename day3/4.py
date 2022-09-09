inp = input().replace(" ","")+"a"
main_arr = []
cure_arr = []
for i in range(len(inp)-1):
    cure_el = inp[i]
    cure_arr.append(cure_el)
    next_el = inp[i+1]
    if next_el!= cure_el:
        main_arr.append(cure_arr)
        cure_arr = []
print(main_arr)

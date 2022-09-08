count = int(input())
nums_arr = []
anton_str = "anton"
for i in range(count):
    inp = input()
    symb_num = 0
    while inp!="" or inp==anton_str:
        if len(inp)<=5:
            break
        if symb_num<5 and inp[symb_num]==anton_str[symb_num]:
            #print(symb_num)
            symb_num+=1
        else:
            inp = inp[:symb_num]+ inp[symb_num+1::]
    if inp == anton_str :
        nums_arr.append(i+1)
print(*nums_arr)
    

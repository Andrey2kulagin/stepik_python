num = input()
num = num[::-1]
symb_count = 0
for i in range(0,len(num)+len(num)//3):
    if len(num)<=3 or num[-4]==',':
        break
    if num[i] in "0123456789":
        symb_count+=1
    if symb_count==3 :
        symb_count = 0
        num = num[0:i+1]+','+num[i+1::]
print(num[::-1])

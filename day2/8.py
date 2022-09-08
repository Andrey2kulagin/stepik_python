num_count = int(input())
num_arr = []
flag = False
for i in range(num_count):
    num_arr.append(int(input()))
c_num = int(input())
for i in range(num_count-1):
    if flag:
        break
    for j in range(i+1,num_count):
        if num_arr[i]*num_arr[j]==c_num:
            print("ДА")
            flag = True
            break
if not flag:
    print("НЕТ")

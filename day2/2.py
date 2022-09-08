count = int(input())
step = int(input())
arr = [i for i in range(1,count+1)]
i = 1
j = 0
len_arr = len(arr)
break_count = len(arr)-1
while arr.count('*')!=break_count:
    if i==step and arr[j]!='*':
        arr[j]='*'
        i=1
    if arr[j]!='*':
        i+=1
    j+=1
    if j>=len_arr:
        j = 0  
for i in arr:
    if i!='*':
        print(i)
        break

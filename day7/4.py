count = int(input())
acess_data_arr = {}
for i in range(count):
    inp = input().split()
    acess_data_arr[inp[0]]=inp[1:]
count1 = int(input())
s = {'write': 'W', 'read': 'R','execute': 'X'}
out_arr = []
for i in range(count1):
    inp = input().split()
    if s[inp[0]] in acess_data_arr[inp[1]]:
        out_arr.append("OK")
    else:
        out_arr.append("Access denied")
for i in out_arr:
    print(i)

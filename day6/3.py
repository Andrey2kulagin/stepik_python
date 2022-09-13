count = int(input())
len_arr = []
for i in range(count):
    len_arr.append(len(set(input().lower())))
for i in len_arr:
    print(i)

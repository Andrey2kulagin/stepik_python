count = int(input())
word_dict = {}
for i in range(count):
    s = input().split()
    word_dict[s[0]] = s[1:]
count1 = int(input())
find_arr = []
for i in range(count1):
    find_arr.append(input())
for j in find_arr:
    for i in word_dict:
        if j in word_dict[i]:
            print(i)


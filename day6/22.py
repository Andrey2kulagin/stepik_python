count = int(input())
word_dict = {}
for i in range(count):
    s = input().lower().split()
    if word_dict.get(s[1]) is not None:
        word_dict[s[1]].append(s[0])
    else:
        word_dict[s[1]] = [s[0]]
count1 = int(input())
find_arr = []
for i in range(count1):
    find_arr.append(input().lower())
for i in find_arr:
    print(*word_dict.get(i, ["абонент не найден"]))

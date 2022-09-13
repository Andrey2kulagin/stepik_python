count = int(input())
progger_dict = {}
for i in range(count):
    s = input().split(':')
    progger_dict[s[0].upper()] = s[1][1:]
count1 = int(input())
check_arr = []
for i in range(count1):
    check_arr.append(input().upper())
for i in check_arr:
    print(progger_dict.get(i, "Не найдено"))

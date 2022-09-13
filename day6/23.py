word_dict = {}
count_dict1 = {}
s1 = input()
for i in s1:
    count_dict1[i] = count_dict1.get(i, 0) + 1
count = int(input())
letter_dict = {}
for i in range(count):
    inp = input().split(":")
    letter_dict[inp[0]] = inp[1][1:]
for i in letter_dict:
    for j in count_dict1:
        if int(letter_dict[i]) == count_dict1[j]:
            s1 = s1.replace(j, i)
print(s1)

count = int(input())
word_dict = {}
for i in range(count):
    s = input().split()
    word_dict[s[0]] = s[1]
find_word = input()
for i in word_dict:
    if find_word == i:
        print(word_dict[i])
        break
    elif word_dict[i]==find_word:
        print(i)
        break

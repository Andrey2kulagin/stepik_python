s = input().split()
for i in range(len(s)):
    s[i]=s[i].lower().strip(".,!?:;-")
count_dict = {}
min_count = len(s)
word_min = ""
for i in s:
    count_dict[i] = count_dict.get(i,0)+1
for i, j in count_dict.items():
    if j<min_count:
        word_min = i
        min_count = j
    if min_count == j:
        word_min = min(word_min,i)
print(word_min)

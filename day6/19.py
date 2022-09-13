import re
s1 = re.sub(r'[ .,;:-?-!]', '', input()).lower()
s2 = re.sub(r'[ .,;:-?-!]', '', input()).lower()
print(s1,s2)
count_dict1 = {}
count_dict2 = {}
for i in s1:
    count_dict1[i] = count_dict1.get(i, 0) + 1
for i in s2:
    count_dict2[i] = count_dict2.get(i, 0) + 1
print("YES" if count_dict1 == count_dict2 else "NO")

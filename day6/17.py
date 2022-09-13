s = input().split()
count_dict = {}
for i in s:
    count_dict[i] = count_dict.get(i,0)+1

for i in count_dict:
    count = 0
    if count_dict[i]>1:
        for j in range(len(s)):
            if s[j]==i:
                if count>=1:
                    s[j]=s[j]+f"_{count}"
                count+=1
print(s)
    
    

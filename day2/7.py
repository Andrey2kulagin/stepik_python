inp = input().split()
diff_count = 0
for i in range(len(inp)-1):
    if inp[i]!=inp[i+1]:
        diff_count += 1
print(diff_count+1)

inp = ""
count = int(input())
for i in range(count):
    inp+=input().lower()
print(len(set(inp)))

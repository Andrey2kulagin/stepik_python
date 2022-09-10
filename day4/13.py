inp = input()
alf = "abcdefgh"
y = int(inp[1]) - 1
x = alf.find(inp[0])
a = [[] for l in range(8)]
for i in range(7, -1, -1):
    for j in range(8):
        down = (i - 2 == y and (j + 1 == x or j - 1 == x))
        up = (i + 2 == y and (j + 1 == x or j - 1 == x))
        right = (j - 2 == x and (i + 1 == y or i - 1 == y))
        left = (j + 2 == x and (i + 1 == y or i - 1 == y))
        if down or up or left or right:
            a[i].append("*")
        elif i == y and j == x:
            a[i].append("N")
        else:
            a[i].append(".")
for i in range(7, -1, -1):
    print(*a[i])

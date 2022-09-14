count = int(input())
byers_data_dict = {}
for i in range(count):
    inp = input().split()
    if byers_data_dict.get(inp[0])is not None:
        if byers_data_dict[inp[0]].get(inp[1]) is not None:
            byers_data_dict[inp[0]][inp[1]]+=int(inp[2])
        else:
            byers_data_dict[inp[0]][inp[1]] = int(inp[2])
    else:
        byers_data_dict[inp[0]] = {inp[1]:int(inp[2])}
for i in sorted(byers_data_dict):
    print(i+":")
    for j in sorted(byers_data_dict[i]):
        print(j,byers_data_dict[i][j])

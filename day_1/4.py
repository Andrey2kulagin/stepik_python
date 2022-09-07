num = input()
if len(num)==6:
    num = num[0]+num[-1:-6:-1]
else: num = num[::-1]
while num[0]=='0':
    num = num[1::]
print(num)

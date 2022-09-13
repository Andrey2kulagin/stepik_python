inp = input().split()
my_set = set()
for i in inp:
    i = i.strip('.,;:-?!')
    my_set.add(i.lower())
print(len(my_set))

inp = input().split()
my_set = set()
for i in inp:
    len1 = len(my_set)
    my_set.add(int(i))
    len2 = len(my_set)
    print("NO" if len2>len1 else "YES")

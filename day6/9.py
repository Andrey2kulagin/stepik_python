count = int(input())
a = []
for i in range(count):
    a.append(input())
my_set = set(a[0])
for i in a:
    my_set &= set(i)
print(*sorted(my_set))

my_set1 = set(list(map(int,input().split())))
my_set2 = set(list(map(int,input().split())))
count_nums = my_set1 - my_set2
print(*sorted(count_nums))

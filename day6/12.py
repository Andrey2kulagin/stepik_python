my_set1 = set(input().split())
my_set2 = set(input().split())
my_set3 = set(input().split())
my_set4 = my_set1 & my_set2 & my_set3
union_set = my_set1 | my_set2 | my_set3
print(*sorted(list(map(int,list(union_set-my_set4)))))

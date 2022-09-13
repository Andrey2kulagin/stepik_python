all_set = {'0','1','2','3','4','5','6','7','8','9','10'}
my_set1 = set(input().split())
my_set2 = set(input().split())
my_set3 = set(input().split())
union_set = my_set1 | my_set2| my_set3
print(*sorted(list(map(int,list(all_set-union_set)))))

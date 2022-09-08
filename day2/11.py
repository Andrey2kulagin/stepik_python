inp = input()
max_count = 0
cure_count = 0
for i in inp:
    if i == 'Р':
        cure_count +=1
        max_count = max(max_count, cure_count)
    else:
        cure_count = 0
print(max_count)        

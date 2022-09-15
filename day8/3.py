from decimal import *
num = Decimal(input())
nums=num.as_tuple()[1]
max_ =  max(nums)
min_ = 0
if -1<num<1:
    print(max_+min_)
else:
    min_ = min(nums)
    print(min_+max_)
print()




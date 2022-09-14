import random
my_set = set()
while len(my_set)<25:
    my_set.add(random.randint(1,75))
j = 0
for i in my_set:
    if(j in[5,10,15,20,25]):
        print()
    if j==12:
        print("0".ljust(3),end="")
    
    else:
        print(str(i).ljust(3),end="")

    j+=1

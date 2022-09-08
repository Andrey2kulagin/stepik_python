count = int(input())
result = [0,0,0,0]
for i in range(count):
    x,y = map(int,input().split())
    if x<0 and y>0:
        result[1]+=1
    elif x>0 and y>0:
        result[0]+=1
    elif x<0 and y<0:
        result[2]+=1
    elif x>0 and y<0:
        result[3]+=1
print("Первая четверть:",result[0])
print("Вторая четверть:",result[1])
print("Третья четверть:",result[2])
print("Четвертая четверть:",result[3])

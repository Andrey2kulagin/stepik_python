def str_without_letter(str,letter):
    while str.count(letter)>0:
        index = str.find(letter)
        str = str[:index]+str[index+1::]
    str = str.replace("  "," ")
    str = str.lstrip()
    str = str.rstrip()
    return str


alf = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
str = input()
str  += " запретил букву"
for i in alf:
    if len(str)==0:
        break
    if i in str:
        print(str,i)
    str = str_without_letter(str,i)
    
    

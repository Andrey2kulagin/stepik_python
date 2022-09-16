def print_products(*args):
    count = 1
    for i in args:
        if type(i) == str and len(i)!=0:
            print(f"{count}) {i}")
            count+=1
    if count==1:
        print("Нет продуктов")
def info_kwargs(**kwargs):
    for i in sorted(kwargs):
        print(f"{i}: {kwargs[i]}")

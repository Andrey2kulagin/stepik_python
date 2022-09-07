str_ = input()
price_cop = len(str_)*60
rub = price_cop//100
cop = price_cop%100
print(f"{rub} р. {cop} коп.")

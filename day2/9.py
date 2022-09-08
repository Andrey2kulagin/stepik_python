timur_choice = input()
ruslan_choice = input()
if timur_choice == ruslan_choice:
    print("ничья")
else:
    result_str = timur_choice+ruslan_choice
    if result_str in ("ножницыбумага","бумагакамень","каменьножницы"):
        print("Тимур")
    else:
        print("Руслан")

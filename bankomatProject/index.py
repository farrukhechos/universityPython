
# ATM project
card_password = 1221
enter_password = int(input("Enter the password: "))
card_balance = 44000

menu = ["Chek balance", "Take cash", "Connect to SMS", "Change password", "Pay for mobile phone", "payments for kredit","Communal payments", "Exit the progrram"]

if enter_password == card_password:
    menu_list = print(f"1: {menu[0]}", f"2: {menu[1]}", f"3: {menu[2]}", f"4: {menu[3]}", f"5: {menu[4]}",
                      f"6: {menu[5]}", f"7: {menu[6]}", f"8: {menu[7]}")
else:
    print("password incorrect")

choose  = int(input("Choose your option: "))
if choose == 1:
    print(f"You have {card_balance} so'm")
    print("If you want return, write 0")
    return_number = int(input("Return number: "))
    if return_number == 0:
        menu_list = print(f"1: {menu[0]}", f"2: {menu[1]}", f"3: {menu[2]}", f"4: {menu[3]}", f"5: {menu[4]}", f"6: {menu[5]}",f"7: {menu[6]}",f"8: {menu[7]}")


# 1:
# saved_password = 1221
# enter_password = int(input("Enter the password to enter: "))
# if enter_password == saved_password:
#     print("ok")
# else:
#     print("not ok")


# 2:
# number = int(input("enter number"))
# bir = number % 10
# on = number // 10 % 10
# yuz = number // 100 % 10
# check = on + bir
# if yuz > check:
#     print("zor")
# else :
#     print("Yomon")

#  3:
# grade = int(input("Enter the student's grade: "))
# result = ""
# if grade == 5:
#     result = "A"
# elif grade == 4:
#     result = "B"
# elif grade == 3:
#     result = "C"
# else:
#     result = "ABC"
#
# print(result)

# 4

menu = ["osh", "shorva", "mastave", "shashlik"]
price = [3200, 2400, 2460, 9800]

print("Menu")
print(f"1: {menu[0]}: {price[0]} som")
print(f"2: {menu[1]}: {price[1]} som")
print(f"3: {menu[2]}: {price[2]} som")
print(f"4: {menu[3]}: {price[3]} som")
#
# chooseFood = int(input("Choose a food: "))
#
#
# if chooseFood == 1:
#     print(f"1: {menu[0]}")
#     how_many_buy = int(input("How many buy: "))
#     enterPrice = int(input("Enter the price: "))
#     if enterPrice >= price[0] * how_many_buy:
#         print("Tayyor")
#     else:
#         print("You don't have enough money")
#
# elif chooseFood == 2:
#     print(f"1: {menu[1]}")
#     how_many_buy = int(input("How many buy: "))
#     enterPrice = int(input("Enter the price: "))
#     if enterPrice >= price[1] * how_many_buy :
#         print("Tayyor")
#     else:
#         print("You don't have enough money")
# elif chooseFood == 3:
#     print(f"1: {menu[2]}")
#     how_many_buy = int(input("How many buy: "))
#     enterPrice = int(input("Enter the price: "))
#     if enterPrice >= price[2] * how_many_buy:
#         print("Tayyor")
#     else:
#         print("You don't have enough money")
#
# elif chooseFood == 4:
#     print(f"1: {menu[3]}")
#     how_many_buy = int(input("How many buy: "))
#     enterPrice = int(input("Enter the price: "))
#     if enterPrice >= price[3] * how_many_buy:
#         print("Tayyor")
#     else:
#         print("You don't have enough money")

# 4: optimization

tanlovMenu = int(input("Tanlov menu: "))
if tanlovMenu >= 1 and tanlovMenu <= 4:
    print(f"Siz: {menu[tanlovMenu -1]}")

    sum = float(input("Sizda qancha pul bor: "))

    if sum >= price[tanlovMenu-1]:
        sum -= price[tanlovMenu-1]
        print(f"Siz: {menu[tanlovMenu-1]} sotib olasiz")
        print(f"Sizda {sum} qoldi")
    else:
        yetarli_emas = price[tanlovMenu-1] - sum
        print(f"Sizda {yetarli_emas} so'm kam")
else:
    print(f"1 dan 4 acha raqam tanlang:")
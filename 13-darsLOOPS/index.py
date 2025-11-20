from unicodedata import digit

# 1
# s = int(input("enter start number: "))
# f = int(input("enter finish number: "))
# for i in range(s+1, f):
#     print(i)


# -80 dan 80 gacha 7 ga karralilarini chiqaring

# for i in range(-77, 80, 7):
#     print(i)


# 3
# kg = 0
# for i in range(1, 11):
#     kg += 5000
#     print(i/10, kg, "Kg")


# 4
# fruits = ['apple', 'banana', 'orange']
# for fruit in fruits:
#     if fruit[-1] == 'e':
#         print(fruit)

# 5
# numbers = [2,4,5,6,7,8,11,-9, -4]
# bigger = numbers[0]
# for x in numbers:
#     if x > bigger:
#         bigger = x
#
# print(bigger)

# 6
# number = [1,2,3,4,5-6,-7,-8, 9, 19,0]
# musbat = []
# manfiy = []
#
# for x in number:
#     if x > 0:
#         musbat.append(x)
#     elif x < 0:
#         manfiy.append(x)
#
# print(musbat)
# print(manfiy)

# 7
# word = "My name is Farrukh and age 18"
#
# for x in word:
#     if x in "0123456789":
#         print(x)
# #






# # While
# parol_saved = 1111
# pass_parol = int(input("Enter your parola number: "))
#
# while pass_parol != parol_saved:
#     pass_parol = int(input("Enter your parola number: "))


# A kesmadagi uzunlikka b kesmadai nechta sig'adi

# a = int(input("Enter uzunlik: e.g 10 "))
# b = int(input("Enter uzunlik: e.g 4 "))
# count = 0
# newResult = 0
# while a >= b:
#     count += 1
#     newResult += b
#     if newResult == a:
#         print(count)


    # while a >= b:
    #     a -= b
    #     count += 1
    # print(count)

    # n = int(input("Enter a number: "))


    # ekranda 2ta qiymat kiritaman s va f s7 ga teng f 28

# start = int(input("Enter a start number: "))
# finish = int(input("Enter a finish number: "))
#
# for i in range(start, finish+1):
#         print(i)

# numbers = [1,2,390,34,8,9,123]
# print(numbers)
#
# x = int(input("Enter a number: "))
# check = False
# for number in numbers:
#     if number == x:
#         check = True
#         break
#
# if check:
#     print(f"{x} bor")
# else:
#     print(f"{x} yo'q")

# number = [1,2,3,4,5,6,7,8,-9,-2,-1]
#
# count = 0
# for i in number:
#     if i < 0:
#         count += 1
#
# print("Manfiy raqamlar", count)

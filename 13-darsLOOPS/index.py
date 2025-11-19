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
word = "My name is Farrukh and age 18"

for x in word:
    if x in "0123456789":
        print(x)
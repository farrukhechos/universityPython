# asosiy operation
# Masalalar

#1  Berilgan k sonining n - darajasini chiqaring
# k = int(input("Sonni kiriting"))
# n = int(input("Darajani kiriting"))
# calc = k ** n
# print(calc)

# assignments operation
# = += -+ /= //+ *= %=


 # compare
 # > < >= <= == True or False

# print(5 > 3)
# print(4 < 3)
# print(5 >= 5)
# print(5 == 5)
# print(5 != 8)

# 1-masala
# Son kiritilgan shu son musbat bolsa true chiqaring
# n = int(input("Son kiriting: "))
# check = n > 0
# print(check)

# 2-masala
# n = int(input("Son kiriting"))
# check = n != 0
# print(check)

# 3-masala
# 3 honali son kiritng, 3 honali sonni onlar honasi 0 ga teng bomasa true chiqairng
# n = int(input("Number"))
# onlik = n // 10 % 10
# check = onlik != 0
# print(check)

# 4-masala
# 2 xonali son berilgan: masalan, 23, 24, 34,68, shu sonlarning raqamlari yigindisi 5 dan katta bosa true chiqaring
# n = int(input("2 honali son kiriitng: "))
# birlik = n % 10
# onlik = n // 10 % 10
# check = birlik + onlik
# bigCheck = check > 5
# print(bigCheck)

# 5 masala
# 3 ta o'g'il bola bor: Ali, Nodir,  Sardor 3tasida N so'mdan pul bor. Lola da ham K sum bor.
# savol:3 ta bolaning summasi agar loladagi summadan 2 barobar katta bolsa true chisin

ali = int(input("ALi summa: "))
nodir = int(input("Nodir summa: "))
sardor = int(input("Sardor summa: "))
lola = int(input("Lola summm: "))
checkBoys = ali + nodir + sardor
lola *= 2
checkOverall = lola < checkBoys
print(checkOverall)


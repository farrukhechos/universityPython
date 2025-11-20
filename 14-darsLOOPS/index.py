# 1
# numbers = [1,2,3,4,5,6,7,8,0]
# count = 0
#
# for i in numbers:
#     if i % 2 ==0 and i != 0: # CHANGED + and condition
#          count += 1
#
# print("Juftlar", count)

# 2
# numbers = [1,2,3,4,5,6,7,8,0,-10,-4,-23,9, 22,44]
# count = 0
# for i in numbers:
#     if i < 10 and i > -10:
#         count += 1
# print(count)


# 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 0, -10, -4, -23, 9, 22, 44]
bigger = numbers[0]
for i in numbers:
    if i > bigger:
        bigger = i
print(bigger)


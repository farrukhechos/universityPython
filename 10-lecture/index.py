
# son kiritiladi 3 kiritiladi fizz chiqsin agar 5 ga bolsinza bazz, agar 3 va 5 ga bolinsa fizzbazz
number = int(input("Enter a number:"))

if number % 3 ==0:
    print("Fizz")
elif number % 5 ==0:
    print("Buzz")
elif number % 3 ==0 and number % 5 ==0:
    print("FizzBuzz")
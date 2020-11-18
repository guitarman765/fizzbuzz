# Create fizz buzz program that takes numbers 1 - 100 and prints fizz if the number is evenly divisible by 2
# Create fizz buzz program that takes numbers 1 - 100 and prints buzz if the number is evenly divisible by 3
# Create fizz buzz program that takes numbers 1 - 100 and prints fizzbuzz if the number is evenly divisible by 2 and 3


i = 1
while i < 100 + 1:
    if (i % 2 == 0) and (i % 3 == 0):
        print("FizzBuzz")
        i += 1
    elif i % 2 == 0:
        print("Fizz")
        i += 1
    elif i % 3 == 0:
        print("Buzz")
        i += 1
    else:
        print(i)
        i += 1
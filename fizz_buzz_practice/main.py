# Create A program that takes in a user defined number, two divisible by numbers and two keywords.
# The program checks every number up to the 1st user defined number.
# If the number is evenly divisible by the users 2nd input number the program prints a key word.
# If the number is evenly divisible by the users 3rd input number the program prints a second key word.
# If the number is evenly divisible by the both the users 2nd and 3rd input numbers a concatenated keyword is printed.

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
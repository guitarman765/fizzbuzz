# Create A program that takes in a user defined number, two divisible by numbers and two keywords.
# The program checks every number up to the 1st user defined number.
# If the number is evenly divisible by the users 2nd input number the program prints a key word.
# If the number is evenly divisible by the users 3rd input number the program prints a second key word.
# If the number is evenly divisible by the both the users 2nd and 3rd input numbers a concatenated keyword is printed.
def fizzbuzz():
    num1 = int(input("Please enter the number to stop at: "))
    num2 = int(input("Please enter the first divisible number: "))
    num3 = int(input("Please enter the second divisible number: "))
    wrd1 = input("Please enter the first divisible word: ")
    wrd2 = input("Please enter the second divisible word: ")
    # NO or anything other than yes will revert to the default naming of wrd3 (concatenation of wrd1 and wrd2)
    user_choice = input("Do you want to make up the divisible by both word or default (YES or NO): ")

    # If user types "YES", program takes in their custom word for divisible by num2 and num3.
    if user_choice == "YES":
        wrd3 = input("Enter custom word: ")
    else:
        wrd3 = str(wrd1) + str(wrd2)

    # Looping through the numbers.
    i = 1
    while i < num1 + 1:
        # If evenly divisible by both numbers.
        if (i % num2 == 0) and (i % num3 == 0):
            print(wrd3)
            i += 1
        # If evenly divisible by num2.
        elif i % num2 == 0:
            print(wrd1)
            i += 1
            # If evenly divisible by num3.
        elif i % num3 == 0:
            print(wrd2)
            i += 1
        # If evenly divisible by neither num2 or num3.
        else:
            print(i)
            i += 1

fizzbuzz()
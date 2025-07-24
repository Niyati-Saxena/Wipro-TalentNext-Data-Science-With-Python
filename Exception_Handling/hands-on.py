# Write a program to accept two numbers from the user and perform division. If any exception occurs, print an error message, otherwise print the result.
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = num1 / num2
    print("Result:", result)
except Exception as e:
    print("Error:", str(e))
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to accept a number from the user and check whether it’s prime or not.If user enters anything other than a number, handle the exception and print an error message.
try:
    num = int(input("Enter a number: "))
    if num < 2:
        print("Not a prime number.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                break
        else:
            print("Prime number.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to accept a file name from the user.If the file exists, print its contents in title case. Otherwise, handle the exception and print an error message.
try:
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        for line in file:
            print(line.title(), end="")
except FileNotFoundError:
    print("Error: File not found.")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Declare a list with 10 integers and ask the user to enter an index.Check whether the number in that index is positive or negative.If an invalid index is entered,
# handle the exception and print an error message.
nums = [3, -7, 12, -1, 0, 8, -4, 6, -9, 10]
try:
    index = int(input("Enter index (0–9): "))
    value = nums[index]
    if value > 0:
        print("Positive number.")
    elif value < 0:
        print("Negative number.")
    else:
        print("Zero.")
except IndexError:
    print("Error: Index out of range.")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")

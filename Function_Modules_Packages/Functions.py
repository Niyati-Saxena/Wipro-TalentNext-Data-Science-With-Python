#----------------------------------------------------------------------------------------------------------------
#----------------------------------------------FUNCTIONS---------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------
# Write a function to return the sum of all numbers in a list.
def sum_of_list(numbers):
    return sum(numbers)
#-----------------------------------------------------------------------------------------------------------------
# Write a function to return the reverse of a string.
def reverse_string(text):
    return text[::-1]
#-------------------------------------------------------------------------------------------------------------------
# Write a function to calculate and return the factorial of a number (a non-negative integer).
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
#-----------------------------------------------------------------------------------------------------------------
# Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.
def count_case_letters(text):
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)
#-----------------------------------------------------------------------------------------------------------------
# Write a function to print the even numbers from a given list. List is passed to the function as an argument.
def print_even_numbers(numbers):
    evens = [n for n in numbers if n % 2 == 0]
    print("Even numbers:", evens)
#---------------------------------------------------------------------------------------------------------------
# Write a function that takes a number as a parameter and checks whether the number is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Write a program to check if a given number is Positive, Negative or Zero.
num = int(input("Enter the number: "))
if num > 0 :
    print("Positve")
elif num < 0:
    print("Negative")
else :
    print("zero")     
# ---------------------------------------------------------------------------------------
# Write a program to check if a given number is odd or even.
num = int(input("Enter the numeber: "))
if num % 2 == 0:
    print("Even")
else :
    print("Odd")  
# -----------------------------------------------------------------------------------------------------
# Given two non-negative values, print true if they have the same last digit, such as with 27 and 57
num1 = int(input("Enter 1st number: ")) % 10
num2 = int(input("Enter 2nd number: ")) % 10

if num1 == num2:
    print("True")
else :
    print("False")    
# ------------------------------------------------------------------------------------------------------
# Write a program to print numbers from 1 to 10 in a single row with one tab space.
for i in range(1,11):
    print(i , end="\t")
# -----------------------------------------------------------------------------------------------------------
# Write a program to print even numbers between 23 and 57. Each number should be printed in a seperate row.
for i in range(23 , 58) :
    if(i % 2 != 0):
        continue
    print(i)
# --------------------------------------------------------------------------------------------------------------
# Write a program to check if a given number is prime or not.
def isPrime(n) :
    if n < 2 : 
        return "Prime"
    for i in range(2 , int(n ** 0.5)+1):
        if n % i == 0:
            return "Not prime"
    return "Prime"    

num = int(input("Enter a number: "))
print(isPrime(num))   
# -------------------------------------------------------------------------------
# Write a program to print prime numbers between 10 and 99.
for i in range(10 ,100):
    if ("Prime" == isPrime(i)):
        print(i)
# -------------------------------------------------------------------------------
# Write a program to print the sum of all the digits of a given number.
num = int(input("Enter the number: "))
sum = 0
while num > 0:
    sum += num % 10
    num = num // 10
print(sum)  
# --------------------------------------------------------------------------------
# Write a program to reverse a given number and print
def isReverse(num):
    isNegative = num < 0
    num = abs(num)
    revnum = 0 
    while num > 0:
        revnum *= 10
        revnum += num % 10
        num //= 10
    return -revnum if isNegative else revnum  

n = int(input("Enter the number: "))
print(isReverse(n)) 
# -----------------------------------------------------------------------------------
# Write a program to find if the given number is palindrom or not.
num = int(input("Enter a number: "))
if (num != isReverse(num) or num < 0):
    print("Not a Palindrome")
else :
    print("Palindrome")  

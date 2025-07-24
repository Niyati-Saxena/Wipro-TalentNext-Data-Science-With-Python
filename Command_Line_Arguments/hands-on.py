# Write a program to accept two numbers as command line arguments and display their sum.
import sys
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
print("Sum:", num1 + num2)
#---------------------------------------------------------------------------------------------------------------------------------------
# Write a program to accept a welcome message through command line arguments and display the file name along with the welcome message.
import sys
message = ' '.join(sys.argv[1:])
print("File name:", sys.argv[0])
print("Welcome message:", message)
#----------------------------------------------------------------------------------------------------------------------------------------
# Write a program to accept 10 numbers through command line arguments and calculate the sum of prime numbers among them.
import sys
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5)+1):
        if n % i == 0:
            return False
    return True

numbers = list(map(int, sys.argv[1:]))
prime_sum = sum(n for n in numbers if is_prime(n))
print("Sum of prime numbers:", prime_sum)

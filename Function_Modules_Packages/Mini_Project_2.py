# We have to write a Python module with three functions:
# ispalindrome(name): It accepts the user name and returns whether the name is a palindrome or not.
# count_the_vowels(name): It accepts the user name and returns how many vowels are present in the name.
# frequency_of_letters(name): It accepts the user name and returns the frequency of each letter in the name.
# You have to import this module in another script and test all the functions.
# Sample Input 1: bob
# Sample Output 1:
# Yes it is a palindrome.
# No of vowels: 1
# Frequency of letters: b-2, o-1

# The functions will be defined in student_utils.py
def ispalindrome(name):
    return name == name[::-1]

def count_the_vowels(name):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in name if char in vowels)

def frequency_of_letters(name):
    freq = {}
    for char in name:
        freq[char] = freq.get(char, 0) + 1
    return freq

# the functions will be imported in main.py file 
import student_utils

name = input("Enter name: ")

if student_utils.ispalindrome(name):
    print("Yes it is a palindrome.")
else:
    print("No it is not a palindrome.")

print("No of vowels:", student_utils.count_the_vowels(name))

freq = student_utils.frequency_of_letters(name)
print("Frequency of letters:")
for letter, count in freq.items():
    print(f"{letter}-{count}")

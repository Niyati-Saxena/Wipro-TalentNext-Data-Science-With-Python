#---------------------------------------------------------------------------------------------------------
#-------------------------------------STRING--------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
# WAP to count the number of upper and lower case letters in a string 
string = "HEllo Everybody"
# using list comprehension
count_lower = sum(1 for ch in string if ch.islower())
count_upper = sum(1 for ch in string if ch.isupper())  
print("Lowercase letters:" , count_lower)
print("Uppercase letters:" , count_upper)  
# ---------------------------------------------------------------------------------------------------------      
# WAP to check whether the given string is palindrome or not
string = input("Enter a string: ")
if string == string[::-1]:    # reverse and compare 
    print("Palindrome String")
else :
    print("Not a palindrome")   
# ---------------------------------------------------------------------------------------------------------     
# Given a String , return a new string made of n copies of the first 2 chars of the original string where n 
# is the length of the string. The string length >= 2
# I/P - Wipro 
# O/P - WiWiWiWiWi
s = input("Enter the string: ")
result = s[:2] * len(s)
print(result)  
# -------------------------------------------------------------------------------------------------------------
# Given a string, if the first or last character is 'x',return the string without those 'x' characters, else
# return string unchanged
# I/P - xHix
# O/P - Hi
s = input("Enter a string: ")
if s.startswith('x'):
    s = s[1:]
if s.endswith('x'):
    s = s[:-1]
print(s)
#---------------------------------------------------------------------------------------------------------------
# Given a string and an integer n, return a string made of n repitations of the last n characters of the string. n 
# is between o to length of string inclusive 
# I/P - Wipro 3
# O/P - propropro
s = input("Enter a string: ")
n = int(input("Enter an integer (should lie within the length of string): "))
result = s[-n:] * n
print(result)

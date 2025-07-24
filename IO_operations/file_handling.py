# Write a program to read the entire content from a txt file and display it to the user.
with open("sample1.txt", "r") as file:
    content = file.read()
    print(content)
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to read first n lines from a txt file. Get n as user input.
n = int(input("Enter number of lines to read: "))
with open("sample2.txt", "r") as file:
    for i in range(n):
        print(file.readline(), end="")
#-----------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to accept input from user and append it to a txt file.
text = input("Enter text to append: ")
with open("sample3.txt", "a") as file:
    file.write(text + "\n")
#------------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to read contents from a txt file line by line and store each line into a list.
with open("sample4.txt", "r") as file:
    lines = file.readlines()
print(lines)
# ------------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
with open("sample5.txt", "r") as file:
    words = file.read().split()
longest = max(words, key=len)
print("Longest word:", longest)
#--------------------------------------------------------------------------------------------------------------------------------------------------
# Write a program to count the frequency of a user entered word in a txt file.
target = input("Enter word to count: ")
with open("sample6.txt", "r") as file:
    text = file.read()
count = text.split().count(target)
print(f"The word '{target}' appears {count} times.")

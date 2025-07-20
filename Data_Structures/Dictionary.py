#---------------------------------------------------------------------------------------------------------
#-------------------------------------DICTIONARY----------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
# WAP to add a key and value to the dictionary
dict1 = {
    "a" : 200 , 
    "b" : 450 , 
    "c" : 980
} 
dict1["d"] = 670
print(dict1)
# ----------------------------------------------------------------------------------------------------------
# WAP to concatenate the given dictionaries
dic1 = {1 : 10 , 2 : 20}
dic2 = {3 : 30 , 4 : 40}
dic3 = {5 : 50 , 6 : 60}
dic4 = {}
dic4.update(dic1)
dic4.update(dic2)
dic4.update(dic3)
print(dic4)
# ----------------------------------------------------------------------------------------------------------
# WAP to check if a given key is already present in the dictionary
n = int(input("Enter the key to be found: "))
if n in dic4:
    print("key is present")
else:
    print("key is not present")    
# -----------------------------------------------------------------------------------------------------------
# WAP to iterate over a dictionary and print keys alone , values alone and key-value both
dict1 = {"a" : 200 , "b" : 450 , "c" : 980}
print("The keys in the dictionary are: ")
for k in dict1.keys():  
    print(k) 
print("The values in the dictonary are: ")
for k in dict1.values():   
    print(k)
print("The key-value pairs in the dictionary are: ")
for k in dict1.items():   
    print(k)
# ------------------------------------------------------------------------------------------------------------
# WAP to prepare a dcitionary where the keys are numbers from [1,15] and the values are the square of the keys
dict = {}
for i in range(1,16):
    dict[i] = i*i
print(dict)
# or by using dictionary comprehension 
dict = {i : i*i for i in range(1,16)}
print(dict)
# ----------------------------------------------------------------------------------------------------------------
# WAP to sum all the values in the dictionary, given the values are of int type
dict1 = {"a" : 200 , "b" : 450 , "c" : 980}
print(sum(dict1.values()))

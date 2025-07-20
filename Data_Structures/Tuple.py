#---------------------------------------------------------------------------------------------------------
#-------------------------------------TUPLE---------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
# WAP to print 4th element from first and 4th element from last
tup = (1,2,3,4,5,6,7)
print("Fourth element from first:" , tup[3])
print("Fourth element from last:" , tup[-4]) 
# ---------------------------------------------------------------------------------------------------------
# WAP to check whether an element exsits in a tuple or not
tup = (1,2,3,4,5,6,7)
n = int(input("Enter element to check: "))
if n in tup :
    print("Element present")
else :
    print("Element not present")    
# ---------------------------------------------------------------------------------------------------------
# WAP to convert a list into tuple
list1 = ['d', 4.6 , 2 , "hello"]
tup = tuple(list1)
print(type(tup))
# ---------------------------------------------------------------------------------------------------------
# WAP to find the index of an item in the tuple
tup = (1,2,3,4,5,6,7)
print(tup.index(5))
# ---------------------------------------------------------------------------------------------------------
# WAP to replace the last value of tuples in a list to 100
list1 = [(10,20,40) , (40,50,60) , (70,80,90)]
# using list comprehension    
list1 = [ t[:-1] + (100,) for t in list1]
print(list1)

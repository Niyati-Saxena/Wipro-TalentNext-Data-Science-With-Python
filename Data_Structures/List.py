#---------------------------------------------------------------------------------------------------------
#-------------------------------------LIST----------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------
# WAP  to create a list of 5 integers and display the list items.Access individual elements through index
lst = [1,2,3,4,5]
print(lst[0]) # print(lst[-5])
print(lst[1]) # print(lst[-4])
print(lst[2]) # print(lst[-3])
print(lst[3]) # print(lst[-2])
print(lst[4]) # print(lst[-1])
# -----------------------------------------------------------------------------------------------------------
# WAP to append a new item to the end of the list
lst.append(9)
print(lst)
# -----------------------------------------------------------------------------------------------------------
# WAP to reverse the order of the items in the list
lst.reverse()
print(lst)
# -----------------------------------------------------------------------------------------------------------
# WAP to print the number of occurance of a specified element in a list
lst1 = [1,2,3,4,5,9,7,5,4,5,2]
print(lst1.count(5))
# ----------------------------------------------------------------------------------------------------------
# WAP to append the items of list1 to list2 in the front
list1 = [1,2,3,4]
list2 = [11,12,13,14]
for i in reversed(list1):
    list2.insert(0,i)
print(list1)
print(list2)    
# ----------------------------------------------------------------------------------------------------------
# WAP to insert a new element before the second element in an existing list
list1 = [1,2,3,4]
list1.insert(1,70)
print(list1)
# ---------------------------------------------------------------------------------------------------------
# WAP to remove the item from a specified index in a list
list1.pop(1)
print(list1)
# ---------------------------------------------------------------------------------------------------------
# WAP to remove the fisrt occurance of a specified element from a list
lst1 = [1,2,3,4,5,9,7,5,4,5,2]
lst1.remove(5)   
print(lst1) 

#We can also check the conditon in list comprehension like:


from hashlib import new


fruits = ["apple","banana","cherry","kiwi","mango"]

mylist =[x for x in fruits if x != "apple"] 

print(mylist) #The condition if x != "apple"  will return True for all elements 
              #other than "apple", making the new list contain all fruits except "apple".



# The condition is optional and can be omitted: i.e 
# With no if statement: 
# newlist = [x for x in fruits]   Output: ["apple","banana","cherry","kiwi","mango"]


# Example
# WE can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)
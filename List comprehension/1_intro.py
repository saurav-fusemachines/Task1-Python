# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

#SYNTAX: [expresion for item in iterable if condition == True]

#EXAMPLE: Without list comprehension
#Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits=["apple","banana","cherry","kiwi","mango"]
mylist = []

for x in fruits:
    if "a" in x:
        mylist.append(x)

print(mylist)


#EXAMPLE: With the use of List Comprehension
fruits = ["apple","banana","cherry","kiwi","mango"]
mylist = [x for x in fruits if "a" in x]
print(mylist)
# Python is an object oriented programming language.
# Almost everything in Python is an object, with its properties and methods.
# A Class is like an object constructor, or a "blueprint" for creating objects.

#Create a Class
# To create a class, we use the keyword class:
class Myclass:
    x = 5          #Create a class named MyClass, with a property named x.
print(Myclass)     #O/P: <class '__main__.Myclass'>

print()
# **************************************************************************************

# Create Object
# Now we can use the class named MyClass to create objects:
p1 = Myclass()
print(p1.x)

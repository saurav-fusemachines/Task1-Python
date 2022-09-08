#  The examples in '1_class_intro.py' are classes and objects in their simplest form, and are not really useful in real life applications.
# To understand the meaning of classes we have to understand the built-in __init__() function.
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

#Example:
from select import select


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person("John",36)

print("Name: ",p1.name)
print("Age: ",p1.age)
# Note: The __init__() function is called automatically every time the class is being used to create a new object.



#Example : Object Methods
#Objects can also contain methods. Methods in objects are functions that belong to the object.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Rhagel", 40)
p1.myfunc()
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


#THE SELF PARAMETER
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

#EXAMPLE:
print()
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Tanjiro", 18)
# p1.age = 20  #We can aslo modify the properties of an object.
#del p1.age    #We can also delete properties on objects by using the del keyword
#del p1        #We can also delete object by using del keyword
p1.myfunc()

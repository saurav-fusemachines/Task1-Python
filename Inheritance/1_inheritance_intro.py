# Inheritance is a powerful feature in object oriented programming.
# It refers to defining a new class with little or no modification to an existing class. The new
# class is called derived (or child) class and the one from which it inherits is called the base (or parent) class.

# Python Inheritance Syntax:
# class BaseClass:
#     # Body of base class
# class DerivedClass(BaseClass):
#     Body of derived class.

#EXAMPLE:


class Animal:
    def eat(self):
        print("Dog & cat can eat.")

class Dog(Animal):
    def bark(self):
        print("Dog can bark")

class Cat(Animal):
    def get_grumpy(self):
        print("Cat sound is meow.")

dog1 = Dog()
dog1.bark()
dog1.eat()

cat1 = Cat()
cat1.get_grumpy()
cat1.eat()


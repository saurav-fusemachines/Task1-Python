import math
def add_number(a,b):
    '''Takes the two parameters
        and returns the sum
    '''
    return a+b

print("The Sum is:", add_number(5,10))
print(add_number.__doc__) #Print the string define inside the add_number functions

#Basically doc string is the multi line comment written inside the function,classes, modules and so on
#While we hoover over the add_number fuction, it displays the comment written inides the function.
#While writing doc string it always should be first line inside class, modules, functions etc.

    
#We can also print the build in doc string like
print(math.__doc__)
print(math.sqrt.__doc__)
'''
A function is a block of code which only runs when it is called. We can pass data,
known as parameters, into a function. A function can return data as a result.
'''

#Creating a function
def function_1():
    print("Creating a function 1")

#Calling a function
function_1()    

#Arguments
'''Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. 
We can add as many arguments as you want, just separate them with a comma.'''
def area(length,breadth):
    print(length * breadth)

area(2,5)
area(5.5,9)
'''
Python has an interesting feature called decorators to add functionality to an existing code.     
In Python, a function can take another function as an argument.  
'''

#Example1:
from unittest import result


def first(msg):
    print(msg)

first("Hello! Saurav.")   

second=first
second("A Data Engineer")


# **********************************************************************
#Example 2
def inc(x):
    return x + 1

def operate(func,x):
    result = func(x)
    return result

print(operate(inc,3))

# ************************************************************************
#Example 3

def msg_func(message):
    greeting = "Hello"
    
  
    def printer():
        print(greeting, message)
    
    printer()

msg_func("Python is awesome programming language.")
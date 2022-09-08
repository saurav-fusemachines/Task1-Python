'''
In Python, we can pass a variable number of arguments to a function using special symbols. There are two special symbols:
*args (Non Keyword Arguments)
**kwargs (Keyword Arguments)
We use *args and **kwargs as an argument when we are unsure about the number of arguments to pass in the functions.

In the function, we should use an asterisk * before the parameter name to pass variable length arguments.The arguments are passed as a tuple and these passed 
arguments make tuple inside the function with same name as the parameter excluding asterisk *.
'''

#EXAMPLE 1:
def adder(*num):
    sum = 0
  
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)


#EXAMPLE 2:
def house_of_the_dragon(*heir):
    king=""
    for kings in heir:
        king = heir
    print(king)        

house_of_the_dragon("Agon")
house_of_the_dragon("Viserys","Viserion")
house_of_the_dragon("Ayres","Daemon","Rhaegal")

# In the above program, we used *num as a parameter which allows us to pass variable length argument list to the adder() function. Inside the function,
#  we have a loop which adds the passed argument and prints the result. We passed 3 different tuples with variable length as an argument to the function.


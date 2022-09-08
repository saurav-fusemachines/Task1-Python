'''
Python passes variable length non keyword argument to function using *args but we cannot use this to pass keyword argument.
For this problem Python has got a solution called **kwargs, it allows us to pass the variable length of keyword arguments to the function.

In the function, we use the double asterisk ** before the parameter name to denote this type of argument. The arguments are passed as a 
dictionary and these arguments make a dictionary inside function with name same as the parameter excluding double asterisk **.
'''

# EXAMPLE: Using **kwargs to pass the variable keyword arguments to the function 

def intro(**data):
    print("\nData type of argument: ",type(data))

    for key, value in data.items():
        print("{} : {}".format(key,value))

intro(Firstname ="Sita",Lastname ="Sharma", Age = 22, Phone = 1234567890)
intro(Firstname = "John", Lastname = "Wick", Email = "john.wick@gmail.com", Country = "Wakanda", Age = 25, Phone = 9787776757)

# In the above program, we have a function intro() with **data as a parameter. We passed two dictionaries with variable argument length to the intro() function.
#  We have for loop inside intro() function which works on the data of passed dictionary and prints the value of the dictionary.


# Things to Remember:
# *args and **kwargs are special keyword which allows function to take variable length argument.
# *args passes variable number of non-keyworded arguments and on which operation of the tuple can be performed.
# **kwargs passes variable number of keyword arguments dictionary to function on which operation of a dictionary can be performed.
# *args and **kwargs make the function flexible.
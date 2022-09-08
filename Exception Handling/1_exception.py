'''
In Python, exceptions can be handled using a try statement.

The critical operation which can raise an exception is placed inside the try clause. The code that handles the exceptions is written in the except clause.

We can thus choose what operations to perform once we have caught the exception. Here is a simple example.
'''


try:
    #code that may cause exception
    numerator = int(input("Enter numerator: "))
    denominator =int (input("Enter denominator: "))
    
    result = numerator//denominator
    print(result)

except:
    #code to run when exception occurs
    print("Denominator cannot be 0. Please try again")

finally:
    print("Program ends.")


#from avobe program if we add 'execpt ZeroDivisionError:' block of except only handles when the denominator is 0.
# In case if other error occured then 'except ZeroDivisionError' block will not handle other errors.


#Handling multiple exception 
try:
    #code that may cause exception
    numerator = int(input("Enter numerator: "))
    denominator =int (input("Enter denominator: "))
    
    result = numerator//denominator
    print(result)

    my_list = [1,2,3]
    i = int(input("Enter an index value: "))
    print(my_list[i])

except ZeroDivisionError:
    #code to run when exception occurs
    print("Denominator cannot be 0. Please try again")


except IndexError:
    print("Index cannot be greater than size of list")

finally:
    print("Program ends.")
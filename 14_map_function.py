'''
The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
'''

def my_func(x):
    return len(x)
fruits =['apple', 'banana', 'cherry']
x = map(my_func,fruits)

print(x)         #output : <map object at 0x000001B01657BE50>
print(list(x))   #Output: [5, 6, 6]

#Example 2
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))    #output: ['appleorange', 'bananalemon', 'cherrypineapple']
# The filter() function returns an iterator were the items are
#  filtered through a function to test if the item is accepted or not.

#SYNTAX filter(function,iterable)

#Example



def myFunc(x):
    if x<18:   
        return False
    else:
        return True

ages = [5,10,17,18,24,32]

adults = filter(myFunc,ages)

for a in adults:
    print(a)
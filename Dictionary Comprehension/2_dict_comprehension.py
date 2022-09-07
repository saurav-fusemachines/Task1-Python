# We can also use dictionary comprehension using data from another dictionary.
#Example
#item price in dollars

old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}
dollar_to_pound = 0.76
new_price = {item:value * dollar_to_pound for (item,value) in old_price.items()}
print(new_price)  #O/P: {'milk': 0.7752, 'coffee': 1.9, 'bread': 1.9}

# *****************************************************************************************************

#Conditionals in Dictionary Comprehension
# We can further customize dictionary comprehension by adding conditions to it. Let's look at an example.
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)   #O/P: {'jack': 38, 'michael': 48}

# *******************************************************************************************************

#Multiple if Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

# *********************************************************************************************************

# if-else Conditional Dictionary Comprehension
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)              #O/P: {'jack': 'young', 'michael': 'old', 'guido': 'old', 'john': 'young'}


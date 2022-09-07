## Dictionary comprehension also offers a shorter syntax when you want to create a new dictionary
#  based on the values of an existing list.

#EXAMPLE: Without using dictionary comprehension
square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)      #O/P: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}


#EXAMPLE: With using dictionary comprehesion
#SYNTAX : dictionary = {key: value for vars in iterable}
square_dict = {num:num*num for num in range(1,11)}
print(square_dict)       #O/P: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

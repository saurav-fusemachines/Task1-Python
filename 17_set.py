from doctest import OutputChecker


s = set()
# print(type(set))
list = [9,'Karim Benzema',12]
set_from_list = set(list)
print(set_from_list)   # Output: {9, 'Karim Benzema', 12}

#Add value or data in set
s.add(1)
print(s)          #Output: {1}

#Set does not append the duplicate values. 
s.add(1)
s.add(1)
s.add(10)
print(s)        #Output: {1,10}

#We can also use diffrent set functions like min(),max(),union(),intersection(),len(), diffrence(),
#symmetric_difference(),pop(),issubset() and many more
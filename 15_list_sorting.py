# EXAMPLE 1
even= [2,4,6,8]
odd = [1,3,5,7,9]

print("Even number list: {}".format(even))
print("Odd number list: {}".format(odd))


even.extend(odd)
print("items form odd extended to even")
print(even)      # [2, 4, 6, 8, 1, 3, 5, 7, 9] extends joins the other list of odd but in un-sorted

even.sort()
print("Items from even and odd with sorting: {}".format(even))

even.sort(reverse=True)
print("Items sorted in reverse order: {}".format(even))
print(even)


# EXAMPLE 2
pangram = "The quick brown fox jumps over the lazy dogs"

letters=sorted(pangram) #sorts the item but duplicate the same items
print(letters)
print

numbers=[2.3,4.5,8.7,3.1,9.2,1.6]
sorted_numbers=sorted(numbers)
print(sorted_numbers)
print()

#DIFFERENCE BETWEEN SORT AND SORTED IS THAT SORT METHOD DIRECTLY SORT THE DEFINED VARIALBLE 
#BUT IN CASE OF SORTED, NEW VARIABLE IS DEFINED AS SORT THE ITEMS AAVAILABLE IN LIST

#above there is jumps and dogs i.e 2 's' this case hase jumped and dogs only one 's'
missing_letter=sorted("The quick brown fox jumped over the lazy dogs",key=str.casefold)  #key=str.casefold sort the Case_insensitive string 
print(missing_letter)
print()

names=["Benzema","Bale","Hazard","isco","Velverde","Casemiro","Alaba","Nacho","Militao","carvajal","Courtious"]
names.sort(key=str.casefold)
print(names)

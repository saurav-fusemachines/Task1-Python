 #List is a sequenced order items represented in square brackets
computer_parts = ["computer","monitor","keyboard","mouse","mouse mat"] 

for part in computer_parts:
    print(part)

print()
print(computer_parts[2])

print(computer_parts[0:3])   #List can also be sliced samme as strings.
print(computer_parts[-1])    #Python idiom that returns the last items in the list


#MUTABLE:
# A mutuable object is one whose value can be changed
# Python has the following mutuable objects:
#  list, dict,  set, bytearray

shoppinglist= ["milk","pasta", "egg","spam","bread","rice"]

another_list = shoppinglist
print(id(shoppinglist))
print(id(another_list))

shoppinglist += ["Cookies"]    #Concatenate at the end of list
print(shoppinglist)            # O/P: ['milk', 'pasta', 'egg', 'spam', 'bread', 'rice', 'Cookies']
print(id(shoppinglist))        #give same id as above list because list are mutuable, Python can able to change the contents  of the list without creating new one.

# #STRING ARE 'IMMUTABLE'. WHEN WE TRY TO CHANGE A STRING, PYTHON CREATES THE NEW OBJECT -a NEW STRING - AND RE-ATTACHETED A NAME TO IT.
print("*"*80)
a = b = c = d = e = f = another_list  #Binding Multiple name to a List.
print(a)
print("Adding new item to a list that is 'Pasta'")
b.append("Pasta")
print(c)
print(f)
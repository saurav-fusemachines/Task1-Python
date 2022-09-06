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
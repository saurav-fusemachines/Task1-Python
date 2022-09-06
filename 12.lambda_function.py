# def double(n):
#     return n*2

from tokenize import Double


double = lambda n:n*2
print(double(10))
print()

larger = lambda a,b: a if a>b else b
print(larger(200,150))

# The power of lambda is better shown when you use them as an anonymous function inside another function.

# Program to filter out only the even items from a list
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(filter(lambda x: (x%2 == 0) , my_list))

print(new_list)
from hashlib import new


def reverse_number(n):
    new_string = str(n)
    if '-' in new_string:
        new_string = new_string[1:]
        return int('-'+new_string[::-1])
    else:
        return int(new_string[::-1])
     
print(reverse_number(456))
print(reverse_number(-123))
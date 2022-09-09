def special_number(number):
    special_numbers = [0,1,2,3,4,5]
    new_digits = [int(d) for d in str(number)]
    for digit in new_digits:
        if digit not in special_numbers:
            return "NOT!!"
    return "Special!!"
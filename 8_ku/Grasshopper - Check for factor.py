def check_for_factor(base, factor):
    # your code here
    if base % factor == 0:
        return True
    else:
        return False

print(check_for_factor(10,2))
print(check_for_factor(99,5))
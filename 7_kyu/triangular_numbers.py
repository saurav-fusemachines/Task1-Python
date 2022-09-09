def is_triangular(t):
    level = 1
    while t > 0:
        t -=level
        level += 1
    return t ==0

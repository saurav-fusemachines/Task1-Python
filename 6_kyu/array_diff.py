def array_diff(a, b):
    b = set(b)
    return [res for res in a if res not in b]


# def array_diff(a, b):
#     return [x for x in a if x not in b]


# def array_diff(a, b):
#     return filter(lambda i: i not in b, a)
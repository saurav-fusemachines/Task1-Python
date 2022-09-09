def grow(arr):
    mul = 1
    for x in arr:
        mul = mul * x
    return mul
    
print(grow([1,2,3]))
print(grow([4, 1, 1, 1, 4]))

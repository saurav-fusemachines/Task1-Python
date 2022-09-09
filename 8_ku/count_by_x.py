def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    arr=[]
    for i in range(1,n+1):
        arr.append(i*x)
    return arr
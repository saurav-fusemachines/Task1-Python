def max_multiple(divisor, bound):
    result = divisor
    while True:
        if result > bound:
            return result - divisor
        result += divisor
    
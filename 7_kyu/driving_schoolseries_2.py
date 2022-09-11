from math import floor

def cost(mins):
    rem = 0 if mins % 30 <= 5 else 1
    total = floor(mins/30) + rem
    return max(30,30 +(total -2) *10)

#BEST PRACTICE
#import math

# def cost(mins):
#     return 30 + 10 * math.ceil(max(0, mins - 60 - 5) / 30)

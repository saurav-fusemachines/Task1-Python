from unittest import result


def rental_car_cost(d):
    result = d * 40
    if d >= 7:
        result -= 50
    elif d >= 3:
        result -= 20
    return result  

print(rental_car_cost(7))
print(rental_car_cost(4))

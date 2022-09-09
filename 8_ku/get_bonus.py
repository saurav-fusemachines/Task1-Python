def bonus_time(salary, bonus):
    if bonus:
        return "${}".format(salary * 10)
    else:
        return "${}".format(salary)
        
print(bonus_time(30000,True))
print(bonus_time(26000,False))
        
#If we donot know how many arguments that will be passed into a function,
#we can add * before the parameter name in the function.
#This way the function will receive a tuple of arguments, and can access the items accordingly:


def func_arbitary(*param):
    print("The arguments are: "+param[1])

func_arbitary("Saurav","Roshan","Ale")
name = input("Please Enter your name: ")
age = int(input(f"Enter your age {name}: "))
print(age)

print()

if age>=18 and age<=99:           #In python there is no need of paranthesis for condition statement
    print("{0}, you are eligible to vote.".format(name))

elif age>=100:
    print("I think yout time has come.") 

else:
    print(f"You are under age. So, {name} you are not eligibele to vote.")

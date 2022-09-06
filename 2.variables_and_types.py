print("Today is a good day to learn Python")

inputname = input("Please enter your name:") #string from user input
greeting = "Namastey"
print(greeting + ' ' + inputname)
age =22
print(greeting,inputname,"Your age is:",age)
height = "5.5"
print(type(greeting)) #In O/P python reports that 'greeeting' is an object of type string,str.
print(type(age))   #In O/P python reports that 'age' is an object of type integer,int.
print("Your height is:",height)
print(type(height)) #yo pani string nai huncha

#Type Casting
var1 = "24"
var2 = "27"

print(var1 + var2," This is concatination")
print(int(var1)+int(var2)," This is typecasting and returs sum") 
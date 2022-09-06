from turtle import clear


number = "9,223;372:036 054,775;807"
seprators = ""
for a in number:
    if not a.isnumeric():
        seprators = seprators + a

print("The character in given numbers are: {}".format(seprators))
print()
print("*"*50)
print()

quote="Alright, but apart from the Sanitation, the Medicine, Education, Wine, Public Order, Irrigation, Roads,\
 the Fresh-Water System,and Public Health, what have the Romans ever done for us?"
for char in quote:
    if char.isupper():
        print(char)

print()
for i in range(0,10):
    print(i)            #prints the every value in new line starting from 0 to 9

clear
# for i in range(10,2):
   # print(i)            #DOESN'T PRINT ANY THING BECAUSE i CAN'T BE INDEXED FROM 10 TO 2.
print()

for i in range(0,10,2):
    print(i)          #prints every number with gap 2 betweem 0 to 10. i.e 0,2,4,6,8
print()

for i in range(10,0,-2):
    print(i)            
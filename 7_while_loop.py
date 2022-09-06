'''
One of the important features of while loops is that they can be used when you can't 
determine, in advance , how many times you will need to loop.

A 'for' loop will  repeat each time  in a predetrmined sequence, whereas with a while loop 
you dont need to know  how many times  the loop will execute.

Example is given below'''

available_exits = ["east", "west", "north","south"]
chosen_exit=""

while chosen_exit not in available_exits:
    chosen_exit=input("Please choose a direction to exit: ").lower()
    if chosen_exit == "quit":
        print("Game Over")
        break

print("Finally you got out from the exit.")


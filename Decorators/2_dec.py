#Function can return as a value

#Example

def msg_func(msg):
    greeting = "Hello"

    def printer():
        print(greeting,msg)
    return printer

func = msg_func("Python is a awesome programming to lear")
func()
# Assume we have the following file, located in the same folder as Python.

f = open("demoFile.txt","r")   #Also we can ignore "r" mode because it is default in python.
print(f.read())
# print(f.read(10))   #Read first 10 character from file
# print(f.read(10))   #Read 10 character starting from position 11 because 10 character is already read by line 5

#We can return one line by using the readline() method:
print(f.readline())   #By calling readline() two times, we can read the two first line

# By looping through the lines of the file, We can read the whole file, line by line:
# for line in f:
#     print(line)

f.close()              #Closig=ng a file after operation is a good practice.


# If the file is located in a different location, you will have to specify the file path, like this:
# f1 = open("C:\Users\Saurav\Desktop\git cmd.txt", "rb")   #rb files in binary form
# print(f1.read())

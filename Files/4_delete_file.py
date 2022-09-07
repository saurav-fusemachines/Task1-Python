#To delete a file, we must import the OS module, and run its os.remove() function:

#EXAMPLE: DELETE FILE
import os

if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")

else:
    print("The file does not exist.")


#EXAMPLE: DELETE FOLDER
if os.path.exists("Folder A"):
    os.rmdir("Folder A")

else:
    print("The Folder/Directory does not exist.")
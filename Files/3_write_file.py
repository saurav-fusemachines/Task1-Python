'''
Write to an Existing File
To write to an existing file, we must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"x" - Create - will create a file, returns an error if the file exist
'''
#EXAMPLE "append mode": 'a'
f = open("demofile2.txt", "a")  #This "a" mode append the data in file
f.write("Now the file has more content!")  #creates automatically demofile2.txt if not existed
f.close()

#open and read the file after the appending:
f = open("demofile2.txt", "r")
print(f.read())

# ****************************************************************************************************
# EXAMPLE: "overwrite mode": 'w'

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())

# *******************************************************************************************************
#EXAMPLE: "creating new file": 'x'

f = open("myfile.txt","x")

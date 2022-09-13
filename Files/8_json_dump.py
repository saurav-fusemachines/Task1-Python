'''
Another way of writing JSON to a file is by using json.dump() method The JSON package has the “dump” function which directly writes the 
dictionary to a file in the form of JSON, without needing to convert it into an actual JSON object. It takes 2 parameters:
dictionary - the name of a dictionary which should be converted to a JSON object.
file pointer - pointer of the file opened in write or append mode.
'''

# Python program to write JSON
# to a file


import json

# Data to be written
dictionary = {
 "name": "sathiyajith",
 "rollno": 56,
 "cgpa": 8.6,
 "phonenumber": "9976770500"
}

with open("sample_dump.json", "w") as outfile:
 json.dump(dictionary, outfile)

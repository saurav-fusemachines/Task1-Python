# Python program to read
# json file   
import json
  
# Opening JSON file
f = open("d:\Fusemachines\Python\Files\data.json")
x = '{"name": "Bob", "languages": "English"}'
# returns JSON object as 
# a dictionary
using_loads =   json.loads(x)   #here x has string like dict so json.loads convert string into python dict.
print(using_loads)

data = json.loads(f.read())  
# Iterating through the json
# list
print("\nPlayer Details:")
for i in data['player_details']:
    print(i)

print("\nMatch Schedule:")
for i in data['match_schedule']:
   print(i)
# Closing file
f.close()
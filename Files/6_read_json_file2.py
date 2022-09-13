
# Python program to read
# json file
  
  
import json
  
# Opening JSON file
f = open("d:\Fusemachines\Python\Files\data.json")
  
# returns JSON object as 
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
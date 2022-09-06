# In python,Dictionary is just like key value pair. Key and value in dictionary are case sensitive.

CL = {"Benzema":"Striker","Vini Jr.":"Left Wing","Rodrigo":"Right Winger",
       "Camavinga":"Left Mid","Tchoumeni":"CDM","Luka Modric":"Right Mid",
       "Velvedre":{"1":"RW","2":"RM","3":"RB"},
       "Mendy":"Left Back","Alaba":"Center Back","Militao":"Center Back","Carvajal":"Right Back","Courtious":"Goal Keeper"
       }

print(CL)  #O/P: Prints all dict from CL
print(CL["Benzema"])   #O/P: Striker
print(CL["Velvedre"])      #O/P:  {'1': 'RW', '2': 'RM', '3': 'RB'}
print(CL["Velvedre"]["1"])  #O/P:  RW

#Adding values to the dict
CL["Andry Lunin"]="Goal Keeper"
print(CL)

#deleting from dict
#del CL["Andry Lunin"]

# making copy of dict
# CL1 = CL.copy()

#print(CL.keys())  #returns all keys
#print(CL.items())  #returns all items
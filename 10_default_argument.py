# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:

def house_targeryan(name = "Rhenrya"):
  print("Name: " + name)

house_targeryan("Viserys")
house_targeryan("Viserion")
house_targeryan()   #while this function is invoked parametr will automatically be Rhenrya
house_targeryan("Agon")
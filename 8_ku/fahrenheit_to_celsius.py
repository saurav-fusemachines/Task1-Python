def weather_info (temp):
    c = convert_to_celsius(temp)
    if (c > 0):
        return (c , " is freezing temperature")
    else:
        return (c , " is above freezing temperature")
    
def convert_to_celsius(temperature):
     celsius = (temperature) - 32.0 + (5.0/9.0)
     return celsius
 
print(weather_info(50))


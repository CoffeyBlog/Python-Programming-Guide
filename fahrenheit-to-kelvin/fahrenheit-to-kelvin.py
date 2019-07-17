# converts fahrenheit to kelvin
def fahrenheit2kelvin(fahrenheit):
    celsius = fahrenheit2celsius(fahrenheit)
    kelvin = celsius + 273.15
    return kelvin

# test!!!
k1 = fahrenheit2kelvin(32)
k2 = fahrenheit2kelvin(212)
print(k1, k2)
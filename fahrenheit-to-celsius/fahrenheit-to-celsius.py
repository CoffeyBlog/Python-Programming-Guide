# converts fahrenheit to celsius
def fahrenheit2celsius(fahrenheit):
    celsius = (5.0 / 9) * (fahrenheit - 32)
    return celsius

# test!!!
c1 = fahrenheit2celsius(32)
c2 = fahrenheit2celsius(212)
print(c1, c2)



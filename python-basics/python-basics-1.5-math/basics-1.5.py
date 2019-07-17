# Math & Expressions continued

# The most important thing that you need to know when working w/ expressions in programming is operator precedence -- or

# P - parentheses
# E - exponent
# M - multiplication
# D - division
# A - addition
# S - subtraction


a = 21
b = 7
print(a + b / 3 -10 * 4)      # 16.66666666

# And this can get confusing -- the best thing to do is use parentheses to add what you'd like to add first

print( (((a + b) / 3) -10) * 4) #-2.66666666

# Sometimes, when dealing with very large math problems it is easier to break the problem down using variables - for example:

x = a + b
y = x / 3
z = y - 10
print(z * 4)  #-2.66666666





# Type conversion:

# Sometimes you may have numbers in the form of a string (especially when you are webscraping)
# In order to create a mathematical expresion w/ this you must type cast it to an int --- other wise it will just concatenate 2 strings

a = "2"
b = "3"
print(a + b)  #23


# So let me show you how to convert -- or -- type cast this ...

print(int(a) + int(b)) #5
# Naming variables


# When naming variables follow PEP 8 --- simple is better than complex.


# lowercase is always clean and welcome
greeting = "Hello Pythonistas"


# lowercase + underscores is also clean and acceptable
login_greeting = "Hello Pythonistas"


#You can also use an underscore at the beginning of a variable declaration -- but is that really simpler? And Cleaner?
_greeting = "Hello Pythonistas"


# You can also put numbers in your variables (just not at the beginning) -- this is not the cleanest look but can be handy when you need to number objects - particularlly short term objects
# -- And I ussually separate the name & number w/ an underscore for cleanliness.
Tim_Smith_1  = 2.99
Tim_Smith_2  = 18.99
Trey_Smith_3 = 9.99


# You can't put percentage signs -- but you should not want to because the goal is to write clean & simple code.
# Everyone knows this mean 25%
Fuel_at_25 = 25


# One slightly tricky thing if you are new to programming -- variables are case sensitive, meaning:
# This means one thing
Animal = "Dog"

# And this means another
animal = "cat"


# Python can add numbers
print(Tim_Smith_1 + Tim_Smith_2)


# And Python can add strings (or concatenate them)#
print(Animal + animal)


# However, Python cannot add a string and a number ... (should get a Typeerror on line 48 ... about str concatenation)
#      print(animal + Fuel_at_25)

# Don't be scared of error messages - they are your friends who offer clues on how to correct problems in your code.


greeting = "Welcome " #notice the small space at the end of the welcome ...
user_input = "user_name"
print(greeting + user_input)

# or you can:


greeting = "Welcome"
print(greeting + " " + user_input)  # To You - this maybe cleaner and less complex - that is the unfortunat thing about code, is on many occasions peoples oppinions differ.
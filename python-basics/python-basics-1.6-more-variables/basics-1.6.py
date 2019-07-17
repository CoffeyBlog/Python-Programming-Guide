# When you create a variable - the computer takes that value and stores it in RAM

# The computer also stores the instructions - but it stores these in another part of memory

# imagine you are moving and you grab a -- box -- and name it "toys" <---- the box is your variable

# then you can put -- or list -- items (or toys) inside this box

box = ["doll", "truck", "blocks", "teddy_bear"]

# The above list that looks like an array in Java is called a list in Python.


state = "Kentucky"
print(state)            #Kentucky
print(state[7])         #y

# Always remember -- that almost all programming languages start counting at 0 rather than at 1

# You can only print letters that are "in range"
#     print(state[8])
#  That will give you an error message "index out of range"


# You can also coun't the string backwards.
print(state[-8])        #K - counted backwards from y


# You can slice the string
print(state[3:7])       # tuck - sliced out the tuck
print(state[:3])        # Ken - Is the same as slicing it [0:3]
print(state[3:])        # tucky - will slice off the first three letters
print(state[-3:1])      # Will print nothing ... because you can't go backwards from the start of a string


# You can also remove spaces ...
numbers = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(numbers[0::3])


# String concatenations
string1 = "she's"
string2 = "happy"
print(string1 + string2)    # she's happy


# String literal
print("she's " "happy")     # you get the same result as above -- however this is weird and complex and thus you probably don't want to do it.


# String Multiplication
print("Dog " * 5)            # Dog Dog Dog Dog Dog


# Searching for substrings w/in text
print("roof" in "The roof is on fire")      # true
print("dog" in "cat")                       # false










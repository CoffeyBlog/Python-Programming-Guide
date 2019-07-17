

students = 15
print("There are " + str(students) + " in the class")       # You have to type cast the int students to a string in order to get it to display.
# This is automatically done for you in Java


# An easier way is by using replacement feilds

print("There are {0} in the class".format(students))

# so now ... students is a parameter that is put inside the parentheses


# Another more appropriate example:
print("The {0} dogs like to eat {1}, {2}, {3}, {4} and {5} ".format(2, "chicken", "fish", "steak", "pork", "sushi"))

# in that example 0 represents the amount of dogs
# in that example 1-5 represent the types of foods the dogs like to eat


#in some cases -- when you have a long list -- it's even cleaner to write it like this

print("""The three cats like to eat 
    cat_one: {0} 
    cat_two: {1} 
    c  at_three: {2}  
    """. format("bread", "potatoes", "eggs"))




for i in range (1,12):
    print("No. {0:2} squared is squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# the 0 / 1 / 2 in {0:2} are parameters where data should be input
# the 2 / 4 / 4 / in {_:4} is used to create space and nicely format the text making the code easier to read.
# When we use the operator (i ** 2) &  (i ** 3) we are raising "i" to the power of 2 & 3


print("Pi is approximately {0:12.50}".format(22/7))

print("Pi is approximately {0:12.7}".format(22/7))
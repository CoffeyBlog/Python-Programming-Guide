
# Input

name = input("Please enter your name: ")


# You can do age like this:
age = input("Please enter your age ")                       # No int

# Or even better ... you can do age like this

age = int(input("How old are you, {0} ".format(name)))      # type cask to int


if age >= 18:
    print("You are old enough to vote")
else:
    print("Please come back in {0} years".format(18 - age))

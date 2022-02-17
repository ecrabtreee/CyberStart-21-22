# Briefing L01 C03
# Converting for Fun
# I hope you've been making notes agent as with this challenge you'll need to take what you've just learnt about variables and try converting the types of data they contain.

# Oh, handy tip, if you make a bit of a mess with your code editor you can always click the reset button on the bottom right. It'll refresh the editor and put back the original text so you can start again.

#------------------------------------------------------------------

# Now that you know the different data types, let's look at how to
# convert between them.

# To convert an integer to a string:
anInt = 4
aString = str(anInt)

# To convert a string to an integer:
aString = "20"
anInt = int(aString)

# To convert a string to a float:
aString = "3.333"
aFloat = float(aString)

# Here's an example...
carInfo = "Number of Doors: "
carDoors = "4"

# Now we can print the number of car doors with:

print(carInfo + carDoors)

# You can see that this prints out:
# Number of Doors: 4

# This works because both carInfo and carDoors are strings.
# Notice the quotation marks.

carDoors = 4

# Now carDoors is not a string anymore, it's an integer. (No quotation
# marks)
# If you tried to do:
# print(carInfo + carDoors)
# Then you would see an error:
# TypeError: cannot concatenate 'str' and 'int' objects.
# Try it for yourself.

carDoors = 2

# CHALLENGE 1: Convert carDoors to a string using type conversion.
# Save it in a new variable: carDoorsString

# CHALLENGE 2: Print out the number of doors in the car
# using print(carInfo + carDoorsString)

#--------------------------------------------------------------

# SOLUTION
carInfo = "Number of Doors: "
carDoors = 2

# CHALLENGE 1: Convert carDoors to a string using type conversion.
# Save it in a new variable: carDoorsString
carDoorsString = str(carDoors)

# CHALLENGE 2: Print out the number of doors in the car
# using print(carInfo + carDoorsString)
print(carInfo + carDoorsString)

# Flag = BTAcahNLr9lkUd0mqCky

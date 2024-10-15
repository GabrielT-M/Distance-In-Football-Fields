# Distance In Football Fields
# Made By Gabriel Tachie Menson
# Made In Visual Studio Code
# Started: 2024 - October - 14
# Finished: 2024 - October - 15


# The distance of a football field in the most popular units
# A football field in imperial measurements.
inches= 4320
feet = 360
yards = 120
miles = 0.0681818

# A football feild in metric measurements.
centimeters = 10972.8
meters = 109.728
kilometers = 0.109728


# This shows the user which standard measurements they can convert from.
print("The currently supported measurements are inches, feet, yards, miles, centimeters, meters, and, kilometers. Press enter to continue.")
print(" ")

# The user needs to choose one of the compatible measurements they are converting from.
measurement = str(input("Enter your sstandard measurement. Press enter to continue: "))
print(" ")

# The user also needs to enter the amount of there standard measurement.
amount = int(input("Enter your amount of standard measurement. Press enter to continue: "))
print(" ")


#The section below take the users input of wich measurement they are converting from and changes it to how many are in a football field.

# Imperial conversion to varible values.
if measurement == "inches":
    convert = inches

if measurement == "feet":
    convert = feet

if measurement == "yards":
    convert = yards

if measurement == "miles":
    convert = miles

# Metric conversion to varible values.
if measurement == "centimeters":
    convert = centimeters

if measurement == "meters":
    convert = meters

if measurement == "kilometers":
    convert = kilometers

# This makes the final calcualtiont that divdes the amount of your standard measurement by the the amount of that measurement are in a football field.
converted_1 = str(amount/convert)


# The final result.
print("Your distance in football fields is " + converted_1 + ".")
# Distance In Football Fields
# Made By Gabriel Tachie Menson
# Started: 2024 - October - 14
# Finished: Year - Month - Day

#The distance of a football field in the most popular units=
#Imperial 
inches= 4320
feet = 360
yards = 120
miles = 0.0681818

#Metric
centimeters = 10972.8
meters = 109.728
kilometers = 0.109728

print("The currently supported measurements are inches, feet, yards, miles, centimeters, meters, and, kilometers. Press enter to continue.")
measurment = str(input("Enter your standerd measurment. Press enter to continue: "))

amount = int(input("Enter your amount of standerd measurment. Press enter to continue: "))



#Imperial
if measurment == "inches":
    convert = inches

if measurment == "feet":
    convert = feet

if measurment == "yards":
    convert = yards

if measurment == "miles":
    convert = miles


#Metric
if measurment == "centimeters":
    convert = centimeters

if measurment == "meters":
    convert = meters

if measurment == "kilometers":
    convert = kilometers

converted_1 = str(amount/convert)

print("Your distance in football fields is " + converted_1 + ".")
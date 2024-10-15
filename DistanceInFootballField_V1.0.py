# Distance In Football Fields
# Made By Gabriel Tachie Menson
# Started: 2024 - October - 14
# Finished: Year - Month - Day


inches= 4320
feet = 360
yards = 120
miles = 0.0681818

centimeters = 10972.8
meters = 109.728
kilometers = 0.109728


print("The currently supported measurements are inches, feet, yards, miles, centimeters, meters, and, kilometers.")
measurment = input("Enter your standerd measurment: ")
amount = input("Enter your amount of standerd measurment: ")

converted_1 = measurment*amount
converted_2 = converted_1/measurment

print("Your distance in football fields is " + converted_2 + " .")

from random import randint

number_of_gallons=randint(10,25)
miles_for_full_tank=randint(200,400)
miles_per_gallon=miles_for_full_tank//number_of_gallons
print("Car's fuel tank can hold " + str(number_of_gallons) + " Gallons of GAS")
print("Car can travel " + str(miles_for_full_tank) + " miles with full tank of GAS")
print("Car can travel " + str(miles_per_gallon ) + " miles with a gallon of GAS")
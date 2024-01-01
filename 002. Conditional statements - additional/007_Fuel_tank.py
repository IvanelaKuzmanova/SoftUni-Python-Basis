fuel_type = input()
liters_in_tank = float(input())

if liters_in_tank >= 25 and (fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type =="Gas"):
    print(f"You have enough {fuel_type.lower()}.")
elif liters_in_tank < 25 and (fuel_type == "Diesel" or fuel_type == "Gasoline" or fuel_type == "Gas"):
    print(f"Fill your tank with {fuel_type.lower()}!")
else:
    print(f"Invalid fuel!")

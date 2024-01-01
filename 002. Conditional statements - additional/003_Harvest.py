import math

area = int(input())
grape_per_m = float(input())
wine_liters_needed = int(input())
workers_number = int(input())

total_grape_quantity = area * grape_per_m
grape_for_wine = 0.4 * total_grape_quantity

liters_of_wine = grape_for_wine / 2.5

wine_difference = abs(wine_liters_needed - liters_of_wine)
wine_per_worker = wine_difference / workers_number

if liters_of_wine < wine_liters_needed:
    print(f"It will be a tough winter! More {math.floor(wine_difference)} liters wine needed.")

elif liters_of_wine >= wine_liters_needed:
    print(f"Good harvest this year! Total wine: {math.floor(liters_of_wine)} liters.")
    print(f"{math.ceil(wine_difference)} liters left -> {math.ceil(wine_per_worker)} liters per person.")

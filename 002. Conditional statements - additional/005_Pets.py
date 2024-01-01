import math

days_number = int(input())
food_quantity = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

total_food_needed = days_number * dog_food_per_day + \
                    days_number * cat_food_per_day + \
                    days_number * turtle_food_per_day * 0.001

difference = abs(food_quantity - total_food_needed)

if total_food_needed <= food_quantity:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
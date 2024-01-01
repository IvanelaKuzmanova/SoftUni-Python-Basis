import math

absent_days = int(input())
food_amount = int(input())
deer_one_food = float(input())
deer_two_food = float(input())
deer_three_food = float(input())

total_food_needed = (deer_one_food + deer_two_food + deer_three_food) * absent_days

difference = abs(food_amount - total_food_needed)

if food_amount >= total_food_needed:
    print(f"{math.floor(difference)} kilos of food left.")
else:
    print(f"{math.ceil(difference)} more kilos of food are needed.")
flowers_type = input()
flowers_number = int(input())
budget = int(input())

price = 0

if flowers_type == "Roses":
    price = 5.00
    if flowers_number > 80:
        price *= (1 - 0.10)

if flowers_type == "Dahlias":
    price = 3.80
    if flowers_number > 90:
        price *= (1 - 0.15)

if flowers_type == "Tulips":
    price = 2.80
    if flowers_number > 80:
        price *= (1 - 0.15)

if flowers_type == "Narcissus":
    price = 3.00
    if flowers_number < 120:
        price *= (1 + 0.15)

if flowers_type == "Gladiolus":
    price = 2.50
    if flowers_number < 80:
        price *= (1 + 0.20)

total_price = price * flowers_number
money_difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {flowers_number} {flowers_type} and {money_difference :.2f} leva left.")
else:
    print(f"Not enough money, you need {money_difference :.2f} leva more.")
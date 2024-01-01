# Ред 1.	Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2.	Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3.	Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]

budget = float(input())
statists_number = int(input())
person_clothes_price = float(input())

# •	Декорът за филма е на стойност 10% от бюджета.
# •	При повече от 150 статиста,  има отстъпка за облеклото на стойност 10%.

decor_price = budget * 0.10 # beware if the price is 10% of something or is discounted with 10%!

if statists_number > 150:
    person_clothes_price *= 1 - 0.10 #discount could be defined to be clearer

total_expences = statists_number * person_clothes_price + decor_price

if total_expences > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {total_expences - budget :.2f} leva more.") #better to define money_needed than to calculate in printing)

else:
    print(f"Action!")
    print(f"Wingard starts filming with {budget - total_expences :.2f} leva left.") # same as row 21

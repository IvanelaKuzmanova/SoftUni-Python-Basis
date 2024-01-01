budget = int(input())
season = input()
people_number = int(input())

price = 0

if season == "Spring":
    price = 3000
elif season == "Summer" or season == "Autumn":
    price = 4200
elif season == "Winter":
    price = 2600

if people_number <= 6:
    price *= (1 - 0.10)
elif 7 <= people_number <= 11:
    price *= (1 - 0.15)
elif people_number >= 12:
    price *= (1 - 0.25)

if people_number % 2 == 0 and not season == "Autumn":
    price *= (1 - 0.05)

difference = abs(budget - price)

if budget >= price:
    print(f"Yes! You have {difference :.2f} leva left.")
else:
    print(f"Not enough money! You need {difference :.2f} leva.")
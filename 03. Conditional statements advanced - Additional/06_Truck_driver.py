season = input()
kilometers_per_month = float(input())

price = 0

if kilometers_per_month <= 5000:
    if season == "Spring" or season == "Autumn":
        price = 0.75
    elif season == "Summer":
        price = 0.90
    elif season == "Winter":
        price = 1.05

elif 5000 < kilometers_per_month <= 10000:
    if season == "Spring" or season == "Autumn":
        price = 0.95
    elif season == "Summer":
        price = 1.10
    elif season == "Winter":
        price = 1.25

elif 10000 < kilometers_per_month <= 20000:
    price = 1.45

total_price = (kilometers_per_month * price) * 4 #each season has 4 months
total_price *= (1 - 0.10)

print(f"{total_price :.2f}")

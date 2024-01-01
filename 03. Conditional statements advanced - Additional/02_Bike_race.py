juniors = int(input())
seniors = int(input())
race_type = input()

price_juniors = 0
price_seniors = 0
total_price = 0

if race_type == "trail":
    price_seniors = 7
    price_juniors = 5.50
    tax = juniors * price_juniors + seniors * price_seniors

elif race_type == "cross-country":
    price_seniors = 9.50
    price_juniors = 8
    tax = juniors * price_juniors + seniors * price_seniors

    if (juniors + seniors) >= 50:
        tax *= (1 - 0.25)

elif race_type == "downhill":
    price_seniors = 13.75
    price_juniors = 12.25
    tax = juniors * price_juniors + seniors * price_seniors

elif race_type == "road":
    price_seniors = 21.50
    price_juniors = 20
    tax = juniors * price_juniors + seniors * price_seniors

donation = tax - 0.05 * tax

print(f"{donation :.2f}")

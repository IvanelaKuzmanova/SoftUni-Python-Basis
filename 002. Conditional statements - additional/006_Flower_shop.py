import math

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.50
cactuses_prices = 8

magnolias_number = int(input())
hyacinths_number = int(input())
roses_number = int(input())
cactuses_number = int(input())
gift_price = float(input())

total_price = magnolias_price * magnolias_number + \
              hyacinths_price * hyacinths_number + \
              roses_price * roses_number + \
              cactuses_prices * cactuses_number

total_price *= (1 - 0.05)
# taxes = 5% of the total price

difference = abs(total_price - gift_price)

if gift_price <= total_price:
    print(f"She is left with {math.floor(difference)} leva.")

else:
    print(f"She will have to borrow {math.ceil(difference)} leva.")


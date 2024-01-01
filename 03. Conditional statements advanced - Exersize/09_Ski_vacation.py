# single_room_price = 18.00
# apartment_price = 25.00
# president_apartment_price = 35.00

number_of_days = int(input())
room_type = input()
grade = input()

price_night = 0
bonus = 0
total_price = 0

if room_type == "room for one person":
    price_night = 18.00
    total_price = (number_of_days - 1) * price_night

elif room_type == "apartment":
    price_night = 25.00
    total_price = (number_of_days - 1) * price_night
    if (number_of_days - 1) < 10:
        total_price *= (1 - 0.30)
    elif 10 <= (number_of_days - 1) <= 15:
        total_price *= (1 - 0.35)
    elif (number_of_days - 1) > 15:
        total_price *= (1 - 0.50)

elif room_type == "president apartment":
    price_night = 35.00
    total_price = (number_of_days - 1) * price_night
    if (number_of_days - 1) < 10:
        total_price *= (1 - 0.10)
    elif 10 <= (number_of_days - 1) <= 15:
        total_price *= (1 - 0.15)
    elif (number_of_days - 1) > 15:
        total_price *= (1 - 0.20)

if grade == "positive":
    bonus = 0.25 * total_price
    total_price = total_price + bonus
else:
    bonus = 0.10 * total_price
    total_price = total_price - bonus

print(f"{total_price :.2f}")




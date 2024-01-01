days_staying = int(input())
room_type = input()
grade = input()

room_price = 0
total_price = 0
staying_nights = days_staying - 1

if room_type == "room for one person":
    room_price = 18.00
    total_price = staying_nights * room_price

elif room_type == "apartment":
    room_price = 25.00
    total_price = staying_nights * room_price
    if staying_nights < 10:
        total_price *= (1 - 0.30)
    elif 10 <= staying_nights <= 15:
        total_price *= (1 - 0.35)
    elif staying_nights > 15:
        total_price *= (1 - 0.50)

elif room_type == "president apartment":
    room_price = 35.00
    total_price = staying_nights * room_price
    if staying_nights < 10:
        total_price *= (1 - 0.10)
    elif 10 <= staying_nights <= 15:
        total_price *= (1 - 0.15)
    elif staying_nights > 15:
        total_price *= (1 - 0.20)

if grade == "positive":
    total_price *= (1 + 0.25)
elif grade == "negative":
    total_price *= (1 - 0.10)

print(f"{total_price :.2f}")

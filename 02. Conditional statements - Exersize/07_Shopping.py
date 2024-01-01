budget = float(input())
videocards_number = int(input())
procesors_number = int(input())
ram_number = int(input())

videocard_price = 250
procesors_price = (videocards_number * 250) * 0.35
ram_price = (videocards_number * 250) * 0.10
discount = 0

total_price = videocard_price * videocards_number + \
              procesors_price * procesors_number + \
              ram_price * ram_number

if videocards_number > procesors_number:
    discount = 0.15
    total_price *= 1-discount

money_more = abs(total_price - budget)
money_less = abs(budget - total_price)

if total_price <= budget:
    print(f"You have {money_more :.2f} leva left!")
else:
    print(f"Not enough money! You need {money_less :.2f} leva more!")
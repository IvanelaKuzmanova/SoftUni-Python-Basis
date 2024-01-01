budget = float(input())
category = input()
number_of_people = int(input())

ticket_price = 0
transport_price = 0

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

if 1 <= number_of_people <= 4:
    transport_price = 0.75 * budget
elif 5 <= number_of_people <= 9:
    transport_price = 0.60 * budget
elif 10 <= number_of_people <= 24:
    transport_price = 0.50 * budget
elif 25 <= number_of_people <= 49:
    transport_price = 0.40 * budget
elif number_of_people >= 50:
    transport_price = 0.25 * budget

total_price = number_of_people * ticket_price + transport_price
difference = abs(budget - total_price)

if budget >= total_price:
    print(f"Yes! You have {difference :.2f} leva left.")
else:
    print(f"Not enough money! You need {difference :.2f} leva.")



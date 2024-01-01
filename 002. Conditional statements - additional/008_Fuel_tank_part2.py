fuel_type = input()
fuel_quantity = float(input())
club_card = input()

price = 0

if fuel_type == "Gasoline":
    price = 2.22
elif fuel_type == "Diesel":
    price = 2.33
elif fuel_type == "Gas":
    price = 0.93

if club_card == "Yes":
    if fuel_type == "Gasoline":
        price = price - 0.18
    elif fuel_type == "Diesel":
        price = price - 0.12
    elif fuel_type == "Gas":
        price = price - 0.08

total_price = (fuel_quantity * price)

if 20 <= fuel_quantity <= 25:
    total_price *= (1 - 0.08)

elif fuel_quantity > 25:
    total_price *= (1 - 0.10)

print(f"{total_price :.2f} lv.")

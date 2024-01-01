budget = float(input())
season = input()
car_type = 0
class_type = 0

if budget <= 100 and season == "Summer":
    class_type = "Economy class"
    car_type = "Cabrio"
    price = 0.35 * budget

elif budget <= 100 and season == "Winter":
    class_type = "Economy class"
    car_type = "Jeep"
    price = 0.65 * budget

elif 100 < budget <= 500 and season == "Summer":
    class_type = "Compact class"
    car_type = "Cabrio"
    price = 0.45 * budget

elif 100 < budget <= 500 and season == "Winter":
    class_type = "Compact class"
    car_type = "Jeep"
    price = 0.80 * budget

elif budget > 500:
    class_type = "Luxury class"
    car_type = "Jeep"
    price = 0.90 * budget

print(f"{class_type}\n{car_type} - {price :.2f}")
    
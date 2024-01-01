budget = float(input())
season = input()

place_type = 0
location = 0
price = 0

if budget <= 1000 and season == "Summer":
    place_type = "Camp"
    location = "Alaska"
    price = 0.65 * budget

elif budget <= 1000 and season == "Winter":
    place_type = "Camp"
    location = "Morocco"
    price = 0.45 * budget

elif 1000 < budget <= 3000 and season == "Summer":
    place_type = "Hut"
    location = "Alaska"
    price = 0.80 * budget

elif 1000 < budget <= 3000 and season == "Winter":
    place_type = "Hut"
    location = "Morocco"
    price = 0.60 * budget

elif budget > 3000:
    place_type = "Hotel"
    price = 0.90 * budget
    if season == "Summer":
        location = "Alaska"
    elif season == "Winter":
        location = "Morocco"

print(f"{location} - {place_type} - {price :.2f}")


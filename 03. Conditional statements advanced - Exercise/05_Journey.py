budget = float(input())
season = input()

destination = 0
vacation_type = 0

if season == "summer":
    vacation_type = "Camp"
elif season == "winter":
    vacation_type = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        budget = 0.30 * budget
    elif season == "winter":
        budget = 0.70 * budget

if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        budget = 0.40 * budget
    elif season == "winter":
        budget = 0.80 * budget

if budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    budget = 0.90 * budget


print(f"Somewhere in {destination}\n{vacation_type} - {budget :.2f}")
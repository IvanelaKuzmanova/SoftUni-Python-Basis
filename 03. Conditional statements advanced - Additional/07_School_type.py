season = input()
group_type = input()
number_of_students = int(input())
nights_number = int(input())

price = 0
sport = 0

if season == "Winter" and (group_type == "boys" or group_type == "girls"):
    price = 9.60
    if group_type == "girls":
        sport = "Gymnastics"
    elif group_type == "boys":
        sport = "Judo"

elif season == "Winter" and group_type == "mixed":
    price = 10
    sport = "Ski"

elif season == "Spring" and (group_type == "boys" or group_type == "girls"):
    price = 7.20
    if group_type == "girls":
        sport = "Athletics"
    elif group_type == "boys":
        sport = "Tennis"

elif season == "Spring" and group_type == "mixed":
    price = 9.50
    sport = "Cycling"

elif season == "Summer" and (group_type == "boys" or group_type == "girls"):
    price = 15
    if group_type == "girls":
        sport = "Volleyball"
    elif group_type == "boys":
        sport = "Football"

elif season == "Summer" and group_type == "mixed":
    price = 20
    sport = "Swimming"

total_price = number_of_students * price * nights_number

if number_of_students >= 50:
    total_price *= (1 - 0.50)
elif 20 <= number_of_students < 50:
    total_price *= (1 - 0.15)
elif 10 <= number_of_students < 20:
    total_price *= (1 - 0.05)

print(f"{sport} {total_price :.2f} lv.")
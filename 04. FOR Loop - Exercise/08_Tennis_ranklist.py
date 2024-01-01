import math

number_of_tours = int(input())
starting_points = int(input())

w_points = 0
f_points = 0
sf_points = 0

total_points = 0
average_points_winned = 0

for points in range(number_of_tours):

    current_points = input()

    if current_points == "W":
        w_points += 2000
    elif current_points == "F":
        f_points += 1200
    elif current_points == "SF":
        sf_points += 720

total_points = w_points + f_points + sf_points + starting_points
average_points_winned = (total_points - starting_points) / number_of_tours

tours_winned_number = w_points / 2000
tours_winned_percent = tours_winned_number / number_of_tours

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points_winned)}")
print(f"{tours_winned_percent :.2%}")
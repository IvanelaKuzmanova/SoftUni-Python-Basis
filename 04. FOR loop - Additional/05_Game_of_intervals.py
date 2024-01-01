number_of_moves = int(input())

result = 0
points_0_to_9 = 0
points_10_to_19 = 0
points_20_to_29 = 0
points_30_to_39 = 0
points_40_to_50 = 0
points_invalid = 0


for score in range(number_of_moves):

    current_points = int(input())

    if 0 <= current_points <= 9:
        result += 0.2 * current_points
        points_0_to_9 += 1
    elif 10 <= current_points <= 19:
        result += 0.3 * current_points
        points_10_to_19 += 1
    elif 20 <= current_points <= 29:
        result += 0.4 * current_points
        points_20_to_29 += 1
    elif 30 <= current_points <= 39:
        result += 50
        points_30_to_39 += 1
    elif 40 <= current_points <= 50:
        result += 100
        points_40_to_50 += 1
    elif current_points < 0 or current_points > 50:
        result /= 2
        points_invalid += 1

print(f"{result :.2f}")
print(f"From 0 to 9: {points_0_to_9 / number_of_moves :.2%}")
print(f"From 10 to 19: {points_10_to_19 / number_of_moves :.2%}")
print(f"From 20 to 29: {points_20_to_29 / number_of_moves :.2%}")
print(f"From 30 to 39: {points_30_to_39 / number_of_moves :.2%}")
print(f"From 40 to 50: {points_40_to_50 / number_of_moves :.2%}")
print(f"Invalid numbers: {points_invalid / number_of_moves :.2%}")


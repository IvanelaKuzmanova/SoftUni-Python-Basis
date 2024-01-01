text = input()
sum_points = 0

for character in text:
    if character == "a":
        sum_points += 1
    elif character == "e":
        sum_points += 2
    elif character == "i":
        sum_points += 3
    elif character == "o":
        sum_points += 4
    elif character == "u":
        sum_points += 5

print(sum_points)


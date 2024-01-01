number_of_days = int(input())

total_liters = 0
total_degrees = 0

for day in range(number_of_days):

    current_liters = float(input())
    current_degree = float(input())
    total_liters += current_liters

    total_degrees += current_liters * current_degree

average_degrees = total_degrees / total_liters

print(f"Liter: {total_liters :.2f}")
print(f"Degrees: {average_degrees :.2f}")
if average_degrees < 38:
    print(f"Not good, you should baking!")
elif 38 <= average_degrees <= 42:
    print(f"Super!")
elif average_degrees > 42:
    print(f"Dilution with distilled water!")
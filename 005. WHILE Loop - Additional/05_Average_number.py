number_to_input = int(input())
total_sum = 0

for _ in range(number_to_input):
    current_number = int(input())
    total_sum += current_number

print(f"{total_sum / number_to_input :.2f}")
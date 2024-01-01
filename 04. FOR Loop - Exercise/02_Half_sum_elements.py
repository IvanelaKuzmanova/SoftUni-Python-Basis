import sys

numbers_count = int(input())

total_sum = 0
max_number = -sys.maxsize

for numbers in range(numbers_count):
    current_number = int(input())

    if current_number > max_number:         #in each cycle the loop checks if current number is the largest and defines it as max number
        max_number = current_number

    total_sum += current_number

sum_others = abs(total_sum - max_number)
difference = abs(max_number - sum_others)

if max_number == sum_others:         #checks if the sum of all other numbers equals the max_number
    print("Yes")
    print(f"Sum = {max_number}")            # in this case max_number is equal to the sum of all others
else:
    print("No")
    print(f"Diff = {difference}")
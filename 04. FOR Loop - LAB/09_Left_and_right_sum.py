numbers_count = int(input())

sum_left = 0
sum_right = 0

# for numbers in range(numbers_count):
#     current_number = int(input())
#     sum_left += current_number
#
# for numbers in range(numbers_count):
#     current_number = int(input())
#     sum_right += current_number

for numbers in range(numbers_count * 2):
    current_number = int(input())
    if numbers < numbers_count:
        sum_left += current_number
    else:
        sum_right += current_number

difference_sum = abs(sum_left - sum_right)

if sum_left == sum_right:
    print(f"Yes, sum = {sum_left}")
else:
    print(f"No, diff = {difference_sum}")
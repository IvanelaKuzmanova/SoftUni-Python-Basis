numbers_count = int(input())

sum_even = 0
sum_odd = 0

for numbers in range(numbers_count):  # from 0 to (numbers count - 1)
    current_number = int(input())

    if numbers % 2 == 0:  # starting from 0, so opposite for even and odd
        sum_odd += current_number
    else:
        sum_even += current_number

difference = abs(sum_odd - sum_even)

if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_odd}")
else:
    print(f"No\nDiff = {difference}")

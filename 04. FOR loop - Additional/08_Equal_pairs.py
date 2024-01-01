number_of_pairs = int(input())
first_number_1 = int(input())
first_number_2 = int(input())

first_sum = first_number_1 + first_number_2

difference = 0

for numbers in range(number_of_pairs -1):

    next_number_1 = int(input())
    next_number_2 = int(input())
    next_sum = next_number_1 + next_number_2

    if first_sum - next_sum != 0:
        difference = abs(first_sum - next_sum)

    first_sum = next_sum

if difference == 0:
    print(f"Yes, value={first_sum}")
else:
    print(f"No, maxdiff={difference}")


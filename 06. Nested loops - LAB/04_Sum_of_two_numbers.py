number_start = int(input())
number_end = int(input())
magical_number = int(input())

same = False
combination_count = 0

for number1 in range(number_start, number_end + 1):
    for number2 in range(number_start, number_end + 1):
        combination_count += 1
        if number1 + number2 == magical_number:
            same = True
            break
    if same:
        break

if same:
    print(f"Combination N:{combination_count} ({number1} + {number2} = {magical_number})")
else:
    print(f"{combination_count} combinations - neither equals {magical_number}")
#bottle = 750
#plate = 5
#cup = 15

bottles_soap = int(input())
command = input()

is_over = False

total_soap = bottles_soap * 750
ml_needed = 0
dishes_count = 0
cups_count = 0
number_of_loads = 0

while command != "End":

    number_of_loads += 1

    if number_of_loads % 3 == 0:
        ml_needed += int(command) * 15
        cups_count += int(command)

    else:
        ml_needed += int(command) * 5
        dishes_count += int(command)

    if ml_needed > total_soap:
        is_over = True
        break

    command = input()

if is_over:
    print(f"Not enough detergent, {abs(total_soap - ml_needed)} ml. more necessary!")
else:
    print(f"Detergent was enough!")
    print(f"{dishes_count} dishes and {cups_count} pots were washed.")
    print(f"Leftover detergent {abs(total_soap - ml_needed)} ml.")
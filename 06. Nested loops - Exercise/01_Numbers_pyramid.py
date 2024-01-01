number = int(input())
current_digit = 1
is_larger = False

for row in range(1, number + 1):

    for col in range(1, row + 1):
        if current_digit > number:
            is_larger = True
            break
        print(f"{current_digit}" , end = " ")
        current_digit += 1

    if current_digit > number:
        break
    print()


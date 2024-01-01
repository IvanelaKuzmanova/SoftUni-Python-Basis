cake_width = int(input())
cake_length = int(input())

number_of_pieces = input()
no_more_cake = False

cake_area = cake_length * cake_width
piece_area = 1 * 1

total_pieces = 0

while number_of_pieces != "STOP":

    total_pieces += int(number_of_pieces)
    cake_area -= int(number_of_pieces) * piece_area

    if cake_area <= 0:
        no_more_cake = True
        break

    number_of_pieces = input()

if no_more_cake:
    print(f"No more cake left! You need {abs(cake_area)} pieces more.")
else:
    print(f"{abs(cake_area)} pieces are left.")
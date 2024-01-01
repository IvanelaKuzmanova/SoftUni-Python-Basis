number_of_floors = int(input())
spaces_per_floor = int(input())

for floor in range(number_of_floors, 0, - 1):

    if number_of_floors == 1 or floor == number_of_floors:
        space_type = "L"
    elif floor % 2 == 0:
        space_type = "O"
    else:
        space_type = "A"

    for space in range(spaces_per_floor):

        print(f"{space_type}{floor}{space}", end = " ")             #defining end of print to print them on the same row with space between each one
    print()             #for moving to next row after ending each nested cycle
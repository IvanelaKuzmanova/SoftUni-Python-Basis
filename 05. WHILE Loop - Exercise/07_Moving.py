box_size = 1            #1x1x1 meters

width = int(input())
length = int(input())
height = int(input())

currents_command = input()

free_space = width * length * height
no_space = False

while currents_command != "Done":

    free_space -= int(currents_command)

    if free_space <= 0:
        no_space = True
        break

    currents_command = input()

if no_space:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
else:
    print(f"{abs(free_space)} Cubic meters left.")
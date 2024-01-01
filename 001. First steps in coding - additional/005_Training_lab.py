# w_length = float(input())
# h_width = float(input())
#
# door = 1
# table = 2
#
# desks_w = (w_length - 1) // 1.2
# desks_h = h_width // 0.7
#
# total_desks = (desks_w * desks_h) - door - table
# total_desks = int(total_desks)
#
# print(f"{total_desks:.0f}")

corridor_height = 100
desk_height = 70
desk_width = 120

removed_desks = 3

hall_width = float(input()) * 100
hall_height = float(input()) * 100

useful_height = hall_height - corridor_height

desks_per_height = int(useful_height / desk_height)
desks_per_width = int(hall_width / desk_width)

total_desks = int(desks_per_height * desks_per_width - removed_desks)

print(total_desks)

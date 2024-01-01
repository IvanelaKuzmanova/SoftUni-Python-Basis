# Green paint

GREEN_AREA_LITER = 3.4

wall_side_x = float(input())
wall_side_y = float(input())

door_area = float(1.2*2)
window_area = float(1.5*1.5)

total_area_green = (2*(wall_side_x*wall_side_x) - door_area) + (2*(wall_side_y*wall_side_x) - 2*window_area)

liters_green = total_area_green/GREEN_AREA_LITER

# Red paint

RED_PAINT_LITER = 4.3

roof_height_h = float(input())

total_area_red = 2*(wall_side_x*wall_side_y) \
                 + 2*((wall_side_x*roof_height_h)/2)

liters_red = total_area_red/RED_PAINT_LITER

print(f'{liters_green :.2f}')
print(f'{liters_red :.2f}')


length=int(input())
width=int(input())
height=int(input())
percentage=float(input())

tank_volume=length * width * height
taken_volume=tank_volume*(percentage/100)

liters_water=(tank_volume - taken_volume)/1000

print(liters_water)
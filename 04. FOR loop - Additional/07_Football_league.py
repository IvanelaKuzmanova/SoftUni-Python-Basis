stadium_capacity = int(input())
number_of_fans = int(input())

sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0
total_fans = 0

for numbers in range(number_of_fans):

    sector = input()

    if sector == "A":
        sector_a += 1
        total_fans += 1
    elif sector == "B":
        sector_b += 1
        total_fans += 1
    elif sector == "V":
        sector_v += 1
        total_fans += 1
    elif sector == "G":
        sector_g += 1
        total_fans += 1

print(f"{sector_a / number_of_fans :.2%}")
print(f"{sector_b / number_of_fans :.2%}")
print(f"{sector_v / number_of_fans :.2%}")
print(f"{sector_g / number_of_fans :.2%}")
print(f"{total_fans / stadium_capacity :.2%}")




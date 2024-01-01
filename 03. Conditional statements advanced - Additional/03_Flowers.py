chrysanthemum_number = int(input())
roses_number = int(input())
tulips_number = int(input())
season = input()
holiday = input()

arrangement_tax = 2.00
chrisanthemum_price = 0
roses_price = 0
tulips_price = 0

if (season == "Spring" or season == "Summer") and holiday == "N":
    chrisanthemum_price = 2.00
    roses_price = 4.10
    tulips_price = 2.50

elif (season == "Spring" or season == "Summer") and holiday == "Y":
    chrisanthemum_price = 2.00 + (0.15 * 2.00)
    roses_price = 4.10 + (0.15 * 4.10)
    tulips_price = 2.50 + (0.15 * 2.50)

elif (season == "Autumn" or season == "Winter") and holiday == "N":
    chrisanthemum_price = 3.75
    roses_price = 4.50
    tulips_price = 4.15

elif (season == "Autumn" or season == "Winter") and holiday == "Y":
    chrisanthemum_price = 3.75 + (0.15 * 3.75)
    roses_price = 4.50 + (0.15 * 4.50)
    tulips_price = 4.15 + (0.15 * 4.15)


total_price = chrysanthemum_number * chrisanthemum_price + \
              roses_number * roses_price + \
              tulips_number * tulips_price

if season == "Spring" and tulips_number > 7:
    total_price *= (1 - 0.05)
elif season == "Winter" and roses_number >= 10:
    total_price *= (1 - 0.10)

if (roses_number + tulips_number + chrysanthemum_number) > 20:
    total_price *= (1 - 0.20)

total_price = total_price + 2

print(f"{total_price :.2f}")





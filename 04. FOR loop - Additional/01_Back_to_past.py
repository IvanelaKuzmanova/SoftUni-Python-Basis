inhereted_money = float(input())
year_for_living = int(input())

current_age = 18

total_money_odd = 0
total_money_even = 0

for number in range(1800, year_for_living + 1):

    if number % 2 == 0:
        total_money_even += 12000
        current_age += 1
    else:
        total_money_odd += 12000 + 50 * (current_age)
        current_age += 1

total_money = total_money_even + total_money_odd

difference = abs(inhereted_money - total_money)

if inhereted_money >= total_money:
    print(f"Yes! He will live a carefree life and will have {difference :.2f} dollars left.")
else:
    print(f"He will need {difference :.2f} dollars to survive.")
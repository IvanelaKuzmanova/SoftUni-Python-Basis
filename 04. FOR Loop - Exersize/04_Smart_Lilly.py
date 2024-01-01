lilly_age = int(input())
washing_machine_price = float(input())
toy_single_price = int(input())

total_money = 0
total_toys_number = 0

for age in range(1, lilly_age + 1):

    if age % 2 == 0:
        total_money += (age / 2 * 10) - 1           #10lv - 1lv taken from her brother

    else:
        total_toys_number += 1

money_from_toys = total_toys_number * toy_single_price

total_sum_collected = money_from_toys + total_money

difference = abs(total_sum_collected - washing_machine_price)

if total_sum_collected >= washing_machine_price:
    print(f"Yes! {difference :.2f}")
else:
    print(f"No! {difference :.2f}")
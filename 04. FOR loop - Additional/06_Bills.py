number_of_months = int(input())

electricity = 0
water = 0
internet = 0
others = 0
total_sum = 0

for months in range(number_of_months):

    electricity_bill = float(input())
    electricity += electricity_bill
    water += 20
    internet += 15
    total_sum = electricity + water + internet
    others += 1.2 * (electricity_bill + 20 + 15)
    total_sum += others


print(f"Electricity: {electricity :.2f} lv")
print(f"Water: {water :.2f} lv")
print(f"Internet: {internet :.2f} lv")
print(f"Other: {others :.2f} lv")
print(f"Average: {total_sum / number_of_months :.2f} lv")




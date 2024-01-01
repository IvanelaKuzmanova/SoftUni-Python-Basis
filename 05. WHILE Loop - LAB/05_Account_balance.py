total_sum = 0

current_income = input()

while current_income != "NoMoreMoney":

    if float(current_income) < 0:
        print(f"Invalid operation!")
        break

    total_sum += float(current_income)
    print(f"Increase: {float(current_income) :.2f}")
    current_income = input()

print(f"Total: {total_sum :.2f}")

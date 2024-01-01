payments_attempts = 0
card_count = 0
cash_count = 0
card_payments = 0
cash_payments = 0
total_money = 0

money_needed = int(input())
current_price = input()

is_collected = False

while current_price != "End":

    payments_attempts += 1

    if payments_attempts % 2 == 0:
        if int(current_price) < 10:
            print(f"Error in transaction!")
            current_price = input()
            continue
        card_payments += int(current_price)
        card_count += 1

    else:
        if int(current_price) > 100:
            print(f"Error in transaction!")
            current_price = input()
            continue
        cash_payments += int(current_price)
        cash_count += 1

    print(f"Product sold!")

    total_money = cash_payments + card_payments

    if total_money >= money_needed:
        is_collected = True
        break

    current_price = input()

if is_collected:
    print(f"Average CS: {cash_payments / cash_count :.2f}")
    print(f"Average CC: {card_payments / card_count :.2f}")
else:
    print(f"Failed to collect required money for charity.")
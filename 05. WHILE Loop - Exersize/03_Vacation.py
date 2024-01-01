trip_price = float(input())
starting_money = float(input())

money_amount = starting_money

spending_counter = 0
number_of_days = 0
cant_save = False

while True:             #we do not have specific guides for the cycle, so it starts with "while True"
                        # could be "while money_amount < trip_price and spending_counter < 5":

    action_type = input()
    saved_spend_amount = float(input())

    number_of_days += 1             #always adding a day through each cycle (starting from 0)

    if action_type == "spend":
        spending_counter += 1

        if spending_counter >= 5:
            cant_save = True
            break

        money_amount -= saved_spend_amount

        if money_amount <= 0:
            money_amount = 0        #if amount is 0 or less - it should always be considered 0 (as described in task)

    elif action_type == "save":

        spending_counter = 0        #if this check is skipped, it crashes on some of the judge tests!
        money_amount += saved_spend_amount

        if money_amount >= trip_price:
            break

if cant_save:
    print(f"You can't save the money.\n{number_of_days}")
else:
    print(f"You saved the money for {number_of_days} days.")







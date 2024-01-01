puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

trip_price = float(input())
puzzles_number = int(input())
dolls_number = int(input())
bears_number = int(input())
minions_number = int(input())
trucks_number = int(input())

number_of_toys = puzzles_number + dolls_number + \
                 bears_number + minions_number + trucks_number

total_profit = (puzzles_number * puzzle_price +
                dolls_number * doll_price +
                bears_number * bear_price +
                minions_number * minion_price +
                trucks_number * truck_price)

if number_of_toys >= 50:
    discount = 0.25 * total_profit
else:
    discount = 0

final_toys_price = total_profit - discount

rent = 0.1 * final_toys_price

final_profit = total_profit - rent - discount

money_for_trip = abs(final_profit - trip_price)

if money_for_trip >= trip_price:
    print(f'Yes! {money_for_trip :.2f} lv left.')

else:
    print(f'Not enough money! {money_for_trip :.2f} lv needed.')
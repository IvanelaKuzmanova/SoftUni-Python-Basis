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

# discount 25% if number is more than 50

if number_of_toys >= 50:
    total_profit *= 1 - 0.25

# rent 10% of the profit should be payed

total_profit *= 1 - 0.1

if total_profit >= trip_price:
    print(f'Yes! {total_profit - trip_price :.2f} lv left.')

else:
    print(f'Not enough money! {trip_price - total_profit :.2f} lv needed.')

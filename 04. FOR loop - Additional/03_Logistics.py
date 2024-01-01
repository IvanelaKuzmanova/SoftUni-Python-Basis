stocks_number = int(input())

stock_weight = 0

microbus_stocks = 0
truck_stocks = 0
train_stocks = 0

for stocks in range(stocks_number):

    stock_weight = int(input())

    if stock_weight <= 3:
        # price_per_tone = 200
        microbus_stocks += stock_weight
    elif 4 <= stock_weight <= 11:
        # price_per_tone = 175
        truck_stocks += stock_weight
    elif stock_weight >= 12:
        # price_per_tone = 120
        train_stocks += stock_weight

total_weight = microbus_stocks + truck_stocks + train_stocks
total_price = microbus_stocks * 200 + truck_stocks * 175 + train_stocks * 120

print(f"{total_price / total_weight :.2f}")
print(f"{microbus_stocks / total_weight :.2%}")
print(f"{truck_stocks / total_weight :.2%}")
print(f"{train_stocks / total_weight :.2%}")

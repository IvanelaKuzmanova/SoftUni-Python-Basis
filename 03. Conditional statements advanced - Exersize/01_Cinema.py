movie_type = input()
rows_number = int(input())
columns_number = int(input())

price = 0
seats = rows_number * columns_number

if movie_type == "Premiere":
    price = 12.00
elif movie_type == "Normal":
    price = 7.50
elif movie_type == "Discount":
    price = 5.00

total_profit = seats * price

print(f"{total_profit :.2f}")
kilometers = int(input())
daytime = input()

taxi_day_price = 0.70 + (kilometers * 0.79)
taxi_night_price = 0.70 + (kilometers * 0.90)

bus_price = 0.09 * kilometers # distances more than 20 km

train_price = 0.06 * kilometers # distances more than 100 km

if kilometers < 20 and daytime == "day":
    print(f"{taxi_day_price :.2f}")

elif kilometers < 20 and daytime == "night":
    print(f"{taxi_night_price :.2f}")

elif kilometers >= 20 and kilometers < 100:
    print(f"{bus_price :.2f}")

else:
    print(f"{train_price :.2f}")
EUR_TO_BGN=1.94

vegetables_price=float(input())
fruits_price=float(input())
vegetables_kg=float(input())
fruits_kg=float(input())

total_vegetables=(vegetables_kg*vegetables_price)/EUR_TO_BGN
total_fruits=(fruits_kg*fruits_price)/EUR_TO_BGN

total_price=total_fruits+total_vegetables

print(f"{total_price :.2f}")



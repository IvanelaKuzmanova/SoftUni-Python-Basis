pen_price=5.80
markers_price=7.20
cleaning_price=1.20

pen_number=int(input())
markers_number=int(input())
cleaning_liters=int(input())
discount=int(input())/100

price=float((pen_number*pen_price) + (markers_price*markers_number) + (cleaning_price*cleaning_liters))

final_price=price-(price*discount)

print(final_price)

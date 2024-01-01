price_per_square_meter=float(7.61)
yard_area=float(input())
full_price=price_per_square_meter*yard_area
discount=float(full_price*0.18)
total_price=full_price-discount

print(f'The final price is: {total_price} lv.')
print(f'The discount is: {discount} lv.')

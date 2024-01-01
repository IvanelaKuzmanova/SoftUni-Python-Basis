yearly_fee=int(input())

shoes_price=yearly_fee - (0.40*yearly_fee)
clothes_price=shoes_price - (0.20*shoes_price)
ball_price=0.25*clothes_price
accessories_price=0.20*ball_price

total_price=yearly_fee + shoes_price + clothes_price + ball_price + accessories_price

print(total_price)
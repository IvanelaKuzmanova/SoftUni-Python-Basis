paper_price = 5.80
fabric = 7.20
glue = 1.20

paper_rolls = int(input())
fabric_rolls = int(input())
liters_glue = float(input())
discount_percent = int(input())

total_price = paper_price * paper_rolls \
              + fabric * fabric_rolls + \
              glue * liters_glue

total_price *= (1 - (discount_percent / 100))

print(f"{total_price :.3f}")

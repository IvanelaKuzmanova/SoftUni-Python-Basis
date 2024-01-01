cover_price=1.50
paint_price=14.50
paint_liquid_price=5.00
additional_cover=2
bags=0.40

cover_amount=int(input())
paint_amount=int(input())
paint_liquid_amount=int(input())
hours=int(input())

additional_paint=0.10*paint_amount

materials_price=((cover_amount+additional_cover)*cover_price) + ((paint_amount+additional_paint)*paint_price) + (paint_liquid_amount*paint_liquid_price) + bags

hourly_rate=0.30*materials_price

total_price=(hourly_rate*8) + materials_price

print(f'{total_price}')



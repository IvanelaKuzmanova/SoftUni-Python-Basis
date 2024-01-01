chicken_menu=10.35
fish_menu=12.40
veggie_menu=8.15
delivery=2.50

chicken_number=int(input())
fish_number=int(input())
veggie_number=int(input())

menu_price=chicken_number*chicken_menu + fish_number*fish_menu + veggie_number*veggie_menu

desserts_price=0.20*menu_price

total_price=menu_price + desserts_price + delivery

print(f'{total_price}')
mackerel_price = float(input())
sprinkle_price = float(input())

bonito_price = mackerel_price + 0.60 * mackerel_price
safrid_price = sprinkle_price + 0.8 * sprinkle_price
SHELL_PRICE = 7.50

bonito_kg = float(input())
safrid_kg = float(input())
shell_kg = int(input())

total_price = bonito_price*bonito_kg \
              + safrid_price*safrid_kg \
              + SHELL_PRICE*shell_kg

print(f'{total_price :.2f}')

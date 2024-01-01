money = float(input())
money_coins = int(money * 100)          # it's important to have int for the coins to avoid bugs

number_of_coins = 0

# coins 1, 2, 5, 10, 20, 50, 1.00, 2.00
while money_coins > 0:
    number_of_coins += 1            # връща се една монета и долу се вижда с каква стойност

    if money_coins >= 200:
        money_coins -= 200

    elif money_coins >= 100:
        money_coins -= 100

    elif money_coins >= 50:
        money_coins -= 50

    elif money_coins >= 20:
        money_coins -= 20

    elif money_coins >= 10:
        money_coins -= 10

    elif money_coins >= 5:
        money_coins -= 5

    elif money_coins >= 2:
        money_coins -= 2

    elif money_coins >= 1:
        money_coins -= 1

print(number_of_coins)



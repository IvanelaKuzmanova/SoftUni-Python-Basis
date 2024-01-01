number = int(input())

for num in range(1111, 9999 + 1):               #подава числа от дефиниран рейнгж

    is_special = True

    for _, digit in enumerate(str(num)):         #обхожда всяко подадено число като стринг

        digit_int = int(digit)                  # обръщане на обходените символи в числа

        if digit_int == 0:          # всяко число, което съдържа 0, не може да е специално (по конкретното условие), защото на 0 не се дели
            is_special = False
            break

        if number % digit_int != 0:
            is_special = False
            break

    if is_special:
        print(f"{num}", end = " ")
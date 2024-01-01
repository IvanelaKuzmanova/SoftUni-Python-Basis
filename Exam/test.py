import math

first_number_limit = int(input())
second_number_limit = int(input())
third_number_limit = int(input())

digit_one = 0
digit_two = 0
digit_three = 0
# •	Първата и третата цифра трябва да бъдат четни
# •	Втората цифра трябва да бъде просто число в диапазона [2...7]

for num1 in range(2, first_number_limit + 1, 2):
    digit_one = num1

    for num2 in range(2, second_number_limit + 1):
        digit_two = num2

        for num3 in range(2, third_number_limit + 1, 2):
            digit_three = num3

            if num2 % 2 == 0 and num2 > 2:
                continue

            if num2 % num3 == 0 and num2 != num3:
                continue

            if num2 > 7:
                break

            print(f"{digit_one} {digit_two} {digit_three}")





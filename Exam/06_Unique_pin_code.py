first_number_limit = int(input())
second_number_limit = int(input())
third_number_limit = int(input())

digit_one = 0
digit_two = 0
digit_three = 0
# •	Първата и третата цифра трябва да бъдат четни
# •	Втората цифра трябва да бъде просто число в диапазона [2...7]

for num1 in range(2, first_number_limit + 1):

    if num1 % 2 == 0:
        digit_one = num1

        for num2 in range(2, second_number_limit):
            is_prime = True

            if second_number_limit % num2 != 0:
                is_prime = False
                break

            if num2 == 0:
                is_prime = False
                break

            digit_two = num2

            for num3 in range(2, third_number_limit + 1):
                if num3 % 2 == 0:
                    digit_three = num3

    print(f"{digit_one} {digit_two} {digit_three}")





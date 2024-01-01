first_number = int(input())
second_number = int(input())


for number in range(first_number, second_number + 1):
    number_to_string = str(number)
    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(number_to_string):            #въвеждат се две промениви - за индекса (от 0) и за цифра от обходения стринг
        if index % 2 == 0:
            odd_sum += int(digit)           # добавят се на обратно, тъй като индексите започват от 0, а не от 1
        else:
            even_sum += int(digit)

    if even_sum == odd_sum:
        print(number, end = " ")
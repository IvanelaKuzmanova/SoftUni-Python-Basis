number_1 = int(input())
number_2 = int(input())
math_operator = input()

classification = 0
result = 0

if math_operator == "+":
    result = number_1 + number_2
    if result % 2 == 0:
        classification = "even"
    else:
        classification = "odd"
    print(f"{number_1} {math_operator} {number_2} = {result} - {classification}")

elif math_operator == "-":
    result = number_1 - number_2
    if result % 2 == 0:
        classification = "even"
    else:
        classification = "odd"
    print(f"{number_1} {math_operator} {number_2} = {result} - {classification}")

elif math_operator == "*":
    result = number_1 * number_2
    if result % 2 == 0:
        classification = "even"
    else:
        classification = "odd"
    print(f"{number_1} {math_operator} {number_2} = {result} - {classification}")


elif math_operator == "/":
    if number_2 != 0:
        result = number_1 / number_2
        print(f"{number_1} / {number_2} = {result :.2f}")
    else:
        print(f"Cannot divide {number_1} by zero")

elif math_operator == "%":
    if number_2 != 0:
        result = number_1 % number_2
        print(f"{number_1} % {number_2} = {result}")
    else:
        print(f"Cannot divide {number_1} by zero")


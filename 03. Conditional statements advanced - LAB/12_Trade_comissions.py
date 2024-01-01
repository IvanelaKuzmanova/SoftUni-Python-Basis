city = input()
sales_number = float(input())

comission = 0

if 0 <= sales_number <= 500:

    if city == "Sofia":
        comission = 0.05
    elif city == "Varna":
        comission = 0.045
    elif city == "Plovdiv":
        comission = 0.055

elif 500 < sales_number <= 1000:

    if city == "Sofia":
        comission = 0.07
    elif city == "Varna":
        comission = 0.075
    elif city == "Plovdiv":
        comission = 0.08

elif 1000 < sales_number <= 10000:

    if city == "Sofia":
        comission = 0.08
    elif city == "Varna":
        comission = 0.10
    elif city == "Plovdiv":
        comission = 0.12

elif sales_number > 10000:

    if city == "Sofia":
        comission = 0.12
    elif city == "Varna":
        comission = 0.13
    elif city == "Plovdiv":
        comission = 0.145

comission_amount = comission * sales_number

if comission == 0:
    print("error")
else:
    print(f"{comission_amount :.2f}")
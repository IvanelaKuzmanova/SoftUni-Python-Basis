age = float(input())
gender = input()
#
# if gender == "m" and age >= 16:
#     print("Mr.")
# elif gender == "m" and age < 16:
#     print("Master")
# elif gender == "f" and age >= 16:
#     print("Ms.")
# elif gender == "f" and age < 16:
#     print("Miss")

if gender == "m":
    if age >= 16:
        print("Mr.")
    else:
        print("Master")

if gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")

numbers_count = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for numbers in range(numbers_count):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

# p1 = (p1 / numbers_count) * 100         #percent = target / total * 100
# p2 = (p2 / numbers_count) * 100
# p3 = (p3 / numbers_count) * 100
# p4 = (p4 / numbers_count) * 100
# p5 = (p5 / numbers_count) * 100

p1 = (p1 / numbers_count)                   #percent_base = target / total
p2 = (p2 / numbers_count)
p3 = (p3 / numbers_count)
p4 = (p4 / numbers_count)
p5 = (p5 / numbers_count)

# print(f"{p1 :.2f}")   #:.2f - prints 2 digits after comma
# print(f"{p2 :.2f}")
# print(f"{p3 :.2f}")
# print(f"{p4 :.2f}")
# print(f"{p5 :.2f}")

print(f"{p1 :.2%}")     #:.2% - multiplies by 100 and prints % at the end with 2 digits after comma
print(f"{p2 :.2%}")
print(f"{p3 :.2%}")
print(f"{p4 :.2%}")
print(f"{p5 :.2%}")
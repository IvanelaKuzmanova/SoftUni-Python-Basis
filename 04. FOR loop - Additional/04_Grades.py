number_of_students = int(input())

sum_of_grades = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0
sum_5 = 0

for grades in range(number_of_students):

    current_grade = float(input())

    if 2.00 <= current_grade <= 2.99:
        sum_2 += 1
        sum_of_grades += current_grade

    elif 3.00 <= current_grade <= 3.99:
        sum_3 += 1
        sum_of_grades += current_grade

    elif 4.00 <= current_grade <= 4.99:
        sum_4 += 1
        sum_of_grades += current_grade

    elif current_grade >= 5.00:
        sum_5 += 1
        sum_of_grades += current_grade

print(f"Top students: {sum_5 / number_of_students :.2%}")
print(f"Between 4.00 and 4.99: {sum_4 / number_of_students :.2%}")
print(f"Between 3.00 and 3.99: {sum_3 / number_of_students :.2%}")
print(f"Fail: {sum_2 / number_of_students :.2%}")
print(f"Average: {sum_of_grades / number_of_students :.2f}")
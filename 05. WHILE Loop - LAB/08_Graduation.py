student_name = input()

student_class = 1
sum_grades = 0
counter_fail = 0

while student_class <= 12:

    grade = float(input())

    if grade < 4:
        counter_fail += 1
        if counter_fail > 1:
            print(f"{student_name} has been excluded at {student_class} grade")
            break
        continue        #if grade is below 4.00 but fails are less than 2, cycle continues without passing to another class (adding 1 to clases)

    student_class += 1
    sum_grades += grade

if counter_fail <= 1:
    print(f"{student_name} graduated. Average grade: {sum_grades / 12 :.2f}")



# while grade >= 4.00:
#
#     sum_grades += grade
#
#     if student_class > 12:
#         print(f"{student_name} graduated. Average grade: {sum_grades / student_class}")
#         break
#
#     student_class += 1
#     grade = float(input())


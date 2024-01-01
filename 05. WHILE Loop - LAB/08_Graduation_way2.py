student_name = input()

student_class = 1
sum_grades = 0
counter_fail = 0
excluded = False

while student_class <= 12:

    grade = float(input())

    if grade < 4:
        counter_fail += 1
        if counter_fail > 1:
            excluded = True
            break
        continue        #if grade is below 4.00 but fails are less than 2, cycle continues without passing to another class (adding 1 to clases)

    student_class += 1
    sum_grades += grade

if excluded:
    print(f"{student_name} has been excluded at {student_class} grade")
else:
    print(f"{student_name} graduated. Average grade: {sum_grades / 12 :.2f}")




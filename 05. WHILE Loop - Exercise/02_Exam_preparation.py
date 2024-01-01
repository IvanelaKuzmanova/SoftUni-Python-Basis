bad_grades_threshold = int(input())
command = input()

counter_fails = 0
is_failed = False

sum_of_grades = 0
number_of_tasks = 0
task_name = " "

while command != "Enough":

    task_name = command
    grade = int(input())
    sum_of_grades += grade
    number_of_tasks += 1

    if grade <= 4:
        counter_fails += 1
        if counter_fails >= bad_grades_threshold:
            is_failed = True
            break

    command = input()

if is_failed:
    print(f"You need a break, {counter_fails} poor grades.")
else:
    print(f"Average score: {sum_of_grades / number_of_tasks :.2f}")
    print(f"Number of problems: {number_of_tasks}")
    print(f"Last problem: {task_name}")
juri_members = int(input())
command = input()

presentations_count = 0
total_score = 0


while command != "Finish":
    presentation = command
    presentations_count += 1

    current_grade = 0

    for grades_ in range(juri_members):
        judge_grade = float(input())
        current_grade += judge_grade

    print(f"{presentation} - {current_grade / juri_members :.2f}.")

    total_score += current_grade

    command = input()
total_average = total_score / (presentations_count * juri_members)          # за всяка презентация получаваме толкова оценки, колкото е броят на съдиите (не само 1)
print(f"Student's final assessment is {total_average :.2f}.")
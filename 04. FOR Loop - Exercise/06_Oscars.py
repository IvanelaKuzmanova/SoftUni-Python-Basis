actor_name = input()
actors_points = float(input())
juri_number = int(input())

for grades in range(juri_number):

    juri_member_name = input()
    points_given = float(input())
    points_from_juri = (len(juri_member_name) * points_given) / 2
    actors_points += points_from_juri

    if actors_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {actors_points :.1f}!")
        exit()

more_points_needed = 1250.5 - actors_points

print(f"Sorry, {actor_name} you need {more_points_needed :.1f} more!")
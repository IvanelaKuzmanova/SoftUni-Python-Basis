number_of_groups = int(input())

musala_count = 0
monblan_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for groups in range(number_of_groups):
    current_group_count = int(input())

    if current_group_count <= 5:
        musala_count += current_group_count
    elif 6 <= current_group_count <= 12:
        monblan_count += current_group_count
    elif 13 <= current_group_count <= 25:
        kilimanjaro_count += current_group_count
    elif 26 <= current_group_count <= 40:
        k2_count += current_group_count
    elif current_group_count >= 41:
        everest_count += current_group_count

total_climbers = musala_count + monblan_count + kilimanjaro_count + k2_count + everest_count

print(f"{musala_count / total_climbers :.2%}")
print(f"{monblan_count / total_climbers :.2%}")
print(f"{kilimanjaro_count / total_climbers :.2%}")
print(f"{k2_count / total_climbers :.2%}")
print(f"{everest_count / total_climbers :.2%}")


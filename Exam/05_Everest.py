command = input()

days_of_climbing = 1
climbed_height = 5364
mount_height = 8848

is_failed = False

while command != "END":
    daily_meters = int(input())

    if command == "Yes":
        days_of_climbing += 1
        if days_of_climbing > 5:
            is_failed = True
            break
        climbed_height += daily_meters
    elif command == "No":
        climbed_height += daily_meters

    if climbed_height >= mount_height:
        break

    command = input()

if is_failed or command == "END":
    print(f"Failed!")
    print(f"{climbed_height}")
else:
    print(f"Goal reached for {days_of_climbing} days!")

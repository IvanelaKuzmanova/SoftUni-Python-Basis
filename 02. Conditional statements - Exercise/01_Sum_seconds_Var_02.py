time_first = int(input())
time_second = int(input())
time_third = int(input())

sum_minutes = (time_first + time_second + time_third) // 60
seconds_left = (time_first + time_second + time_third) % 60

print(f'{sum_minutes}:{seconds_left :02d}')

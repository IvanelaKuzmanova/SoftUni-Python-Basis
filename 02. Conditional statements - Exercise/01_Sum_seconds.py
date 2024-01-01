import math

time_first = int(input())
time_second = int(input())
time_third = int(input())

sum_minutes = (time_first + time_second + time_third) // 60
seconds_left = (time_first + time_second + time_third) % 60

sum_minutes = math.floor(sum_minutes)

if seconds_left < 10:
    print(f'{sum_minutes} : 0 {seconds_left}')
else:
    print(f'{sum_minutes} : {seconds_left}')

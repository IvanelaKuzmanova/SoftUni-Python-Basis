hours = int(input())
minutes = int(input())
additional_minutes = 15
time = 0

if (minutes + additional_minutes) < 10:
    minutes = (f'0{minutes + additional_minutes}')
    time = (f'{hours}:{minutes}')


elif 10 <= (minutes + additional_minutes) <= 59:
    minutes = (f'{minutes + additional_minutes}')
    time = (f'{hours}:{minutes}')

else:
    hours_from_minutes = (minutes + additional_minutes) // 60
    minutes_last = (minutes + additional_minutes) % 60

    if minutes_last < 10:
        time = (f'{hours + hours_from_minutes}:0{minutes_last}')

    else:
        time = (f'{hours + hours_from_minutes}:{minutes_last}')


if (hours + hours_from_minutes) == 24:
    hours = 00

if hours == 24:
    hours = 00

print(time)

hours = int(input())
minutes = int(input())

total_time_minutes = hours * 60 + minutes + 15

total_hours = total_time_minutes // 60
total_minutes = total_time_minutes % 60

if total_hours == 24:
    total_hours = 00

print(f'{total_hours}:{total_minutes :02d}')


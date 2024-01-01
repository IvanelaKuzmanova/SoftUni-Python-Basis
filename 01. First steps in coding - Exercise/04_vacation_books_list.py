pages=int(input())
pages_per_hour=int(input())
days_to_finish=int(input())

hours_per_day=int((pages/pages_per_hour)/days_to_finish)

print(hours_per_day)

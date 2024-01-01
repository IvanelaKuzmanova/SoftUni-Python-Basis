days_off = int(input())

year = 365
playing_norm_minutes = 30_000
minutes_workday = 63
minutes_day_off = 127

working_days = year - days_off

playing_minutes_overall = working_days * minutes_workday + \
                          days_off * minutes_day_off

norm_difference = abs(playing_norm_minutes - playing_minutes_overall)

playing_hours_difference = norm_difference // 60
playing_minutes_difference = norm_difference % 60

if playing_minutes_overall > playing_norm_minutes:
    print(f"Tom will run away\n{playing_hours_difference} hours and {playing_minutes_difference} minutes more for play")
else:
    print(f"Tom sleeps well\n{playing_hours_difference} hours and {playing_minutes_difference} minutes less for play")


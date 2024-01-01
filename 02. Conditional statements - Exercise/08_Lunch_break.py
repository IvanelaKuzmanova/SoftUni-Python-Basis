import math

series_name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = (1/8) * break_time
relax_time = (1/4) * break_time

time_left = break_time - lunch_time - relax_time
free_time_after_episode = math.ceil(time_left - episode_time)
more_time_needed = math.ceil(episode_time - time_left)

if time_left >= episode_time:
    print(f"You have enough time to watch {series_name} and left with {free_time_after_episode} minutes free time.")

else:
    print(f"You don't have enough time to watch {series_name}, you need {more_time_needed} more minutes.")

import math

record_seconds = float(input())
distance_meters = float(input())
seconds_per_meter = float(input())

slow_down_seconds = math.floor(distance_meters / 15) * 12.5 #be careful if only the distance is floored or the whole result

swimming_time = distance_meters * seconds_per_meter + slow_down_seconds

slower_than_record = swimming_time - record_seconds

if swimming_time < record_seconds:
    print(f" Yes, he succeeded! The new world record is {swimming_time :.2f} seconds.")
else:
    print(f"No, he failed! He was {slower_than_record :.2f} seconds slower.")


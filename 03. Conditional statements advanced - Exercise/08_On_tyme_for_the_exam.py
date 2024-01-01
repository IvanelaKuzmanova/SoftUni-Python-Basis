exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time_minutes = exam_hour * 60 + exam_minutes
arrival_time_minutes = arrival_hour * 60 + arrival_minutes

difference_minutes = abs(exam_time_minutes - arrival_time_minutes)
difference_hours = abs(difference_minutes // 60)

if difference_minutes >= 60:
    difference_minutes = abs(difference_minutes % 60)
    # difference_hours = abs(difference_minutes // 60)

if exam_time_minutes < arrival_time_minutes:
    print("Late")

    if difference_minutes < 60 and difference_hours < 1:
        print(f"{difference_minutes} minutes after the start")
    elif difference_hours >= 1:
        print(f"{difference_hours}:{difference_minutes :02d} hours after the start")

elif exam_time_minutes > arrival_time_minutes:

    if difference_minutes <= 30 and difference_hours < 1:
        print("On time")
    else:
        print("Early")

    if difference_minutes < 60 and difference_hours < 1:
        print(f"{difference_minutes} minutes before the start")
    elif difference_minutes >= 60 or difference_hours >= 1:
        print(f"{difference_hours}:{difference_minutes :02d} hours before the start")

else:
    print("On time")



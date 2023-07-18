# modules
from datetime import datetime

# current day
day = datetime.today().strftime('%A')

def sch_day():
    # days
    if day == "Saturday":
        day_x0 = "Sat"
        day_x1 = "Sun"
        day_x2 = "Mon"
        day_x3 = "Tue"
        day_x4 = "Wed"
        day_x5 = "Thu"
        day_x6 = "Fri"

    elif day == "Sunday":
        day_x0 = "Sun"
        day_x1 = "Mon"
        day_x2 = "Tue"
        day_x3 = "Wed"
        day_x4 = "Thu"
        day_x5 = "Fri"
        day_x6 = "Sat"

    elif day == "Monday":
        day_x0 = "Mon"
        day_x1 = "Tue"
        day_x2 = "Wed"
        day_x3 = "Thu"
        day_x4 = "Fri"
        day_x5 = "Sat"
        day_x6 = "Sun"

    elif day == "Tuesday":
        day_x0 = "Tue"
        day_x1 = "Wed"
        day_x2 = "Thu"
        day_x3 = "Fri"
        day_x4 = "Sat"
        day_x5 = "Sun"
        day_x6 = "Mon"

    elif day == "Wednesday":
        day_x0 = "Wed"
        day_x1 = "Thu"
        day_x2 = "Fri"
        day_x3 = "Sat"
        day_x4 = "Sun"
        day_x5 = "Mon"
        day_x6 = "Tue"

    elif day == "Thursday":
        day_x0 = "Thu"
        day_x1 = "Fri"
        day_x2 = "Sat"
        day_x3 = "Sun"
        day_x4 = "Mon"
        day_x5 = "Tue"
        day_x6 = "Wed"

    elif day == "Friday":
        day_x0 = "Fri"
        day_x1 = "Sat"
        day_x2 = "Sun"
        day_x3 = "Mon"
        day_x4 = "Tue"
        day_x5 = "Wed"
        day_x6 = "Thu"
    
    return day_x0, day_x1, day_x2, day_x3, day_x4, day_x5, day_x6

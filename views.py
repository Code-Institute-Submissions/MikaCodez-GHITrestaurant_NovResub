from django.shortcuts import render
import calendar
from calendar import HTMLCalendar

def home(request, year, month):
    name= "user"
    month = month.capitalize()
    # convert month from name to number
    month_number = list(calendar.month_name).index(value)
    month_number = int(month_number)

    # create a calendar
    cal = HTMLCalendar().formatmonth(
        year, month_number)

    # current year
    now = datetime.now()
    current_year = now.year

    # current time
    time = now.strftime('%I:%M:%p')

    return render(request,
        'booking.html',{
            "name": name,
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal": cal,
            "current_year": current_year,
            "time": time,
        })
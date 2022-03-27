import calendar
import datetime

#sets the first day of the week as Sunday for the calendar
calendar.setfirstweekday(calendar.SUNDAY)


# gets current date to setup calendar for current date
def getDateForCalendar():
    _currentDateTime = datetime.datetime.now()
    yy = _currentDateTime.year
    mm = _currentDateTime.month
    dd = _currentDateTime.day

    _currentWeek = calendar.monthcalendar(yy, mm)

    _cal = calendar.month(yy, mm)
    
    return _cal

"""

for i in range(5):
    for y in range(7):
        if _currentWeek[i][y] == dd:
            ww = _currentWeek[i]        

print(_currentWeek)

"""
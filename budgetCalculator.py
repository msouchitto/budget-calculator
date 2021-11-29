from tkinter import *
from tkinter import ttk
import tkinter

"""
win = Tk()

win.title("Budget Calculator")
win.geometry("1024x768")

_exit = Button(win, text = "Exit", command=exit)

_exit.grid(row = 6, column= 6)

win.mainloop()

"""

import calendar
import datetime

calendar.setfirstweekday(calendar.SUNDAY)

_currentDateTime = datetime.datetime.now()
yy = _currentDateTime.year
mm = _currentDateTime.month
dd = _currentDateTime.day

_currentWeek = calendar.monthcalendar(yy, mm)



for i in range(5):
    for y in range(7):
        if _currentWeek[i][y] == dd:
            ww = _currentWeek[i]        

print(_currentWeek)


weeklyIncome = 510
monthlyIncome = weeklyIncome * 4

monthlyRent = 750

electricBill = 60
gasBill = 20

weeklyLunch = 6 * 5
monthlyLunch = weeklyLunch * 4

biMonthlyWaterBill = 150
monthlyWaterBill = biMonthlyWaterBill / 2

def calculateBills():
    return monthlyIncome - (monthlyRent + monthlyWaterBill + electricBill + monthlyLunch + gasBill) 

#print("Monthly income: $", monthlyIncome)
#print("Amount after all bills: $", calculateBills())
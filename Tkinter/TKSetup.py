from tkinter import *
from tkinter import font
from income import *
from calendarSetup import *
import tkinter.font as tkFont

def key(event):
    print ('pressed'), repr(event.char)

def callback(event):
    #print("Click at: ", event.x, event.y)
    print(event)



win = Tk()



#tkinter font setup
default_Font = tkFont.nametofont("TkDefaultFont")
default_Font.configure(family='Comic Sans MS', size = 22)


win.title("Budget Calculator")
win.geometry("1024x768")
#win.configure(bg='black')

#exit button
_exit = Button(win, padx = 10, pady = 10, text = "Exit", command=exit)

#display the calendar
_calendarView = Label(win, padx=20, pady = 20, text = getDateForCalendar())

#label for income and bill amount
_monthlyIncome = Label(win, text = "Monthly takehome income: $" + str(monthlyIncome))
_bills = Label(win, padx=10,text = "Bills: $" )
_calculatedIncome = Label(win, text="Money after bills: $" + str(calculateBills()))


#display the calendar
_calendarView.grid(row = 1, column = 1)


#clicking on the calendar calls the callback function which prints the position of the click
_calendarView.bind("<Key>", key)
_calendarView.bind("<Button-1>", callback)

#display income and bill amounts
_monthlyIncome.grid(row = 2, column = 3)
_calculatedIncome.grid(row = 3, column = 3)
_exit.grid(row = 6, column= 6)


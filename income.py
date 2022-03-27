from os import read
from fileReadWrite import *
from Transaction import *

weeklyIncome = readFromFile()
monthlyIncome = weeklyIncome * 4

monthlyRent = 750

electricBill = 60
gasBill = 20

weeklyLunch = Transaction("Lunch", 6)
monthlyLunch = weeklyLunch.price * 4

biMonthlyWaterBill = 150
monthlyWaterBill = biMonthlyWaterBill / 2

def sumBills():
    return monthlyRent + monthlyWaterBill + electricBill + monthlyLunch + gasBill

def calculateBills():
    return monthlyIncome - sumBills()
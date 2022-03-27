from Transaction import Transaction

class Day:
    def __init__(self, t, d):
        self.transactionList = [t]
        self.currentDate = d
    def setDay(self, _day):
        self.currentDate = _day
    def addTransaction(self, d):
        self.transactionList.append(d)
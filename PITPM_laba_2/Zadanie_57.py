import calendar

class Zate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def getYear(self):
        return self.year

    def getMonth(self):
        return self.month

    def getDay(self):
        return self.day

    def getWeekdayIndex(self):
        return calendar.weekday(self.year, self.month, self.day)

    def getWeekdayName(self):
        weekday_index = self.getWeekdayIndex()
        return calendar.day_name[weekday_index]

    def getMonthName(self):
        return calendar.month_name[self.month]

zate = Zate(2005, 4, 14)

print(zate.getYear())
print(zate.getMonth())
print(zate.getDay())
print(zate.getWeekdayIndex())
print(zate.getWeekdayName())
print(zate.getMonthName())
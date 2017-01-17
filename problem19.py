def daysInMonth(month,year):
    if month in [4,6,9,11]:
        return 30
    elif month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return 29
                else:
                    return 28
            else:
                return 29
        else:
            return 28
    else:
        return 31

class Date:
    def __init__(self,day=1,month=1,year=1900,weekday=1):
        self.day = day
        self.month = month
        self.year = year
        self.weekday = weekday

    def tomorrow(self):
        self.day += 1
        self.weekday = (self.weekday + 1) % 7
        if self.day > daysInMonth(self.month,self.year):
           self.day = 1
           self.month += 1
           if self.month > 12:
               self.month = 1
               self.year += 1

    def goTo(self,day,month,year,countingDay):
        days = 0
        while self.day != day or self.month != month or self.year != year:
           if self.weekday == countingDay and self.day == 1:
               days += 1
           self.tomorrow()
        return days
           

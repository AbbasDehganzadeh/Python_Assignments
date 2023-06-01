import datetime
import random


month_names = tuple(
    (
        [{"jan": "january"}, 31],
        [{"feb": "february"}, 28],
        [{"mar": "mars"}, 31],
        [{"apr": "april"}, 30],
        [{"may": "may"}, 31],
        [{"jun": "june"}, 30],
        [{"jul": "july"}, 31],
        [{"aug": "august"}, 31],
        [{"sep": "september"}, 30],
        [{"oct": "october"}, 31],
        [{"nov": "november"}, 30],
        [{"dec": "december"}, 31],
    )
)


class DateCalc:
    def __init__(self, y=1972, m=1, d=1):
        """It produces a date of [year, month, day]"""
        self.year = y
        self.month = m
        self.day = d
        DateCalc.normalize(self)

    def add_date(self, oth):
        """This adds two dates correspondingly"""
        d3 = DateCalc()
        d3.day = self.day + oth.day
        d3.month = self.month + oth.month
        d3.year = self.year + oth.year
        DateCalc.normalize(d3)
        return d3

    def sub_date(self, oth):
        """This subtracts two dates correspondingly"""
        d3 = DateCalc()
        d3.day = self.day - oth.day
        d3.month = self.month - oth.month
        d3.year = self.year - oth.year
        DateCalc.normalize(d3)
        return d3

    def normalize(d):
        """It normalize date with type of DateCalc"""
        if isinstance(d.day, int):
            max_days = month_names[d.month - 1][1]
            rem = d.day // max_days
            d.day %= max_days
        else:
            raise TypeError("invalid date for day")

        d.month += rem
        if isinstance(d.month, int):
            rem = d.month // 12
            d.month %= 12
        else:
            raise TypeError("Invalid date for month")

        d.year += rem
        if d.year < 0:  # negative year cases
            print("year should be positive")
            return DateCalc(1)

    def display(self, short=True, format_="-"):
        """It shows given date neatly"""
        d = self.day
        for month in month_names:
            mo = month[0]
            if month_names[self.month - 1] == month:
                f, s = mo.items()
                if short:
                    m = f
                else:
                    m = s

        y = self.year
        print(f" {format_} ".join([y, m, d]))


d1 = DateCalc(3, d=23)
d2 = DateCalc(m=4, d=10)

# d1.display()
# d2.display()

d3 = d1.add_date(d2)
d3.display()

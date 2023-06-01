import time
import random


class TimeCalc:
    def __init__(self, h=12, m=0, s=0):
        """It produces a timestamp of [hour, minute, second]"""
        self.hour = h
        self.minute = m
        self.second = s
        TimeCalc.normalize(self)

    @staticmethod
    def sec2time(sec):
        """It converts seconds to hours, minutes, and seconds"""
        t = TimeCalc(s, sec)
        TimeCalc.normalize(t)
        return t

    def time2sec(self, mode="s"):
        """It converts a TimeCalc to seconds, minutes, and hours
        mode: h=hours, m=minutes, s=seconds"""

        hour = self.hour
        if mode == "h":
            return hour

        minutes = hour * 60 + self.minute
        if mode == "m":
            return minutes

        seconds = minutes * 60 + self.second
        if mode == "s":
            return seconds

    def add_time(self, oth):
        """This adds two times correspondingly"""
        t3 = TimeCalc()
        t3.second = self.second + oth.second
        t3.minute = self.minute + oth.minute
        t3.hour = self.hour + oth.hour
        TimeCalc.normalize(t3)
        return t3

    def sub_time(self, oth):
        """This subtracts two times correspondingly"""
        t3 = TimeCalc()
        t3.second = self.second - oth.second
        t3.minute = self.minute - oth.minute
        t3.hour = self.hour - oth.hour
        TimeCalc.normalize(t3)
        return t3

    def normalize(t):
        """It normalize time with type of TimeCalc"""
        if isinstance(t.second, int):
            rem = t.second // 60
            t.second %= 60
        else:
            raise TypeError("invalid time type for second")

        t.minute += rem
        if isinstance(t.minute, int):
            rem = t.minute // 60
            t.minute %= 60
        else:
            raise TypeError("invalid time type for minute")

        t.hour += rem
        if t.hour < 0:  # negative hour cases
            print("hour should be positive!")
            return TimeCalc(0)

    def display(self):
        """It shows given time neatly"""
        print("{}:{}:{}".format(self.hour, self.minute, self.second))


t1 = TimeCalc(3, s=53)
t2 = TimeCalc(m=4, s=10)

# t1.display()
# t2.display()

t3 = t1.add_time(t2)
t3.display()

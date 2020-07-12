import os
import sys
sys.path.append(os.getcwd())
from adt.mydate import MyDate

def main():
    d = MyDate(month=7, year=2020, day=6)
    print(d.year())
    print(d.month(), d.monthName())
    print(d.day())
    print(d.isLeapYear())
    print(d.asGregorian())
    print(d.dayOfWeek())
    print(d.dayOfWeekName())
    print(d.isWeekday())
    print(d.dayOfYear())
    otherDate = MyDate(day=31,month=1, year=2020)
    print(d.numDays(otherDate=otherDate))
    print(d.advanceBy(2))



if __name__ == "__main__":
    main()
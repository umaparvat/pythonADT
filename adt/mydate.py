from time import localtime

class MyDate(object):

    def __init__(self, month=0, day=0, year=0000):
        self._julianDay = 0
        if not month or not day or not year:
            t = localtime()
            month, day, year = t.tm_mon, t.tm_mday, t.tm_year
        assert self._isValidGregorain(month, day, year), "Invalid Gregorian Date"
        tmp = 0
        if month < 3:
            tmp = -1
        self._julianDay = day - 32075 + (1461 * (year + 4800 + tmp) // 4) + (
                367 * (month - 2 - tmp * 12) // 12) - (3 * ((year + 4900 +tmp) // 100) // 4)

    def _isValidGregorain(self, month, day, year):
        """
        check given month, day, year is valid
        :param month:
        :param day:
        :param year:
        :return: True or False
        """
        month_day = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        if not 0 < month < 13:
            return False
        if not 0 < year < 10000:  # this shouldn't be 10000.
            return False
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            month_day[2] = 29
        if not 0 < day <= month_day[month]:
            return False
        return True

    def _toGregorian(self):
        """
        convert julian date to gregorian date
        :return:
        """
        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 4
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        month = 80 * A // 2447
        day = A - (2447 * month //80)
        A = month // 11
        month = month + 2 -(12 * A)
        year = 100 * (B - 49) + year + A
        return month, day, year
        
    def day(self):
        """
        returns gregorian day
        :return: day(int)
        """
        return self._toGregorian()[1]

    def month(self):
        """
        returns month
        :return:
        """
        return self._toGregorian()[0]

    def year(self):
        """
        returns year
        :return:
        """
        return self._toGregorian()[2]

    def monthName(self):
        """ returns name of the month"""
        MONTH = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
        return MONTH[self._toGregorian()[0] -1]

    def dayInMonth(self):
        """
        returns number of days in a month
        :return:
        """
        month_day = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        month_day[2] = month_day[2]+1 if self.isLeapYear()else month_day[2]
        return month_day[self.month()]

    def dayOfWeek(self):
        """
        Returns the number of the day
        Su represents 0 and saturday represents 6
        :return:
        """
        month, day, year = self._toGregorian()
        if month < 3:
            month += 12
            year -= 1            
        return (((13 * month + 3) //5 + day + year +year // 4 - year // 100 +year // 400) % 7) + 1

    def numDays(self, otherDate):
        """
        difference between two days in positive integer, includes the end date
        :param otherDate:
        :return:
        """
        if self._julianDay > otherDate._julianDay:
            return self._julianDay - otherDate._julianDay
        else:
            return otherDate._julianDay - self._julianDay

    def isLeapYear(self):
        """
        check year is leap year
        :return:
        """
        year = self.year()
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    def advanceBy(self, days):
        """
        Increment the date to given number of days. days can be positive or negative value
        :param days:
        :return:
        """
        self._julianDay = self._julianDay + days
        month, day, year = self._toGregorian()
        assert self._isValidGregorain(month, day, year), "Invalid days given"
        return str(self)

    def __eq__(self, otherDate):
        """
        compares two dates are equal
        :param otherDate:
        :return:
        """
        return self._julianDay == otherDate._julianDay

    def __lt__(self, otherDate):
        """
        compares other date is greater than given date
        :param otherDate:
        :return:
        """
        return self._julianDay < otherDate._julianDay

    def __le__(self, otherDate):
        """
        compares used date is less than or equal to given otherDate
        :param otherDate:
        :return:
        """
        return self._julianDay <= otherDate._julianDay

    def __str__(self):
        """
        string representation of the date
        :return:
        """
        month, day, year = self._toGregorian()
        return "{0:2d}/{1:2d}/{2:4d}".format(month,day, year)

    def dayOfWeekName(self):
        """
        uses zeller's method to find the day of week name
        k is day
        m is month
        D is last two digits of year
        c is first two digits of year
        # F = k +( (13*m -1)/5) +d+(d/4)+(c/4) -2*c
        :return: Su or Mo or Tu or We or Th or Fr or Sa
        """
        DAY = ("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")
        mon = {3: 1, 4:2, 5:3, 6:4, 7:5, 8:6, 9:7, 10:8, 11:9, 12:10, 1: 11, 2: 12}
        month, day, year = self._toGregorian()
        last_two_digit_year = year % 100
        first_digit_year = year // 100

        f = day +((13 * mon.get(month) - 1)// 5) + last_two_digit_year + (last_two_digit_year//4) + (first_digit_year//4) -2*first_digit_year
        day_remainder = f % 7
        return DAY[day_remainder]

    def isWeekday(self):
        """
        Return whether is a weekday
        :return:
        """
        week_name = self.dayOfWeekName()
        return week_name != "Su" or week_name != "Sa"

    def asGregorian(self, divchar='/'):
        """
        returns date with the given separator
        :param divchar:
        :return:
        """
        return str(self).replace("/", divchar)

    def dayOfYear(self):
        """
        Returns the number of days for the given date
        :return:
        """
        month, day, year = self._toGregorian()
        month_day = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }
        if self.isLeapYear():
            month_day[2] +=1
        total_days = 0
        for i in range(1, month):
            total_days += month_day[i]
        total_days += day
        return f"day {total_days} is of the {year}"


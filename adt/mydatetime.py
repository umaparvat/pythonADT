from adt.mydate import MyDate
from adt.mytime import MyTime


class MyDateTime(MyDate, MyTime):
	def __init__(self, month=0, day=0, year=0000, hours=0, minutes=0, seconds=0):
		MyDate.__init__(self, month, day, year)
		MyTime.__init__(self, hours, minutes, seconds)




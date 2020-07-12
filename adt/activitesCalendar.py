import sys
import os
sys.path.append(os.getcwd())
from adt.mydate import MyDate


class ActivitiesCalendar:
	def __init__(self, dateFrom, dateTo):
		self._startdate = MyDate(*map(int, dateFrom.split("/")))
		self._enddate = MyDate(*map(int, dateTo.split("/")))
		assert self._startdate < self._enddate, "dateTo should not overlap dateFrom"
		day = self._startdate.day()
		month = self._startdate.month()
		year = self._startdate.year() +1
		assert self._enddate < MyDate(month, day, year), "dateTo cannot be next year of the start date"
		self._dateFrom = dateFrom
		self._dateTo = dateTo
		self._activities = dict()

	def length(self):
		return len(self._activities)

	def getActivity(self, date):
		return self._activities.get(date, None)

	def addActivity(self, date, activity):
		assert self._startdate <= MyDate(*map(int, date.split("/"))) <= self._enddate, f"{date} " \
														   f"is out of {self._dateFrom} " \
														   f"and {self._dateTo}"
		if not self._activities.get(date):
			self._activities[date] = activity

	def displayMonth(self, month: str):
		MONTH = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
		ind = MONTH.index(month)+1
		strig = f"{month:^10} {self._startdate.year():<10}\n DATE    ACTIVITY\n------------------\n"
		for key in sorted(self._activities.keys()):
			if int(key.split("/")[0]) == ind:
				strig += f"\n{key} {self._activities.get(key)}"
		return strig

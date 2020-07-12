import sys
import os
sys.path.append(os.getcwd())
from adt.activitesCalendar import ActivitiesCalendar

def main():
	startDate = "7/12/2020"
	endDate = "7/8/2021"
	act = ActivitiesCalendar(startDate, endDate)
	print(act.length())
	eventdate = "7/12/2020"
	eventdate2 = "8/15/2020"
	act.addActivity(eventdate, "dancecalss")
	act.addActivity(eventdate2, "gym")
	print(act.getActivity(eventdate2))
	print(act.displayMonth("Jul"))

if __name__ == "__main__":
	main()
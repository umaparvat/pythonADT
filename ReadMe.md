## MyFraction
Python provides a numeric class for working with 
oating-point values. But
not all real numbers can be represented precisely on a computer since they are
stored as binary values. In applications where the precision of real numbers
is important, we can use rational numbers or fractions to store exact values.
A fraction, such as 7
8 , consists of two parts, both of which are integers. The
top value, which can be any integer value, is known as the numerator. The
bottom value, which must be greater than zero, is known as the denominator.
* Define a Fraction ADT to represent and store rational numbers. The ADT
should include all of the common mathematical and logical operations. In
addition, your ADT should provide for the conversion between 
oating-
point values and fractions and the ability to produce a string version of
the fraction.
* Provide a Python implementation of your Fraction ADT.

[Fraction ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/activitesCalendar.py)

## ActivityCalendar
Anyone who is involved in many activities typically uses a calendar to keep
track of the various activities. Colleges commonly maintain several calendars
such as an academic calendar, a school events calendar, and a sporting events
calendar. We have dened an Activities Calendar ADT below that can keep
track of one activity per day over a given range of dates. Select a data structure
and implement the ADT.
* **ActivitiesCalendar( dateFrom, dateTo )**: Creates a new empty activ-
ities calendar initialized to the given range of dates. The date range can
be specied for any non-overlapping period. The only requirements are
that dateFrom must precede dateTo and dateTo cannot overlap the day
and month of dateFrom for the next year.
* **length ()**: Returns the number of activities on the calendar.
* **getActivity( date )**: Returns the string that describes the activity for
the given date if an activity exists for the given date; otherwise, None is
returned.
* **addActivity( date, activity )**: Adds the given activity description to
the calendar for the given date. The date must be within the valid date
range for the calendar.
* **displayMonth( month )**: Displays to standard output all activities for the
given month. The display includes the year and name of the month and
the list of activities for the month. The display of each activity includes
the day of the month on which the activity occurs and the description
of the activity.
[Activity ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/activitesCalendar.py)

## LineSegment
A line segment is a straight line bounded by two endpoints. The Line Segment
ADT, whose operations are described below, represents a line segment dened
by points in the two-dimensional Cartesian coordinate system. Use the Point
class from Appendix D and implement the Line Segment ADT.
* **LineSegment( ptA, ptB )**: Creates a new Line Segment instance dened
by the two Point objects.
* **endPointA()**: Returns the rst endpoint of the line.
* **endPointB()**: Returns the second endpoint of the line.
* **length ()**: Returns the length of the line segment given as the Euclidean
distance between the two endpoints.
* **toString ()**: Returns a string representation of the line segment in the
format (Ax, Ay)#(Bx, By).
* **isVertical()**: Is the line segment parallel to the y-axis?
* **isHorizontal()**: Is the line segment parallel to the x-axis?
* **isParallel( otherLine )**: Is this line segment parallel to the otherLine?
* **isPerpendicular( otherLine )**: Is this line segment perpendicular to the
otherLine?
* **intersects(otherLine )**: Does this line segment intersect the otherLine?
* **bisects( otherLine )**: Does this line segment bisect the otherLine?
* **slope()**: Returns the slope of the line segment given as the rise over the
run. If the line segment is vertical, None is returned.
* **shift( xInc, yInc )**: Shifts the line segment by xInc amount along the
x-axis and yInc amount along the y-axis.
* **midpoint()**: Returns the midpoint of the line segment as a Point object.

[LineSegment]([Fraction ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/LineSegment.py))
## CounterBag
A click counter is a small hand-held device that contains a push button and
a count display. To increment the counter, the button is pushed and the new
count shows in the display. Clicker counters also contain a button that can be
pressed to reset the counter to zero. Design and implement the Counter ADT
that functions as a hand-held clicker.

[ConterBag]([Fraction ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/counter.py))
## GrabBag
A Grab Bag ADT is similar to the Bag ADT with one dierence. A grab
bag does not have a remove() operation, but in place of it has a grabItem()
operation, which allows for the random removal of an item from the bag.
Implement the Grab Bag ADT.

[grabbag]([Fraction ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/grabbag.py))

## RandomItemBag
A Counting Bag ADT is just like the Bag ADT but includes the numOf(item)
operation, which returns the number of occurrences of the given item in the
bag. Implement the Counting Bag ADT and defend your selection of data
structure.

[randombag]([Fraction ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/countbag.py))
## Date
A date represents a single day in the proleptic Gregorian calendar in which the
rst day starts on November 24, 4713 BC.
* ** Date( month, day, year ): Creates a new Date instance initialized to the
given Gregorian date which must be valid. Year 1 BC and earlier are indicated
by negative year components.
* **day()**: Returns the Gregorian day number of this date.
* **month()**: Returns the Gregorian month number of this date.
* **year()**: Returns the Gregorian year of this date.
* **monthName()**: Returns the Gregorian month name of this date.
* **dayOfWeek()**: Returns the day of the week as a number between 0 and 6 with
0 representing Monday and 6 representing Sunday.
* **numDays( otherDate )**: Returns the number of days as a positive integer be-
tween this date and the otherDate.
* **isLeapYear()**: Determines if this date falls in a leap year and returns the
appropriate boolean value.
* **advanceBy( days )**: Advances the date by the given number of days. The date
is incremented if days is positive and decremented if days is negative. The
date is capped to November 24, 4714 BC, if necessary.
* **comparable ( otherDate )**: Compares this date to the otherDate to deter-
mine their logical ordering. This comparison can be done using any of the
logical operators <, <=, >, >=, ==, !=.
* **toString ()**: Returns a string representing the Gregorian date in the format
mm/dd/yyyy. Implemented as the Python operator that is automatically called
via the str() constructor.

[MyDate]([Fraction ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/mydate.py))
## Time
We can use a Time ADT to represent the time of day, for any 24-hour period,
as the number of seconds that have elapsed since midnight. Given the following
list of operations, implement the Time ADT.
* **Time( hours, minutes, seconds )**: Creates a new Time instance and ini-
tializes it with the given time.
* **hour()**: Returns the hour part of the time.
* **minutes()**: Returns the minutes part of the time.
* **seconds()**: Returns the seconds part of the time.
* **numSeconds( otherTime )**: Returns the number of seconds as a positive
integer between this time and the otherTime.
* **isAM()**: Determines if this time is ante meridiem or before midday (at or
before 12 o'clock noon).
* **isPM()**: Determines if this time is post meridiem or after midday (after
12 o'clock noon).
* **comparable ( otherTime )**: Compares this time to the otherTime to de-
termine their logical ordering. This comparison can be done using any of
the Python logical operators.
* **toString ()**: Returns a string representing the time in the 12-hour format
hh:mm:ss. Invoked by calling Python's str() constructor.
[MyTime]([Fraction ADT](https://github.com/umaparvat/pythonADT/blob/master/adt/mytime.py))
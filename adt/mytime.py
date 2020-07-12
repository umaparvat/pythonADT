class MyTime:
    def __init__(self, hours, minutes, seconds):
        assert self._isValidTime(hours, minutes and seconds), "Invalid time input"
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds
        self._totaltime = self._timeinseconds(hours, minutes, seconds)
    @staticmethod
    def _timeinseconds(hours, minutes, seconds):
        totalsec = (hours * 3600) + (minutes * 60) +seconds
        return totalsec

    @staticmethod
    def _isValidTime(hours, minutes, seconds):
        return 0 < MyTime._timeinseconds(hours, minutes, seconds) <= 86400

    def hour(self):
        return self._hours

    def minutes(self):
        return self._minutes

    def seconds(self):
        return self._minutes

    def isAM(self):
        return  0 < self._totaltime <= 43200

    def isPM(self):
        return 43200 < self._totaltime <= 86400
        
    def numSeconds(self, otherTime):
        if self._totaltime < otherTime._totaltime:
             return otherTime._totaltime - self._totaltime
        else:
            return self._totaltime - otherTime._totaltime

    def _to24hours(self):
        hours = int(self._totaltime / 3600)
        minutes = (int(self._totaltime / 60)) % 60
        seconds = self._totaltime % 60
        return hours, minutes, seconds

    def _to12hours(self):
        if self.isPM():
            newTime = self._totaltime - 43200
            format = "PM"
        else:
            newTime = self._totaltime
            format = "AM"
        hours = int(newTime / 3600)
        minutes = (int(newTime / 60)) % 60
        seconds = newTime % 60
        return hours, minutes, seconds, format

    def __le__(self, otherTime):
        return self._totaltime <= otherTime._totaltime

    def __lt__(self, otherTime):
        return self._totaltime < otherTime._totaltime

    def __eq__(self, otherTime):
        return self._totaltime == otherTime._totaltime

    @staticmethod
    def _zfillchar(number):
        if number < 10:
            return str(number).zfill(2)

    def __str__(self):
        hours, minutes, seconds, format = self._to12hours()
        str_hours = self._zfillchar(hours)
        str_minutes = self._zfillchar(minutes)
        str_seconds = self._zfillchar(seconds)
        return f"{str_hours}:{str_minutes}:{str_seconds} {format}"

    def toString(self):
        return str(self)



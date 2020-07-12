class StudentFileReader:
    def __init__(self, filepath):
        self._file = filepath
        self._open = None

    def open(self):
        self._open = open(self._file, 'r')
        return self._open

    def close(self):
        self._open.close()
        self._open = None

    def fetchRecord(self):
        assert self._open, "File is not opened to read"
        data = self._open.readline()
        if data is None:
            return None
        record = StudentRecord(*data.split(", "))
        return record

    def fetchAll(self):
        assert self._open, "File is not opened to read"
        records = list()
        record = self.fetchRecord()
        while record is not None:
            records.append(record)
            record = self.fetchRecord()
        return records

    def _get_key(self, key):
        if key == "name":
            return lambda obj: (obj.firstname, obj.lastname)
        return lambda obj: getattr(obj, key)

    def sort(self, key='id'):
        records = self.fetchAll()
        sorted_data = list()
        if records is not None:
            sorted_data = sorted(records, key=self._get_key(key))
        return sorted_data

class StudenRecordWriter:
    def __init__(self, filepath=None):
        self._file = filepath
        self._open = None

    def open(self):
        self._open = open(self._file, "w")
        return self._open

    def writeRecord(self, record, format=" "):
        format_data = str(record).replace(" ", format)
        self._open.write(format_data)

    def writeAll(self, records, format=" "):
        if not records:
            return
        for each_student_rec in records:
            self.writeRecord(each_student_rec, format)

    def show(self, records):
        if isinstance(records, list):
            for line in records:
                print(str(line))
        else:
            print(str(records))

class StudentRecord:
    def __init__(self, studentid, firstname, lastname, year, gpa):
        self.studentid = int(studentid)
        self.firstname = firstname
        self.lastname = lastname
        self.year = int(year)
        self.gpa = float(gpa)

    def __str__(self):
        return f"{self.studentid} {self.firstname},{self.lastname} {self.year} {self.gpa}"


def main():

    fs = StudentFileReader("xys")
    fs.open()
    data = fs.fetchRecord()
    sorted_data = fs.sort(key="studentid")
    fw = StudenRecordWriter()
    fw.show(sorted_data)
    print()
    fw.show(data)


if __name__ == "__main__":
    main()

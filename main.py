def isLeapYear(year: int):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def isLeapYearChecker():
    year = 2001
    if isLeapYear(year):
        print("It is a leapyear")
    else:
        print("It is not a leapyear")


isLeapYearChecker()




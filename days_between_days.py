#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates.
#

def IsLeapYear(year):
    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    else:
        if month1 < month2:
            return True
        else:
            if day1 < day2:
                return True
            return False

def daysInMonth(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    else:
        if month==2:
            if IsLeapYear(year):
                return 29
            return 28
        else:
            return 30


def nextDate(year, month, date):
    if date < daysInMonth(month, year):
        return year, month, date+1
    else:
        if month < 12:
            return year, month+1, 1
        else:
            return year+1, 1, 1

def daysBetweenDates(year1, month1, date1, year2, month2, date2):
    days=0
    while dateIsBefore(year1, month1, date1, year2, month2, date2):
        year1, month1, date1 = nextDate(year1, month1, date1)
        days+=1


    return days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")


test()
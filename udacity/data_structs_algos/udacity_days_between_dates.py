def find_days_in_month(month, is_leap_year=False):
    if month == 2 and is_leap_year:
        return 29
    months_and_days = dict([(1, 31),(2, 28), (3,31), (4, 30), (5, 31), (6, 30), (7, 31), (8,31), (9, 30), (10, 31), (11, 30), (12, 31)])
    
    return months_and_days[month]


def determine_leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 400 == 0:
                return True
    return False 


def determine_is_before(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False


def find_next_day(year, month, day, days):
    if day < days:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def days_between_dates(cur_year, cur_month, cur_day, fut_year, fut_month, fut_day):
    assert determine_is_before(cur_year, cur_month, cur_day, fut_year, fut_month, fut_day)

    days = 0
    is_leap_year = determine_leap_year(cur_month)
    days_in_month = find_days_in_month(cur_month, is_leap_year)
    prev_year = cur_year
    prev_month = cur_month

    while determine_is_before(cur_year, cur_month, cur_day, fut_year, fut_month, fut_day):
        if cur_year != prev_year:
            is_leap_year = determine_leap_year(cur_year)
        if cur_month !=  prev_month:
            days_in_month = find_days_in_month(cur_month, is_leap_year)
        prev_year = cur_year
        prev_month = cur_month
        cur_year, cur_month, cur_day = find_next_day(
            cur_year, cur_month, cur_day, days_in_month)
        days += 1
    
    return days

def test_find_days_in_month():
    assert find_days_in_month(3) == 31
    assert find_days_in_month(2, True) == 29
    assert find_days_in_month(12) == 31
    assert find_days_in_month(9) == 30

def test_determine_leap_year():
    assert determine_leap_year(1992) == True
    assert determine_leap_year(2000) == True
    assert determine_leap_year(1900) == False
    assert determine_leap_year(2100) == False
    assert determine_leap_year(2012) == True


def test_find_next_day():
    assert find_next_day(2013, 1, 2, 31) == (2013, 1, 3)
    assert find_next_day(2013, 1, 30, 31) == (2013, 1, 31)
    assert find_next_day(2013, 12, 31, 31) == (2014, 1, 1)


def test_determine_is_before():
    assert determine_is_before(2013, 1, 2, 2014, 1, 2) == True
    assert determine_is_before(2013, 1, 2, 2013, 2, 2) == True
    assert determine_is_before(2013, 1, 2, 2013, 1, 3) == True
    assert determine_is_before(2013, 1, 2, 2013, 1, 2) == False


def test_days_between_dates():
    
    # test same day
    # assert(days_between_dates(2017, 12, 30, 2017, 12, 30) == AssertionError)

    # test adjacent days
    assert(days_between_dates(2017, 12, 30, 2017, 12, 31) == 1)
    # test new year
    assert(days_between_dates(2017, 12, 30, 2018, 1,  1)  == 2)
    # test full year difference
    assert(days_between_dates(2012, 6, 29, 2013, 6, 29)  == 365)
    
    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")

test_find_days_in_month()
test_determine_leap_year()
test_find_next_day()
test_determine_is_before() 
test_days_between_dates()

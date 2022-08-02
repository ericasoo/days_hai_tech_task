""" A delta of days
"""
################################################################################
# Author: Erica Soo
# July 2022
################################################################################


import re

## function: date_to_days
## counts the number of days before each date starting from the date "0000-01-01"
## assumptions: user will not enter a date "BC"
def date_to_days(date, month_lengths):

    year, month, day = date.split("-")
    year = int(year)
    month = int(month)
    day = int(day)

    # add years and days
    num_days = year * 365 + day

    # add months
    for i in range(0, month - 1):
        num_days += month_lengths[i]

    # account for leap years
    if month <= 2:
        year -= 1
    # gregorian calendar began in 1582
    num_leap_days = 0
    if (year >= 1582):
        num_leap_days = (year // 4) - (year // 100) + (year // 400)
    num_days += num_leap_days

    return num_days

## function: valid_input
## determines whether the input dates are valid
## returns boolean value for validity
def valid_input(date, month_lengths):
    valid = 1

    # checking expected format
    date_pattern = "^[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}$"
    matched = re.match(date_pattern, date)
    if not bool(matched):
        valid = 0
        print("The date {} is invalid".format(date))
        return valid

    year, month, day = date.split("-")

    # checking all values are digits
    if (not year.isdigit()) or (not month.isdigit()) or (not day.isdigit()):
        valid = 0
        print("The date {} is invalid".format(date))
        return valid

    
    year = int(year)
    month = int(month)
    day = int(day)
    
    # check date is valid
    curr_month_length = month_lengths[month-1]
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) and month == 2:
        curr_month_length = 29

    if ((day > curr_month_length) or (month > 12) or (year < 1000 or year > 9999)):
        valid = 0
        print("The date {} is invalid".format(date))

    return valid


## function: find_dates
## calculates the number of days between two input dates
def find_days(date1, date2, month_lengths):


    num_days1 = date_to_days(date1, month_lengths)
    num_days2 = date_to_days(date2, month_lengths)

    days_between = abs(num_days2 - num_days1)

    if days_between > 0:
        days_between -= 1

    print("{} days between {} and {}".format(days_between, date1, date2))
    return days_between




def main():

    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    date1_valid = 0
    date2_valid = 0
    while (not date1_valid):
        date1_input = input("Please enter a date in the format YYYY-MM-DD: ")
        if valid_input(date1_input, month_lengths):
            date1_valid = 1
    
    while (not date2_valid):
        date2_input = input("Please enter another date in the format YYYY-MM-DD: ")
        if valid_input(date2_input, month_lengths):
            date2_valid = 1
    
    diff3 = find_days(date1_input, date2_input, month_lengths)



if __name__ == "__main__":
    main()
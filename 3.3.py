def LeapYear(year):
    if year % 4 == 0:
        return 'Could be a leap year.'
    else:
        return 'Definitely not a leap year'

#DriverCode
year = int(input('Enter year: '))
x = LeapYear(year)
print(x)

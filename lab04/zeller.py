"""CS 108 - Lab 4.2

Zeller formula, calculates dates

@author: Ben Elpidius (bee6)
@author: Andrew Jackson (amj34)
@date: Fall, 2021
"""

year = int(input('Enter year: '))
month = int(input('Enter month: '))
day = int(input('Enter day: '))

#calculates the day of the week (0 to 6)
if month == 1:
    month = 13         #changes the month to 13
    year = year - 1  
    h = (day + (((month+1)*26) // 10) + (year % 100) + ((year % 100) // 4) + ((year // 100) // 4) + 5*(year // 100)) % 7
elif month == 2:
    month = 14         #changes the month to 14
    year = year - 1
    h = (day + (((month+1)*26) // 10) + (year % 100) + ((year % 100) // 4) + ((year // 100) // 4) + 5*(year // 100)) % 7
else:                  #if it is not 1 or 2, just calculates it without changing the variables
    h = (day + (((month+1)*26) // 10) + (year % 100) + ((year % 100) // 4) + ((year // 100) // 4) + 5*(year // 100)) % 7

#list of weekdays
weekdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

print(weekdays[h])   
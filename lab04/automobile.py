"""CS 108 - lab 4.0

program for an automobile service

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

#user inputs oil change, tire rotation, or car wash
services = input('service: ')

if services == 'oil change':               #set as oil change
    print('cost of oil change: $35')

elif services == 'tire rotation':          #set as tire rotation
    print('cost of tire rotation: $19')

elif services == 'car wash':               #set as car wash
    print('cost of car wash: $7')

else:                                      #error
    print('error:', services, 'is not recognized')
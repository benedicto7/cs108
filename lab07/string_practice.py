"""CS 108 - Lab 7.0

String Practice

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

user = input('Full Name: ')

# user inputted name is separated into a list and ordered by index
separated_list = user.split(' ')

if len(separated_list) == 3:
    first_name = separated_list[0]       # make a variable that holds first name so that we can take the initial 
    first_initial = first_name[0] 
    middle_name = separated_list[1]      # make a variable that holds the middle name so that we can take the initial
    middle_initial = middle_name[0]
    last_name = separated_list[2]
    print(last_name + ',', first_initial + '.' + middle_initial + '.')

elif len(separated_list) == 2:
    first_name = separated_list[0]       # make a variable that holds first name so that we can take the initial
    first_initial = first_name[0]
    middle_name = separated_list[1]      # make a variable that holds the middle name so that we can take the initial
    middle_initial = middle_name[0]
    print(middle_name + ',', first_initial + '.')

else:
    print("'" + user + "'", 'is a non-standard name.')

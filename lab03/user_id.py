"""CS 108 - Lab 3.1

Creating User ID

@author: Ben Elpidius (bee6)
@author: Steven McKelvey (smm56)
@date: Fall, 2021
"""

#input for the given variables
first_name = input('First name: ')
last_name = input('Last name: ')
student_id = input('Student ID: ')

#concatenating to make a user ID and lowercase the ID
login = first_name[0] + last_name + student_id[0] + student_id[1]
login = login.lower()

print('User ID: ' + login)
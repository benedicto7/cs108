"""CS 108 - Lab 7.1

Making SSN

@author: Ben Elpidius (bee6)
author: Chongxiang Ju (cj43)
@date: fall, 2021
"""

# function for returning true or false for a SSN
def is_valid_ssn(user):
    if user[0:3].isdigit() and user[4:6].isdigit() and user[7:11].isdigit() and len(user) == 11:
        return True
    else:
        return False

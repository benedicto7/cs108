"""CS 108 - Lab 7.2

Making password validation

@author: Ben Elpidius (bee6)
author: Chongxiang Ju (cj43)
@date: fall, 2021
"""

# function that returns True or False for a password.
# True if password is either a number or a digit, has at least 8, has at least 2 numbers.
def is_valid_password(user):
    if len(user) >= 8 and user.isalnum():    # checks if password is at least 8 and is either a number or letter
        count = 0
        for i in user:                       # loop that increment by 1 if the i in user is a digit
            if i.isdigit():
                count = count + 1           
        if count >= 2:
            return True
        else:
            return False
    else:
        return False


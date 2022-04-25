"""CS 108 - Lab 7.3

Making password validation

@author: Ben Elpidius (bee6)
author: Chongxiang Ju (cj43)
@date: fall, 2021
"""

# function for a valid first 2 prefix
def is_valid_prefix(user): 
    if user[0:2]=='37' or user[0]=='4' or user[0]=='5' or user[0]=='6':
        return True
    else:
        return False

# function for sum of odds
def sum_of_odds(user): 
    block = user[-1:-len(user)-1:-2]
    count = 0
    for i in block:
        count = count + int(i)
    return count

# function for sum of evens, doubled and if 5-9 is the addition of the two number
def sum_of_double_evens(user):
    block = user[-2:-len(user)-1:-2]
    count1 = 0
    count2 = 0
    for i in block:
        if i <= str(4):                         # single digits
            count1 = count1 + int(i) * 2
        if i >= str(5):                         # double digits
            x = int(i) * 2
            y = x - 9
            count2 = count2 + y
    return count1 + count2

# function for valid prefix is True, and is all a number, sum of odd + sum of double evens divisible by 10 and the total length between 13 and 16
def is_valid_cc(cc):    
    if is_valid_prefix(cc) == True and cc.isdigit() and (sum_of_odds(cc) + sum_of_double_evens(cc)) % 10 == 0 and len(cc) >= 13 and len(cc) <= 16:
        return True
    else:
        return False
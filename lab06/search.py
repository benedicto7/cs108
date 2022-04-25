"""CS 108 - Homework 6.1

Searching a list

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

# function of search() that returns i if it is the same with the element in the list, or -1 if it is not in the list.
def search(str_list, target):
    for i in range(len(str_list)):  
        if target == str_list[i]:
            return i
    return -1

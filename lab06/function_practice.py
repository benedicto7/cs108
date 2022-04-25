"""CS 108 - Lab 6.0

Function practice 

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

def compute_cost(miles, miles_per_gallon, dollars_per_gallon):  
    return (miles / miles_per_gallon) * dollars_per_gallon

def count_spaces(s):
    count = 0
    for c in s:
        if c == ' ':
            count = count + 1
    return count

a = count_spaces('o n e s')
print(a)
    

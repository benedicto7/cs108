"""CS 108 - Lab 5.0

output range with increments of 10

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

#user inputs two integers
first = int(input())
second = int(input())

#if statement, executes when first is bigger. if it is false, goes to while statement. 
if first > second:
    print("Second integer can't be less than the first.")

while first <= second:
    print(first)
    first = first + 10
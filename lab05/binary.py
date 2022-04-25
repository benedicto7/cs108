"""CS 108 - Lab 5.1

Convert to binary

@author: Ben Elpidius (bee6)
@author: Caden Ziskie (cmz7)
@date: fall, 2021
"""

#user inputted
x = int(input('integer: '))

#if x greater than 0, executes. prints the result of x % 2, then sets new x.
while x > 0:
    print(x % 2, end='')
    x = x // 2
print()
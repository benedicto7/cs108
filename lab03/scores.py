"""CS 108 - Lab 3.2

Store scores in a dictionary

@author: Steven McKelvey (smm56)
@author: Ben Elpidius (bee6)
@date: Fall, 2021
"""

score_dict = {'Joe' : 10, 'Tom' : 23, 'Barb' : 13, 'Sue' : 19, 'Sally' : 12}


print(score_dict['Barb'])

#update Sally's score
score_dict['Sally'] = 13

#delete Tom and his score from the dictionary
del score_dict['Tom']

#print the entire final dictionary
print(score_dict)
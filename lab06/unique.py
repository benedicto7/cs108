"""CS 108 - Lab 6.2

Function that writes unique words into a list.

@author: Ben Elpidius (bee6)
@author: Caleb Albrecht (cma27)
@date: fall, 2021
"""

# function for search to see if str_list (user inputted) is not in unique_word
def search(str_list, target):
    for i in range(len(str_list)):  
        if target == str_list[i]:
            return i
    return -1

# function for outputting unique_words
def get_unique_words(str_list):
    unique_words = []
    for i in str_list:
        if search(unique_words, i) == -1:
            unique_words.append(i)
    return unique_words

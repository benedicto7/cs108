"""CS 108 - Lab 2.1

Einstein Theory

@author: YOUR-NAME (yourid123)
@author: PARTNER-NAME (theirid123)
@date: semester, year
"""

num = int(input('Enter a three digit number: '))

#when dividing with // 100, it gives only the 100s digit.
digit_1 = num // 100

#using the value from digit_1, * 100 so that it becomes a 3 digit value. Minus that with the user inputted value, erases the 100s digit and then dividing with // 10 gives the 10s digit only.
digit_2 = (num - (digit_1 * 100)) // 10

#using the user inputted value, using // 10 gives the 100s and 10s digit only. * 10 gives a 3 digit value and the minusing with the user inputted value will give the 1s digit. 
digit_3 = num - (num // 10) * 10

#using the value of digit 3, * 100 to make it into a 3 digit value. Using value of digit 2, * 10 to make it into a 2 digit value. and so on.
rev_numb = (digit_3 * 100) + (digit_2 * 10) + (digit_1)

#absolute to make it positive regardless.
difference = abs(num - rev_numb)

diff_digit_1 = difference // 100
diff_digit_2 = (difference - (digit_1 * 100)) // 10
diff_digit_3 = difference - (num // 10) * 10

rev_diff = (diff_digit_3 * 100) + (diff_digit_2 * 10) + (diff_digit_1)

print('Difference is ', difference, 'and rev_diff is ', rev_diff)

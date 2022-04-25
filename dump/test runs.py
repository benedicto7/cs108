test = input('name: ')
print('your name is' + test)

test2 = input('name: ')
print('your name is', test)

# ----------------------------------------

x = int(input('number'))
y = int(input('number'))
z = int(input('number'))
largest = x
if y > largest:
    largest = y
if z > largest:
    largest = z
print(largest)

# ---------------------------
# Iterating N times using a loop variable
i = 1
while i <= 10:
    print(i, end=' ')
    i = i + 1

# ------------------------------------------

nose = '0'  # Looks a little like a nose
user_value = '-'

while user_value != 'q':
    print(' {} {} '.format(user_value, user_value))  # Print eyes
    print('  {}  '.format(nose))  # Print nose
    print(user_value*5)  # Print mouth
    print('\n')

    # Get new character for eyes and mouth
    user_input = input("Enter a character ('q' for quit): \n")
    user_value = user_input[0]

print('Goodbye.\n')

# ---------------------------------------

for name in ['Bill', 'Nicole', 'John']:
  print('Hi {}!'.format(name))

# ---------------------------------------

my_str = ''
for character in "Take me to the moon.":
    my_str += character + '_'
print(my_str)

# -----------------------------------------

channels = {
    'MTV': 35,
    'CNN': 28,
    'FOX': 11,
    'NBC': 4,
    'CBS': 12
}
for c in channels:
    print('{} is on channel {}'.format(c, channels[c]))
    
# -----------------------------------------------------------

empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):
        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        # Find first meal option that exactly matches user money
        if meal_cost == user_money:
            break

    # Find first meal option that exactly matches user money
    if meal_cost == user_money:
        break

if meal_cost == user_money:
    print('${} buys {} empanadas and {} tacos without change.'
        .format(meal_cost, num_empanadas, num_tacos))
else:
    print('You cannot buy a meal without having change left over.')
    
# --------------------------------------------------------------------------

empanada_cost = 3
taco_cost = 4

user_money = int(input('Enter money for meal: '))

num_diners = int(input('How many people are eating: '))

max_empanadas = user_money // empanada_cost
max_tacos = user_money // taco_cost

meal_cost = 0
num_options = 0
for num_tacos in range(max_tacos + 1):
    for num_empanadas in range(max_empanadas + 1):

        # Total items purchased must be equally divisible by number of diners
        if (num_tacos + num_empanadas) % num_diners != 0:
            continue

        meal_cost = (num_empanadas * empanada_cost) + (num_tacos * taco_cost)

        if meal_cost == user_money:
            print('${} buys {} empanadas and {} tacos without change.'
                  .format(meal_cost, num_empanadas, num_tacos))
            num_options += 1

if num_options == 0:
    print('You cannot buy a meal without having change left over.')
    
# -------------------------------------------------------------

for i in range(3):
    print('the number is', i)
print('goodbye')

for i in range(4):
    if i == 3:
        break
    print('the number is', i)
print('goodbye')

# --------------------------------------

print('hello')
for x in [2, 7, 1]:
    print('the number is', x)
print('goodbye')

print('hello')
l = [2, 7, 1]
for i in range(len(l)):
    print('the number is', l[i])
print('goodbye')

print('hello')
l = [2, 7, 1]
i = 0
while i < len(l):
    print('the number is', l[i])
    i = i + 1
print('goobye')

# ------------------------

n = int(input('how many?'))
for i in range(n):
    score = int(input('score #' + str(i+1) + ': '))
    print(str(score) + '/20 is ' + str(score * 5) + '%\n')
print('goodbye')

score = int(input('score (negative to quit): '))
while score >= 0:
    print(str(score) + '/20 is ' + str(score *5) + '%\n')
    score = int(input('score (negative to quit): '))
print('goodbye')

while True:
    score = int(input('score (negative to quit): '))
    if score < 0:
        break
    print(str(score) + '/20 is ' + str(score *5) + '%\n')
print('goodbye')

# ----------------------------------------------------------------

password = input('enter password: ')
while len(password) < 8:
    print('try again')
    password = input('enter password: ')
print('good password')

while True:
    password = input('enter password')
    if len(password) < 8:
        print('try again')
    else:
        print('good password')
        break
# If there is time, give the user only three chances to enter a valid password -> for

# ------------------------------------------------

for i in range(100):
    if (i % 15) == 0:
        print('fizzbuzz')
    if (i % 3) == 0:
        print('fizz')
    elif (i % 5) == 0:
        print('buzz')
    else:
        print(i)

# -------------------------------------

def calc_pizza_area():
  pi_val = 3.14159265

  pizza_diameter = 12.0
  pizza_radius = pizza_diameter / 2.0
  pizza_area = pi_val * pizza_radius * pizza_radius
  return pizza_area

print('{:.1f} inch pizza is {:.3f} square inches'
      .format(12, calc_pizza_area()))

# -------------------------------------------------------

def compute_square(num_to_square):
    return num_to_square * num_to_square
num_squared = compute_square(7)
print('7 squared is', num_squared)

# ---------------------------------------------

def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    return feet
def steps_to_calories(num_steps):
    steps_per_minute = 70.0
    calories_per_minute_walking = 3.5

    minutes = num_steps / steps_per_minute
    calories = minutes * calories_per_minute_walking
    return calories

steps = int(input('Enter number of steps walked: '))
feet = steps_to_feet(steps)
print('Feet:', feet)
calories = steps_to_calories(steps)
print('Calories:', calories)

# --------------------------------------------

employee_name = 'N/A'

def get_name():
    global employee_name
    name = input('Enter employee name:')
    employee_name = name

get_name()
print('Employee name:', employee_name)

# ----------------------------------------------

def print_date(day, month, year, style=0):
    if style == 0:  # American
        print(month, '/', day, '/', year)
    elif style == 1:  # European
        print(day, '/', month, '/', year)
    else:
        print('Invalid Style')

print_date(30, 7, 2012, 0)
print_date(30, 7, 2012, 1)
print_date(30, 7, 2012)  # style argument not provided! Default value of 0 used.

# ---------------------------------------------------------------------------------------

def append_to_list(value, my_list=None):  # Use default parameter value of None
    if my_list == None:  # Create a new list if a list was not provided
        my_list = []
    my_list.append(value)
    return my_list
numbers = append_to_list(50)  # default list appended with 50
print(numbers)
numbers = append_to_list(100)  # default list appended with 100
print(numbers)


def append_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list
numbers = append_to_list(50)  # default list appended with 50
print(numbers)
numbers = append_to_list(100)  # default list appended with 100 = 50 and 100
print(numbers)

# ----------------------------------------------------------------------------------

s = input() # finishes loop first, does all input then prints final
count = 0
for c in s:
    if c == ' ':
        count = count + 1
print(count)

s = input() # prints all, but fluctuates
count = 0
for c in s:
    if c == ' ':
        count = count + 1
    print(count)

s = input() # prints everytime c == ' '
count = 0
for c in s:
    if c == ' ':
        count = count + 1
        print(count)

# ---------------------------------------------

def rectangle(): # write a function that READS after calling
    w = float(input('width: '))
    h = float(input('height: '))
    area = w * h
    return area

a = rectangle()
print(a)

def rectangle(width, height): # write a function that RECEIVES the width and height
    area = width * height
    return area

a = rectangle(int(input('width: ')), int(input('height: ')))
print(a)

# ------------------------

names =[]
print('enter name: ')
while True:
    name = input('name: ')
    if name == '':
        break
    names.append(name)
print(name)

# ---------------------------------

names =[]
print('enter name: ')
while True:
    name = input('name: ')
    if name == '':
        break
    names.append(name)
print(name)

def names():
    name = []
    print('enter name')
    while True:
        names = input('name: ')
        if names == '':
            break
        name.append(names)
    return name

print(names())

# ----------------------------------------

word = 'onomatopoeia'
num_guesses = 10

hidden_word = '-' * len(word)

guess = 1

while guess <= num_guesses and '-' in hidden_word:
    print(hidden_word)
    user_input = input('Enter a character (guess #{}): '.format(guess))
    
    if len(user_input) == 1:
        # Count the number of times the character occurs in the word
        num_occurrences = word.count(user_input)
    
        # Replace the appropriate position(s) in hidden_word with the actual character.
        position = -1
        for occurrence in range(num_occurrences):
            position = word.find(user_input, position+1)  # Find the position of the next occurrence
            hidden_word = hidden_word[:position] + user_input + hidden_word[position+1:]  # Rebuild the hidden word string
    
        guess += 1
        
if not '-' in hidden_word:
    print('Winner!', end=' ')        
else:
    print('Loser!', end=' ')

print('The word was {}.'.format(word))

# ---------------------------------------------------

menu_prompt = ('Available commands:\n'
               '  (add) Add passenger\n'
               '  (del) Delete passenger\n'
               '  (print) Print passenger list\n'
               '  (exit) Exit the program\n'
               'Enter command:\n')

destinations = ['PHX', 'AUS', 'LAS'] 

destination_prompt = ('Available destinations:\n'
                      '(PHX) Phoenix\n'
                      '(AUS) Austin\n'
                      '(LAS) Las Vegas\n'
                      'Enter destination:\n')

passengers = {}

print('Welcome to Mohawk Airlines!\n')
user_input = input(menu_prompt).strip().lower()

while user_input != 'exit':
    if user_input == 'add':
        name = input('Enter passenger name:\n').strip().upper()
        destination = input(destination_prompt).strip().upper()
        if destination not in destinations:
            print('Unknown destination.\n')
        else:
            passengers[name] = destination
            
    elif user_input == 'del':
        name = input('Enter passenger name:\n').strip().upper()
        if name in passengers:
            del passengers[name]

    elif user_input == 'print':
        for passenger in passengers:
            print('{} --> {}'.format(passenger.title(), passengers[passenger]))
    else:
        print('Unrecognized command.')

    user_input = input('Enter command:\n').strip().lower()
  
# -----------------------------------------------------------------

def palindrome(user):
    if user[::1] == user[::-1]:
        return True
    else:
        return False

print(palindrome('bob'))

# ---------------------------------

"""accumulator
initialize an accumulator/make an place holder
loop for each element in list/string/collection:
    if current element 'matches' then:
        update the accumular (e.g place holder = place holder + element
"""

'I\'m Adam' 

def function(s):
    answer = ''
    for c in s:
        if c.isalpha():
            answer = answer + c
    return answer

def palindrome(user):
    x = function(user)  # Madam 2
    s = x.lower()
    if s[::1] == s[::-1]:
        return True
    else:
        return False

print(palindrome("Madam, I'm Adam!"))

# ------------------------------------------

grades = {
    'John Ponting': {
        'Homeworks': [79, 80, 74],
        'Midterm': 85,
        'Final': 92
    },
    'Jacques Kallis': {
        'Homeworks': [90, 92, 65],
        'Midterm': 87,
        'Final': 75
    },
    'Ricky Bobby': {
        'Homeworks': [50, 52, 78],
        'Midterm': 40,
        'Final': 65
    },
}

user_input = input('Enter student name: ')

while user_input != 'exit':
    if user_input in grades:
        # Get values from nested dict
        homeworks = grades[user_input]['Homeworks']
        midterm = grades[user_input]['Midterm']
        final = grades[user_input]['Final']

        # print info
        for hw, score in enumerate(homeworks):
            print('Homework {}: {}'.format(hw, score))

        print('Midterm: {}'.format(midterm))
        print('Final: {}'.format(final))

        # Compute student total score
        total_points = sum([i for i in homeworks]) + midterm + final
        print('Final percentage: {:.1f}%'.format(100*(total_points / 500.0)))

    user_input = input('Enter student name: ')

# ---------------------------------------------------------------------------------

grid = [
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
['Y', ' ', ' ', ' ', 'Y', 'Y', ' '],
['R', ' ', ' ', 'Y', 'R', 'R', ' '],
['R', 'R', 'Y', 'R', 'Y', 'R', ' '],
['R', 'Y', 'R', 'Y', 'Y', 'Y', 'R'],
]
count = 0
for i in range(len(grid)): # outer loop
    print("row =", grid[i])
    for j in range(len(grid[i])): # inner loop
        print("cell =", grid[i][j])
        if j == ' ':
            count += 1
print(count, "spaces remaining")

# -------------------------------------------

grid = [
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
[' ', ' ', ' ', ' ', ' ', ' ', ' '],
['Y', ' ', ' ', ' ', 'Y', 'Y', ' '],
['R', ' ', ' ', 'Y', 'R', 'R', ' '],
['R', 'R', 'Y', 'R', 'Y', 'R', ' '],
['R', 'Y', 'R', 'Y', 'Y', 'Y', 'R'],
]
count = 0
for row in grid: # outer loop
    print("row =", row)
    for cell in row: # inner loop
        print("cell =", cell)
        if cell == ' ':
            count = count + 1
print(count, "spaces remaining")

# -----------------------------------------

chart = [['X', ' ', 'X', ' '],
         [' ', 'X', ' ', 'X'],
         ['X', ' ', 'X', ' '],
         [' ', 'X', ' ', 'X']]

def seat_taken(x, y): # x = row, y = collumn
    if chart[x][y] == 'X':
        return True # taken
    else:
        return False # not taken
print(seat_taken(int(input('x: ')), int(input('y: '))))

def seat_taken2(x, y):
    is_taken = chart[x][y] == 'X'
    return is_taken
print(seat_taken2(int(input('x: ')), int(input('y: '))))

def seat_taken(chart): # x = row, y = collumn
    count = 0
    for row in chart:
        for collumn in row:
            if collumn == 'X':
                count = count + 1
    return count
    
# ----------------------------------------

total=[]
file = open('data.txt', 'r')    
lines = file.readlines()
for i in lines:
    total.append(int(i))
file.close()
print(total)

# -----------------------------

total = []
file = open('data.txt', 'r')
lines = file.readlines()
for i in lines:
    values = i.split(',')
    x = int(values[0]), int(values[1]), int(values[2]), int(values[3])
    total.append(x)
file.close()
print(total)

# ---------------------------------

from guizero import App, PushButton, Text

def destroy_message():
    message.destroy()

app = App()
message = Text(app, text="Destroy me!")
destroy_button = PushButton(app, text="Destroy", command=destroy_message)

app.display()

# --------------------------

from guizero import App, PushButton, TextBox

def show():
    text_box.show()

def hide():
    text_box.hide()

def enable():
    text_box.enable()

def disable():
    text_box.disable()

app = App()

text_box = TextBox(app)

show_button = PushButton(app, text="show", command=show)
hide_button = PushButton(app, text="hide", command=hide)
enable_button = PushButton(app, text="enable", command=enable)
disable_button = PushButton(app, text="disable",command=disable)

app.display()

# ---------------------

from time import sleep

text = 0
while True:
    text = text + 1
    sleep(1)
    print(text)

# -------------------------

from guizero import App, Text

# Action you would like to perform
def counter():
    text.value = int(text.value) + 1

app = App("Hello world")
text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms
app.display()

# --------------------------

from guizero import App, TextBox

def highlight():
    text_box.bg = "lightblue"

def lowlight():
    text_box.bg = "white"

app = App()
text_box = TextBox(app)

# When the mouse enters the TextBox
text_box.when_mouse_enters = highlight
# When the mouse leaves the TextBox
text_box.when_mouse_leaves = lowlight

app.display()

# -------------------

from guizero import App, Box, Text, TextBox
app = App()

title_box = Box(app, width="fill", align="top", border=True)
Text(title_box, text="title")

buttons_box = Box(app, width="fill", align="bottom", border=True)
Text(buttons_box, text="buttons")

options_box = Box(app, height="fill", align="right", border=True)
Text(options_box, text="options")

content_box = Box(app, align="top", width="fill", border=True)
Text(content_box, text="content")

form_box = Box(content_box, layout="grid", width="fill", align="left", border=True)
Text(form_box, grid=[0,0], text="form", align="right")
Text(form_box, grid=[0,1], text="label", align="left")
TextBox(form_box, grid=[1,1], text="data", width="fill")

app.display()

# -----------------


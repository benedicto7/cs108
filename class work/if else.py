user_num = int(input('Enter a number: '))
div_remainder = user_num % 2;
if div_remainder == 0:
    print(user_num, 'is even.')
else:
    print(user_num, 'is odd.')
    
# -----------------------------------------------------

user_age = int(input('Enter your age: '))
if user_age < 16:          # Age 15 and under
   print('Too young.')
   insurance_price = 0
elif user_age < 25:        # Age 16 - 24
   insurance_price = 4800
elif user_age < 40:         # Age 25 - 39
   insurance_price = 2350
else:                      # Age 40 and up
   insurance_price = 2100
print('Annual price: $', insurance_price)

# ---------------------------------------------------------

# First code block has no indentation
model = input('Enter car model: ')
year = int(input('Enter year of car manufacture: '))
antique = False
domestic = False
if year < 1970:
    # New code block has indentation of 4 columns
    antique = True
# Back to code block 0
if model in ['Ford', 'Chevrolet', 'Dodge']:
  # New code block has indentation of 2 columns
  # Any amount of indentation > 0 is OK.
  domestic = True
# Back to code block 0
if antique:
    # New code block has indentation of 4 columns
    if domestic:
        # New block has 4 additional columns (8 total)
        print('My own model-T still runs like a charm...')
        
# ----------------------------------------------------------------

user_age = 26  # Hardcoded for this tool. Could replace with "int(input('Enter age: '))"
# Note that more than one "if" statement can execute
if user_age < 16:
    print('Enjoy your early years.')
   
if user_age > 15:
    print('You are old enough to drive.')

elif user_age > 17:
    print('You are old enough to vote.')

if user_age > 24:
    print('Most car rental companies will rent to you.')
  
elif user_age > 34:
    print('You can run for president.')
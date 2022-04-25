"""CS 108 - Lab 4.1

Wind Chill calculation

@author: Ben Elpidius (bee6)
@author: Andrew Jackson (amj34)
@date: Fall, 2021
"""

temp = float(input('Temperature: '))     #temperature in degrees fahrenheit
windspeed = float(input('Wind speed: '))      #wind speed in miles per hour

# Windchill temp formula
wc_temp = 35.74 + 0.6215*temp - 35.75*windspeed**0.16 + 0.4275*temp*windspeed**0.16

if windspeed < 2 or temp < -58 or temp > 41:
    print('Invalid input')
else:
    print('Wind chill:', wc_temp)     

# Prints how many layers you need for the temp
    if wc_temp < -40:                
        print("Stay home!")
    elif (wc_temp < -10):           
        print("Four layers")
    elif wc_temp < 20:
        print("Three layers")
    elif wc_temp < 40:
        print("Two layers")
    else:
        print("One layer")




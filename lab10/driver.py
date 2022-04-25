"""CS 108 Lab 10.2

This driver uses the Employee class to compute and save corporate statistics.

@author: Ben Elpidius (bee6)
@date: fall, 2021
"""

from employee import Employee

# Construct an employee object for each employee specified in 'employees.txt'
# and add it to the employees list.
# YOUR CODE HERE
employees = []
file = open('employees.txt', 'r')
lines = file.readlines()

for value in lines:
    values = value.split(',')
    employee = Employee(values[0], values[1], values[2], int(values[3]))
    employees.append(employee)

file.close()

# Write the total number of employees into the 'employee-count.txt' file.
# YOUR CODE HERE
new_file = open('employee-count.txt', 'w')
total = len(employees)
new_file.write(str(total))
new_file.close()

# Compute and print out statistics for employees
# YOU WILL REPLACE THIS LINE.

# if the length of the employees list (which is an object) is not 0
if len(employees) == 0:
    print('There are no employees.')

else:
    totals = {}   
    counts = {}
    max_employee = employees[0]                       # sets max as the first index of employee object*
    min_employee = employees[0]                       # sets min as the first index of employee object*
    for employee in employees:
        if employee.rank in totals:                   # takes the rank value of employee from employees
            totals[employee.rank] += employee.salary
            counts[employee.rank] += 1
        else:                                         
            totals[employee.rank] = employee.salary
            counts[employee.rank] = 1
        if employee.salary > max_employee.salary:     # compares the max*
            max_employee = employee
        if employee.salary < min_employee.salary:     # compares the min*
            min_employee = employee


# opens a new file
stat = open('employee-stats.txt', 'w')

# writes the maximum and minimum employee 
stat.write('Maximum and Minimum Salaries\n')  #*
stat.write(str(max_employee) + '\n' + str(min_employee) + '\n')   #*

# writes the average of each rank by looping
stat.write('Rank and Average Salaries\n')
for rank in totals:                                
    stat.write(rank + ': {:.2f}'.format(totals[rank] / counts[rank]) + '\n')

stat.close()
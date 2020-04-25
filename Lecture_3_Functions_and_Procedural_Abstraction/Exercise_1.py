'''
Exercise 1

This program should print out a conversion table of temperatures, after
prompting the user for upper and lower bounds of the table in
Fahrenheit, and the temperature difference between table entries.
This is the same table you have constructed in Lecture 2 but now you will use
functions to divide the code into sub problems

To do:
Add function definitions for the following functions required in the skelleton
code already supplied below:
    print_preliminary_message
    print_message_echoing_input
    print_table

In your code use the functions already defined for you:
    celsius_of
    absolute_value_of
'''

'''
FUNCTION DEFINITIONS
'''
# This function converts fahrenheit to celsius
def celsius_of(fahr):
    return float(5 / 9) * (fahr - 32)

# This function converts fahrenheit to absolute value
def absolute_value_of(fahr):
    return float(5 / 9) * (fahr - 32) + 273.15

# Add function definitions here ...

'''
MAIN PROGRAM
'''
# 1. Print message about what the program does
print_preliminary_message()

# 2. Collect input parameters from the user
lower = input("Please enter the LOWEST Fahrenheit entry in the table")
upper = input("Please enter the HIGHEST Fahrenheit entry in the table")
step = input("Please enter the DIFFERENCE in Fahrenheit between entries")

# 3. Print appropriate message echoing the inputs of the program
print_message_echoing_input(lower, upper, step);

# 4. Print the table (including the column headings):
print_table(lower, upper, step)

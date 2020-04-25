'''
FUNCTION TO CALCULATE AREA
'''
def area(length, width):
    area = length * width
    return area
'''
END OF FUNCTION
'''

'''
MAIN PROGRAM
'''
this_length = input("Enter the length: ")
this_width = input("Enter the width: ")
this_area = area(int(this_length), int(this_width))

print("The area of a " + this_length + "x" + this_width + " rectangle is " + str(this_area))
'''
END OF MAIN PROGRAM
'''

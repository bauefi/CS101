from Area import area

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

year_now = input("Enter the current year then press RETURN.\n")

age_now = input("Enter your current age in years.\n")

another_year = input("Enter the year for which you wish to know your age.\n")

another_age =  int(another_year) - (int(year_now) - int(age_now));

if another_age >= 0:
    print("Your age in " + str(another_year) + ": " + str(another_age))
else:
    print("You weren't even born in " + str(another_year) + "!");

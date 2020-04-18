# 1. Read all inputs
year_now = int(input("Enter the current year then press RETURN.\n"))

month_now = int(input("Enter the current month (a number from 1 to 12).\n"))

age_now = int(input("Enter your current age in years.\n"))

month_born = int(input("Enter the month in which you were born (a number from 1 to 12).\n"))

another_year = int(input("Enter the year for which you wish to know your age.\n"))

another_month = int(input("Enter the month in this year.\n"))

# 2. Calculate the current age in months
age_now_in_months = age_now * 12 + month_now - month_born
if month_now - month_born < 0:
    age_now_in_months += 12

# 3. Calculate how many months into the future
extra_months_from_now = (another_year - year_now) * 12 + another_month - month_now

# 4. Calculate total months
total_months = age_now_in_months + extra_months_from_now

# 5. Express total months in years and months
years  = int(total_months / 12)
months = total_months % 12

# 6. Print the result
# Check if the age is above 150
if total_months >= 150 * 12:
    print("Sorry but you will probably be dead by : " +str(another_month) + " / " + str(another_year))
# Check if the age is negative
elif total_months <= 0:
    print("You weren't even born in " + str(another_month) + " / " + str(another_year));
# The answer is valid
else:
    print("Your age in " + str(another_month) + " / " + str(another_year) + " is", end='')
    if years == 1:
        print(" 1 year", end='')
    if years > 1:
        print(" " + str(years) + " years", end='')
    if months == 1:
        print(" 1 month", end='')
    if months > 1:
        print(" " + str(months) + " months", end='')

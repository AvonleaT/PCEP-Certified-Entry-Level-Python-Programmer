year = int(input("Enter a year: "))

if year < 1582:
    print("This year is not within the Gregorian calendar period.")
elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("The year is a leap year.")
else:
    print("The year is a common year.")
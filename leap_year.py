leap_year = int(input("Enter the year: "))

if leap_year % 4 == 0:
    result = "leap year"
else:
    result = "not a leap year"
print(f"{leap_year} is {result}")

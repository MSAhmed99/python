age = input("Please enter your age: ")
while age == "":
    print("You did not enter your age")
    age = input("Please enter your age: ")

years = 90 - int(age)
weeks = years * 52
days = weeks / 7

print(f"you have {years} years, {weeks} weeks, {days} days left.")
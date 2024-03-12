# Exercises: Level 1
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
age = int(input(("Enter your age: " )))
difference = 18-age
if age >= 18:
    print("You are old enough to learn to drive.")
else:
    print(f"You need {difference} more years to learn to drive.")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = int(input("Enter your age: "))
your_age = int(input("Enter another person's age: "))
difference = my_age - your_age

if my_age > your_age:
    print(f"I am {difference} years older than you.")
elif my_age < your_age:
    print(f"You are {abs(difference)} years older than me.")
else:
    print("We are of the same age.")


# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
number_one = int(input('Enter number one:'))
number_two = int(input('Enter number two:'))

if number_one > number_two:
    print(f"{number_one} is greater than {number_two}")

elif number_one < number_two:
    print(f"{number_one} is lesser than {number_two}")
else:
    print(f"{number_one} is equal {number_two}")


# ### Exercises: Level 2
# Write a code which gives grade to students according to theirs scores:
# 80-100, A
# 70-89, B
# 60-69, C
# 50-59, D
# 0-49, F
    
# Get the student's score
score = int(input("Enter the student's score: "))

# Assign grades based on score ranges
if 80 <= score <= 100:
    grade = 'A'
elif 70 <= score <= 79:
    grade = 'B'
elif 60 <= score <= 69:
    grade = 'C'
elif 50 <= score <= 59:
    grade = 'D'
elif 0 <= score <= 49:
    grade = 'F'
else:
    grade = 'Invalid Score'

print(f"The student's grade is: {grade}")



# Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
# season = ('Autumn', 'Winter', 'Spring', 'Summer')
user_input = input("Enter the season: ")

autumn_months = ['September', 'October', 'November']
winter_months = ['December', 'January', 'February']
spring_months = ['March', 'April', 'May']
summer_months = ['June', 'July', 'August']

if user_input in autumn_months:
    print("The season is Autumn")

elif user_input in winter_months:
    print("The season is Winter")

elif user_input in spring_months:
    print("The season is Spring")

elif user_input in summer_months:
    print("The season is Summer")

else:
    print("Invalid input. Please enter a valid month.")


# The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
user_input = input("Enter the fruit: ")
if user_input in fruits:
    print("The fruit already exist in the list")

else:
    fruits.append(user_input)
    print("Modified list:", fruits)

# Exercises: Level 3
# Here we have a person dictionary. Feel free to modify it!
person = {
        'first_name': 'Asabeneh',
        'last_name': 'Yetayeh',
        'age': 250,
        'country': 'Finland',
        'is_marred': True,
        'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
        'address': {
            'street': 'Space street',
            'zipcode': '02210'
        }
    }
#  * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
user_input = input("Enter the skills: ")

middle = int(len(person) / 2)
print(list[middle])


#  * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
if user_input in person():
        print("skill is present")
    
else:
        print("skill isn't present")
#  * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!

front_end = ['JavaScript', 'React']
back_end = ['Node', 'Python', 'MongoDB']
full_stack = ['React', 'Node', 'MongoDB']

if user_input in front_end:
    print("He is a front end developer")

elif user_input in back_end:
    print("He is a backend developer")

elif user_input in full_stack:
    print("He is a fullstack developer")

else:
    print('unknown title')



#  * If the person is married and if he lives in Finland, print the information in the following format:
#     Asabeneh Yetayeh lives in Finland. He is married.
        
# if (mylist["item1"] == true): 

if (person["is_married"] == True):
    print(" Asabeneh Yetayeh lives in Finland. He is married.")

else:
    print("Asabeneh Yetayeh is not married")
        
# Exercises: Level 1
# Declare a first name variable and assign a value to it
# Declare a last name variable and assign a value to it
# Declare a full name variable and assign a value to it
# Declare a country variable and assign a value to it
# Declare a city variable and assign a value to it
# Declare an age variable and assign a value to it
# Declare a year variable and assign a value to it
# Declare a variable is_married and assign a value to it
# Declare a variable is_true and assign a value to it

first_name = "Shakeel"
last_name = "Ahmed"
country = "India"
city = "Hanamkonda"
age = "18"
year = "2024"
is_married = "False"
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Test', 
    'lastname':'User', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Declare multiple variable on one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)

# Exercises: Level 2
# Check the data type of all your variables using type() built-in function
# Using the len() built-in function, find the length of your first name
print(len(first_name))
# Compare the length of your first name and your last name
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = (num_one + num_two)
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
diff = (num_two - num_one)
print(diff)
# Multiply num_two and num_one and assign the value to a variable product
product = (num_two * num_one)
print(product)
# Divide num_one by num_two and assign the value to a variable division
division = (num_two / num_one)
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = (num_two % num_one)
print(remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = (num_one  ** num_two)
print(exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = (num_one // num_two)
print(floor_division)


# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.
r = 30
pi = 3.14
area = pi * r * r
circumference = 2 * pi * r
print(int(area))
print(int(circumference))

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = int(input("Enter your first name: "))
last_name = int(input("Enter your last name: "))
country = str(input("Enter your country name: "))
age = int(input("Enter your age: "))

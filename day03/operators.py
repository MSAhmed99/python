# # Declare your age as integer variable
age = int(input("Please enter your age: "))
print(age)

# # Declare your height as a float variable
height = float(input("Please enter your age: "))
print(height)

# # Declare a variable that store a complex number
height = complex(input("Please enter your age: "))
print(height)

# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("base: "))
height = int(input("height: "))
area = 0.5 * base * height
print(int(area))

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
perimeter = a + b + c
print(int(perimeter))


# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("length: "))
width = int(input("width: "))
area = length * width
perimeter = 2 * (length + width)
print(int(area))
print(int(perimeter))

# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = int(input("r: "))
area = pi * r * r
circumference = 2 * pi * r
print(int(area))
print(int(circumference))


# Calculate the slope, x-intercept and y-intercept of y = 2x -2
# Given equation: y = 2x - 2
# Coefficients
slope = 2
x_intercept = 0  # For a line in the form y = mx + b, x-intercept is where y = 0
y_intercept = -2  # For a line in the form y = mx + b, y-intercept is the constant term
print(f"Slope: {slope}")
print(f"X-intercept: {x_intercept}")
print(f"Y-intercept: {y_intercept}")

# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# Coordinates of the two points
x1, y1 = 2, 2
x2, y2 = 6, 10

# Calculate the slope (m)
slope = (y2 - y1) / (x2 - x1)

# Calculate the Euclidean distance
distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# Print the results
print(f"Slope (m): {slope}")
print(f"Euclidean Distance: {distance}")

# Compare the slopes in tasks 8 and 9.
# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.



# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
word1 = 'python'
word2 = 'dragon'

length_word1 = len(word1)
length_word2 = len(word2)
print(length_word1)
print(length_word2)

# Falsy comparison statement
if length_word1 != length_word2:
    print(f"The lengths of '{word1}' and '{word2}' are not equal.")
else:
    print(f"The lengths of '{word1}' and '{word2}' are equal.")


# Use and operator to check if 'on' is found in both 'python' and 'dragon'
word1 = 'python'
word2 = 'dragon'

if 'on' in word1 and 'on' in word2:
    print("'on' found in both 'python' and 'dragon'")
else:
    print("'on' not found in both words")


# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'

if 'jargon' in sentence:
    print("jargon is in the sentence")


# There is no 'on' in both dragon and python
word1 = 'python'
word2 = 'dragon'
if 'on' in word1 & word2:
    print("There is 'on' in both dragon and python")

else:
    print("There is no 'on' in both dragon and python")

# Find the length of the text python and convert the value to float and convert it to string
text = "python"
# Find the length of the text
text_length = len(text)
length_as_float = float(text_length)
length_as_string = str(length_as_float)


# Print the results
print(f"Original text: {text}")
print(f"Text length: {text_length}")
print(f"Length as float: {length_as_float}")
print(f"Length as string: {length_as_string}")
    

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")


# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
7 // 3 == int(2.7)
2 == 2

# Check if type of '10' is equal to type of 10
result = type('10') == type(10)
print(result)


# Check if int('9.8') is equal to 10
result = int(round(float('9.8')))
if result == 10:
    print("The rounded integer is equal to 10.")
else:
    print("The rounded integer is not equal to 10.")

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter hours: "))
rate_per_hour = int(input("Enter rate per hour: "))
weekly_earning = hours * rate_per_hour
earning = weekly_earning
print(f"Your weekly earning is {earning}")

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
person_can_live = 100
number_of_years = float(input("Enter number of years you have lived: "))
number_of_seconds = number_of_years * 365.25 * 24 * 60 * 60
print(f"You have lived for {number_of_seconds} seconds.")

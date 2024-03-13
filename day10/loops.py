# Exercises: Level 1
# Iterate 0 to 10 using for loop, do the same using while loop.
for num in range(1, 10):
    print(num)

number = 0
while number <= 10:
    print(number)
    number += 1


# Iterate 10 to 0 using for loop, do the same using while loop.
for num in reversed(range(0, 10)):
    print(num)

num = 10
while num >= 1:
    print(num)
    num -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
#   #
#   ##
#   ###
#   ####
#   #####
#   ######
#   #######

for i in range(1, 8):
    print("#" * i)
    

# Use nested loops to create the following:

# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
# # # # # # # # #
    
for _ in range(8):  # Outer loop for rows
    for _ in range(8):  # Inner loop for columns
        print("# ", end="")
    print()  # Move to the next line after each row


# Print the following pattern:

# 0 x 0 = 0
# 1 x 1 = 1
# 2 x 2 = 4
# 3 x 3 = 9
# 4 x 4 = 16
# 5 x 5 = 25
# 6 x 6 = 36
# 7 x 7 = 49
# 8 x 8 = 64
# 9 x 9 = 81
# 10 x 10 = 100
    
for i in range(11):
    result = i * i
    print(f"{i} x {i} = {result}")
    


# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
programs = ['Python', 'Numpy','Pandas','Django', 'Flask']

for x in range(len(programs)):
    print(programs[x]);


# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0,100):
    if i % 2 != 0:
        print(i,end=",")

for i in range(0,100):
    if i % 2 == 0:
        print(i)


# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0,100):
    if i % 2 != 0:
        print(i,end=",")

for i in range(0,100):
    if i % 2 != 0:
        print(i)

# Exercises: Level 2
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
# The sum of all numbers is 5050.
i = 0 
for num in range(101):
    i += num  
print(i)


# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
# The sum of all evens is 2550. And the sum of all odds is 2500.

# even numbers
i = 0 
for num in range(0, 101):
    if (num % 2 == 0):
        i = i + num
print(i)

# odd numbers
i = 0 
for num in range(0, 101):
    if (num % 2 != 0):
        i = i + num
print(i)


# Exercises: Level 3
# Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
# This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
# Go to the data folder and use the countries_data.py file.
# What are the total number of languages in the data
# Find the ten most spoken languages from the data
# Find the 10 most populated countries in the world
# Check the python version you are using
import sys
print ("python version")
print(sys.version)

print("Version info.")
print(sys.version_info)

# Open the python interactive shell and do the following operations. The operands are 3 and 4.
# addition(+)
print (3 + 4)
# subtraction(-)
print (3 - 4)
# multiplication(*)
print (3 * 4)
# modulus(%)
print (3 % 4)
# division(/)
print (3 / 4)
# exponential(**)
print (3 ** 4)
# floor division operator(//)
print (3 // 4)



# Write strings on the python interactive shell. The strings are the following:
# Your name
print ("Your name")
# Your family name
print ("Your family name")
# Your country
print ("Your country")
# I am enjoying 30 days of python
print(" I am enjoying 30 days of python")



# Check the data types of the following data:
# 10
print (type(10))
# 9.8
print (type(9.8))
# 3.14
print (type(3.14))
# 4 - 4j
print (type(4 - 4j))
# ['Asabeneh', 'Python', 'Finland']
print (type(['Asabeneh', 'Python', 'Finland']))
# Your name
print (type("Your name"))
# Your family name
print (type("Your family name"))
# Your country
print (type("Your country"))




# Exercise: Level 2
# Create a folder named day_1 inside 30DaysOfPython folder. Inside day_1 folder, create a python file helloworld.py and repeat questions 1, 2, 3 and 4. Remember to use print() when you are working on a python file. Navigate to the directory where you have saved your file, and run it.

# Exercise: Level 3
# Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.


# Find an Euclidian distance between (2, 3) and (10, 8)
import math
p1 = [2, 3]
p2 = [10, 8]

distance = math.sqrt(((p1[0]-p2[0]**2) + ((p1[1]-p2[1]**2))))
print(distance)
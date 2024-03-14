# Exercises: Level 1
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add(a, b):
    return a + b

print("Sum of a & b:", add(10, 25))


# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area(pi, r):
    return pi * r * r

print("area of circle: ", area(3.14, 14)) 


# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        else:
            return "All list items should be numbers."
    return total



# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit



# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
autumn_months = ['September', 'October', 'November']
winter_months = ['December', 'January', 'February']
spring_months = ['March', 'April', 'May']
summer_months = ['June', 'July', 'August']

def check_season(month):
    # Convert month to lowercase for case-insensitive matching
    month_lower = month.lower()

    if month_lower in autumn_months:
        return 'Autumn'
    elif month_lower in winter_months:
        return 'Winter'
    elif month_lower in spring_months:
        return 'Spring'
    elif month_lower in summer_months:
        return 'Summer'
    else:
        return 'Invalid Month'


# Write a function called calculate_slope which return the slope of a linear equation

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for item in lst:
        print(item)

my_list = [1, 2, 3, 4, 5]
print_list(my_list)


# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
# print(reverse_list([1, 2, 3, 4, 5]))
# # [5, 4, 3, 2, 1]
# print(reverse_list1(["A", "B", "C"]))
# # ["C", "B", "A"]
def reverse_list(arr):
    reversed_arr = []
    for i in range(len(arr) - 1, -1, -1):
        reversed_arr.append(arr[i])
    return reversed_arr

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list(["A", "B", "C"]))  


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    capitalized_list = [item.capitalize() for item in lst]
    return capitalized_list


my_list = ['apple', 'banana', 'cherry', 'date']
capitalized_result = capitalize_list_items(my_list)
print(capitalized_result)




# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(add_item(food_staff, 'Meat'))     # ['Potato', 'Tomato', 'Mango', 'Milk','Meat'];
# numbers = [2, 3, 7, 9];
# print(add_item(numbers, 5))      [2, 3, 7, 9, 5]
def add_item(lst, item):
    lst.append(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_staff, 'Meat')) 

numbers = [2, 3, 7, 9]
print(add_item(numbers, 5)) 



# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
# food_staff = ['Potato', 'Tomato', 'Mango', 'Milk'];
# print(remove_item(food_staff, 'Mango'))  # ['Potato', 'Tomato', 'Milk'];
# numbers = [2, 3, 7, 9];
# print(remove_item(numbers, 3))  # [2, 7, 9]
def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst

food_staff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_staff, 'Mango')) 

numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  



# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
# print(sum_of_numbers(5))  # 15
# print(sum_all_numbers(10)) # 55
# print(sum_all_numbers(100)) # 5050
def sum_of_numbers(n):
    return sum(range(1, n + 1))

print(sum_of_numbers(5)) 
print(sum_of_numbers(10))  
print(sum_of_numbers(100))  


# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(number):
    sum_odd = 0
    for num in range(1, number + 1):
        if num % 2 != 0:
            sum_odd += num
    return sum_odd

number_input = int(input("Enter a number: "))
result = sum_of_odds(number_input)
print(f"The sum of odd numbers up to {number_input} is {result}.")


# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    sum_even = 0

    for num in range(1, number + 1):
        if num % 2 == 0:
            sum_even += num
    
    return sum_even

number = int(input("Enter a number: "))
result = sum_of_even(number)
print(f"The sum of even numbers up to {number} is: {result}")


# Exercises: Level 2
# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
#     print(evens_and_odds(100))
#     # The number of odds are 50.
#     # The number of evens are 51.

def evens_and_odds(number):
    even_count = 0
    odd_count = 0

    for digit in str(number):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return f"The number of odds are {odd_count}.\nThe number of evens are {even_count}."

print(evens_and_odds(100))



# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(number):
    if number < 0:
        return "Factorial is not defined for negative numbers"
    result = 1
    
    for i in range(1, number + 1):
        result *= i
    return result

number_input = int(input("Enter a number: "))
factorial_result = factorial(number_input)
print(f"The factorial of {number_input} is {factorial_result}.")


# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(param):
    if not param:
        return True
    else:
        return False

value = input("Enter a value: ")
if is_empty(value):
    print("The value is empty.")
else:
    print("The value is not empty.")


# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).


# Exercises: Level 3
# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    return num % 1 == 0



# Write a functions which checks if all items are unique in the list.
def are_all_unique(lst):
    unique_set = set(lst)
    
    return len(unique_set) == len(lst)

my_list = [1, 2, 3, 4, 5]
print(are_all_unique(my_list)) 

my_list = [1, 2, 3, 4, 1]
print(are_all_unique(my_list)) 


# Write a function which checks if all the items of the list are of the same data type.
data_type =  ['Potato', '2', '101.5', 'Milk'];

# Write a function which check if provided variable is a valid python variable
import re

def is_valid_python_variable(variable):
    # Check if the variable name follows Python variable naming rules
    return re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', variable) is not None


# Go to the data folder and access the countries-data.py file.

# Create a function called the most_spoken_languages in the world. It should return 10 or 20 most spoken languages in the world in descending order

# Create a function called the most_populated_countries. It should return 10 or 20 most populated countries in descending order.




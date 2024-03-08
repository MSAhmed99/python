# Exercises: Level 1
# Declare an empty list
empty_list = list()
print(len(empty_list)) 


# Declare a list with more than 5 items
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']  

# Find the length of your list
print('Number of vegetables:', len(vegetables))

# Get the first item, the middle item and the last item of the list
first_vegetables = vegetables[-5]
middle_vegetables = vegetables[-3]
last_vegetables = vegetables[-1]
print(first_vegetables)
print(middle_vegetables)
print(last_vegetables)


# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['name', 'age', 'height', 'marital status', 'address']



# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
for x in range(len(it_companies)):
    print(it_companies[x]);

# Print the number of companies in the list
print(it_companies)
print(len(it_companies))

# Print the first, middle and last company
first = it_companies[-7]
middle = it_companies[-3]
last = it_companies[-1]

# Print the list after modifying one of the companies
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# it_companies.insert(0, 'LWSS')
it_companies.append('LWSS')
print(it_companies)

# Add an IT company to it_companies
it_companies.append('capgemini')

# Insert an IT company in the middle of the companies list
# syntax: 
# lst.insert(index, item) 
it_companies.insert(3, 'DXC')

# Change one of the it_companies names to uppercase (IBM excluded!)

# Join the it_companies with a string '#;  '
result = '#; '.join(it_companies)
print(result)

# Check if a certain company exists in the it_companies list.
user_input = input("Enter the Company name: " ).lower
if user_input in it_companies:
    print("Yes, the company exists")

else:
    print("No, the company doesn't exists")

# Sort the list using sort() method
it_companies.sort()

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)

# Slice out the first 3 companies from the list
slice_first3 = it_companies[0:3]
print(slice_first3)
# Slice out the last 3 companies from the list
slice_last3 = it_companies[-3:]
print(slice_last3)

# Slice out the middle IT company or companies from the list
print(len(it_companies))
it_companies.pop(3)
print(it_companies)

# Remove the first IT company from the list
it_companies.pop(1)

# Remove the middle IT company or companies from the list
it_companies.pop(3)

# Remove the last IT company from the list
it_companies.pop(7)

# Remove all IT companies from the list
del it_companies

# Destroy the IT companies list
it_companies.clear()


# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end + back_end

new_skills = ['python', 'SQL']
front_end.extend(new_skills)
print(front_end)


# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort() 

# Add the min age and the max age again to the list
addition = min(ages) + max(ages)
print(addition)

# Find the median age (one middle item or two middle items divided by two)
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

sorted_ages = sorted(ages)
n = len(sorted_ages)
if n % 2 == 0:
    middle1 = sorted_ages[n // 2 - 1]
    middle2 = sorted_ages[n // 2]
    median = (middle1 + middle2) / 2
else:
    median = sorted_ages[n // 2]

print("The median age is:", median)


# Find the average age (sum of all items divided by their number )
avg = sum(ages) / len(ages)
print (int(avg))

# Find the range of the ages (max minus min)
range = max(ages) - min(ages)


# Compare the value of (min - average) and (max - average), use abs() method
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

average_age = sum(ages) / len(ages)
min_difference = abs(min(ages) - average_age)
max_difference = abs(max(ages) - average_age)

if min_difference > max_difference:
    print("The absolute difference between the minimum age and average age is greater.")
elif max_difference > min_difference:
    print("The absolute difference between the maximum age and average age is greater.")
else:
    print("The absolute differences are equal.")




countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
# Find the middle country(ies) in the countries list
middle_index = len(countries) // 2
middle_countries = countries[middle_index] if len(countries) % 2 != 0 else [countries[middle_index - 1], countries[middle_index]]
# Divide the countries list into two equal lists if it is even if not one more country for the first half.
first_half = countries[:middle_index]
second_half = countries[middle_index:]

# Unpack the first three countries and the rest as scandic countries.
first_country, second_country, third_country, *scandic_countries = countries

print("Middle country(ies):", middle_countries)
print("First half of countries:", first_half)
print("Second half of countries:", second_half)
print("First three countries:", first_country, second_country, third_country)
print("Scandic countries:", scandic_countries)
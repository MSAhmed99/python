# Create an empty dictionary called dog
dog = {}


# Add name, color, breed, legs, age to the dog dictionary
dog = {
    'name': 'tom',
    'color':'golden',
    'breed': 'pamerian',
    'legs':'4',
    'age':'7'
}


# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'm',
    'last_name': 'sa',
    'gender':'M',
    'age':'27',
    'marital status':'un-married',
    'skills': ['python', 'data analysis', 'problem solving'], 
    'country': 'India',
    'city':'HNK',
    'address':'xyz'
}


# Get the length of the student dictionary
print(len(student))


# Get the value of skills and check the data type, it should be a list
skills_data_type = type(student['skills'])
print(f"The data type of 'skills' is: {skills_data_type}")

# Modify the skills values by adding one or two skills
# 'skills': ['python', 'data analysis', 'problem solving'], 


# Get the dictionary keys as a list
keys_list = list(student.keys())
print(keys_list)


# Get the dictionary values as a list
values_list = list(student.values())
print(values_list)


# Change the dictionary to a list of tuples using items() method
student_tuples = list(student.items())
print(student_tuples)


# Delete one of the items in the dictionary
student.pop("age")
print(student)


# Delete one of the dictionaries
student.clear()
print(student)
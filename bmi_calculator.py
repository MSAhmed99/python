height = int(input("Enter your height in cm: "))
weight = int(input("Enter your weight in kg: "))

bmi = weight / (height/100)**2

# Determine the weight category
if bmi < 18.5:
    category = "underweight"
elif bmi < 25:
    category = "normal weight"
elif bmi < 30:
    category = "overweight"
elif bmi < 35:
    category = "obese"
else:
    category = "severely obese"

# Print the BMI and weight category
print(f"Your BMI is {bmi:.2f}, you are {category}.")
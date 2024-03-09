# Exercises: Level 1

# Create an empty tuple
empty_tuple = tuple()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
siblings = ('wa', 'sk','rm', 'ms', 'ma', 'ms', 'ma')

# Join brothers and sisters tuples and assign it to siblings
brothers = ('wa', 'rm', 'ms', 'ma', 'ms')
sisters = ('sk', 'ma')
siblings = brothers + sisters

# How many siblings do you have?
len(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('father_name', 'mother_name')
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings, *parents = family_members

print("Siblings:", siblings)
print("Parents:", parents)


# Create fruits, vegetables and animal_products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('meat products', 'poultry products', 'dairy products', 'non-food products')
food_stuff_tp = fruits + vegetables + animal_products

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle_index = len(food_stuff_lt) // 2
middle_item = food_stuff_lt.pop(middle_index) if len(food_stuff_lt) % 2 != 0 else None

# Slice out the first three items and the last three items from food_staff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# Delete the food_staff_tp tuple completely
del food_stuff_tp

print("Original List:", food_stuff_lt)
print("Middle Item:", middle_item)
print("First Three Items:", first_three_items)
print("Last Three Items:", last_three_items)











# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
# Check if 'Estonia' is a nordic country
if 'Estonia' in nordic_countries:
    print("Estonia is in nordic country")
else:
    print("Estonia is not in nordic country")

# Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print("Iceland is in nordic country")
else:
    print("Iceland is not in nordic country")
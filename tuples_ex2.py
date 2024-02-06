# Create fruits, vegetables, and animal products tuples join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('Strawberry', 'Grapess', 'Watermalon')
vegetables = ('ONion', 'Gobi', 'Potatoes')
animal_products = ('Meat', 'Chicken', 'Eggs')
food_stuff_tp = fruits + vegetables + animal_products

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_lt) // 2
middle_item_tp = food_stuff_tp[middle_index]
middle_items_lt = food_stuff_lt[middle_index-1:middle_index+2]

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items_lt = food_stuff_lt[:3]
last_three_items_lt = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'UK', 'Iceland', 'Switzerland', 'Sweden')

# Check if 'UK' is a nordic country
if 'UK' in nordic_countries:
    print("UK is in the list of nordic country.")
else:
    print("UK is not in the list of nordic country.")

# Check if 'Iceland' is a nordic country
if 'Iceland' in nordic_countries:
    print("Iceland is in the list of nordic country.")
else:
    print("Iceland is not in the list of nordic country.")

# Display results after such operations
print("First Three Items from List:", first_three_items_lt)
print("Last Three Items from List:", last_three_items_lt)
# LEVEL 1

# 1. Create an empty tuple
empty_tuple = ()

# 2. Create a tuple containing names of your sisters and brothers
sisters = ("Vicky", "Mayela")
brothers = ("Kike", "Brandon")

# 3. Join brothers and sisters tuples and assign to siblings
siblings = sisters + brothers
print ("Siblings:", siblings)

# 4. How many siblings do you have?
print ("Number of siblings:", len(siblings))

# 5. Modify siblings tuple and add parents
family_memebers = siblings + ("Father", "Mother")
print ("Family members:", family_memebers)

# LEVEL 2   

# 1. Unpack siblings and parents from family_members
*siblings, father, mother = family_memebers
print("Siblings:", siblings)
print("Parents:", father, mother)

# 2. Create tuples for food categories
fruits = ("Apple", "Banana", "Mango")
vegetables = ("Carrot", "Tomato", "Potato")
others = ("Milk", "Cheese", "Eggs")

# 3. Join the three tuples into food_stuff_tp
food_stuff_tp = fruits + vegetables + others
print("Food tuple:", food_stuff_tp)

# 4. Convert food_stuff_tp tuple to food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print("Food list:", food_stuff_lt)

# 5. Slice out the middle item(s)
n = len(food_stuff_lt)
middle_items = food_stuff_lt[(n-1)//2 : n//2+1]
print("Middle item(s):", middle_items)

# 6. Slice out the first three and last three items
print("First three items:", food_stuff_lt[:3])
print("Last three items:", food_stuff_lt[-3:])

# 7. Delete the food_stuff_tp tuple
del food_stuff_tp

# 8. Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')
print("Is Estonia a Nordic country?", 'Estonia' in nordic_countries)
print("Is Iceland a Nordic country?", 'Iceland' in nordic_countries)
# Create an empty tuple
empty_tuple = ()

# Create a tuple containing names of sisters and brothers
sisters = ('rahini', 'diya')
brothers = ('om', 'kirtan')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
total_siblings = len(siblings)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
father_name = 'Yogeshbhai'
mother_name = 'Jignaben'
family_members = (father_name, mother_name) + siblings

# Display results after such operations
print("Empty Tuple:", empty_tuple)
print("Sisters:", sisters)
print("Brothers:", brothers)
print("Siblings:", siblings)
print("Number of Siblings:", total_siblings)
print("Family Members:", family_members)
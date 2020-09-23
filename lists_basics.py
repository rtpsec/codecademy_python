ints_and_strings = [1, 2, 3, 'four', 'five', 'any']
sam_height=['Sam', 67]

# Add to an empty list

orders = ['daisies', 'periwinkle']
orders.append('tulips')
orders.append('roses')
print(orders)


# Add to the end of the list
langs.insert(0, "PHP")
langs.insert(2, "Lua")

# Multiple Lists in one list
heights = [['Jenny', 61], ['Alexus', 70], ['Sam', 67], ['Grace', 64], ['Vik', 68]]
ages = [['Aaron', 15], ['Dhruti', 16]]

#zip takes two (or more) lists as inputs and returns an object that contains a list of pairs. Each pair contains one element from each of the inputs.
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)

print(names_and_dogs_names)
# output example
# <zip object at 0x7fe996ee7b08>

print(list(names_and_dogs_names))
# Output example
# [('Jenny', 'Elphonse'), ('Alexus', 'Dr. Doggy DDS'), ('Sam', 'Carter'), ('Grace', 'Ralph')]

# Empty list with nothing
my_empty_list = []

# Combining Lists using a + symbol.
items_sold_new = items_sold + ['biscuit', 'tart']
#print(items_sold_new)
# ['cake', 'cookie', 'bread', 'biscuit', 'tart']

# Range sets a range of numbers from 0-##
range(7)

# we call range with two arguments, we can create a list that starts at a different number. 
# For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):
range(2,9)



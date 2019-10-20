print('')
# Create a variable and set it as an List
print('Create a variable and set it as an List')
myList = ["Chandra", 81, "Hythem", 84]
print(myList)

print('')
# Adds an element onto the end of a List
print('Adds an element onto the end of a List')
myList.append("Justin")
print(myList)

print('')
# Returns the index of the first object with a matching value
print('Returns the index of the first object with a matching value')
print(myList.index("Justin"))

print('')
# Changes a specified element within an List at the given index
print('Changes a specified element within an List at the given index')
myList[3] = 85
print(myList)

print('')
# Returns the length of the List
print('Returns the length of the List')
print(len(myList))

print('')
# Removes a specified object from an List
print('Removes a specified object from an List')
myList.remove("Justin")
print(myList)

print('')
# Removes the object at the index specified
print('Removes the object at the index specified')
myList.pop(0)
print(myList)

print('')
# Removes another object at the index specified
print('Removes another object at the index specified')
myList.pop(0)
print(myList)

print('')
# Creates a tuple, a sequence of immutable Python objects that cannot be changed
print('Creates a tuple, a sequence of immutable Python objects that cannot be changed')
myTuple = ('Python', 100, 'VBA', False)
print(myTuple)

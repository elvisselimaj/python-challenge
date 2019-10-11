# Creates a variable with a string "Dartanion"
name = "Dartanion"

# Creates a variable with a string "Data Engineering Manager"
title = "Data Engineering Manager"

# Creates a variable with an integer 15
years = 15

# Creates a variable with the boolean value of True
expert_status = True

# Prints a statement adding the variable
print(name + " is a professional " + title)

# Convert the integer years into a string and prints
print("He has been coding professionally for over " + str(years) + " years")

# Converts a boolean into a string and prints
print("Expert status: " + str(expert_status))

# An f-string accepts all data types without conversion
print(f"Expert status: {expert_status}")

# Another example of using f-strings
print(f"{name} loves working as a {title} and is {years} years in the game")

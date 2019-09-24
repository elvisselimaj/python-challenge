## Basic Variables

# Create two different variables that will take the input of your first name and your neighbor's first name.
my_name = input("What is your name? ")
neighbors_name = input("What is your neighbor's name? ")

# Create two more inputs that will ask how many months each of you has been coding.
my_years_coding = int(input("How long have you been coding? "))
neighbors_years_coding = int(input(f"How long has {neighbors_name} been coding? "))

# Finally, display a result with both your names and the total amount of months coding.
total_years_coding = my_years_coding + neighbors_years_coding
print(f"{my_name} and {neighbors_name} have been coding for {total_years_coding} years!")
## Hello Variable World

# Create two variables called `name` and `country` that will hold strings.
name = 'Dartanion "The Great" Williams'
# name = "Dartanion 'The Great' Williams"
country = 'USA'

# Create two variables called `age` and `hourly_wage` that will hold integers.
age = 36
hourly_wage = 1000

# Create a variable called `satisfied` which will hold a boolean.
satisfied = True

# Create a variable called `daily_wage` that will hold the value of `hourly_wage` multiplied by 8.
daily_wage = hourly_wage * 8

# Use traditional string concatenation to print the `name`, `country`, `age`, and `hourly_wage` variables.
print(name + ' is from ' + country + ' and is ' + str(age) + ' years old. He makes ' + str(hourly_wage) + ' per hour')

# With an `f-string`, print the `daily_wage` and `satisfied` variables.
print(f"{name} makes {daily_wage} per day and is satisfaction rating is: {True}")

## **Hint**
#  For additional help with f-strings, visit [Python 3's f-Strings](https://realpython.com/python-f-strings/).

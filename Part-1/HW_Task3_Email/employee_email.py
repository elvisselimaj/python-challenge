import os
import csv

filepath = os.path.join("Resources", "employees.csv")

new_employee_data = []
# Read data into dictionary and create a new email field

with open(filepath, newline="") as csvfile:
   reader = csv.DictReader(csvfile)
   for row in reader:
       new_employee_data.append(row)
       new_employee_data.append({'email': row['first_name'] + row['last_name'] + "@testmail.com"})
       # Hint: You can use csv.DictReader
       # This will require a little bit of independent research (by design)
       # In the real world, you will encounter situations like this

# Grab the filename from the original path
_,filename = os.path.split(filepath)

# Write updated data to csv file
csvpath = os.path.join("output", filename)
with open(csvpath, "w") as csvfile:
   fieldnames = ["last_name", "first_name", "ssn", "email"]
   writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
   writer.writeheader()
   writer.writerows(new_employee_data)
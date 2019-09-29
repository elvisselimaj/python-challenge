# @TODO: Your code here
my_dict = {
"name":"Dartanion",
"occupation":"Data Engineering Manager",
"age":36,
"hobbies": ["travel", "live music", "coding", "teaching"],
"wake-up": {"Mon": "9 AM", "Tue": "9:30 AM", "Sat": "7 AM"}
}

print(f"Hi! My name is {my_dict['name']}")
print(f"I have {len(my_dict['hobbies'])} hobbies")
print(f"On Saturdays, I wake up at {my_dict['wake-up']['Sat']}")
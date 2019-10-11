# Incorporate the random library
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
if(computer_choice == 'r'):
    if(user_choice == 'r'):
        print("TIE!")
    elif(user_choice == 's'):
        print("YOU LOSE!")
    elif(user_choice == 'p'):
        print("YOU WIN!")
elif(computer_choice == 's'):
    if(user_choice == 's'):
        print("TIE!")
    elif(user_choice == 'p'):
        print("YOU LOSE!")
    elif(user_choice == 'r'):
        print("YOU WIN!")
elif(computer_choice == 'p'):
    if(user_choice == 'p'):
        print("TIE!")
    elif(user_choice == 'r'):
        print("YOU LOSE!")
    elif(user_choice == 's'):
        print("YOU WIN!")

print(f"You chose {user_choice} and the computer chose {computer_choice}")
#Initial variable to track shopping status
shopping = "y"
#House of pies
#establish the pie purchase and pie lists and still shopping variable
pies_purchased = [0,0,0,0,0,0,0,0,0,0]
still_shopping = "y"
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun",
           "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

#print house of pies welcome message and pies available
print("Welcome to the House of Pies! Here are our pies:")

#while still shopping for pies
while shopping == "y":
    print("-----------------------------------------------")
    print("(1) Pecan, (2) Apple Crisp, (3) Bean, (4) Banoffee, (5) Black Bun, (6) Blueberry, (7) Buko, (8) Burek, " +
     " (9) Tamale, (10) Steak ")
    
    # Prompt customer to select a pie
    pie_choice = input("Which kind of pie would you like (select by number reference)? ")

    # Get index of the pie from the selected number
    choice_index = int(pie_choice) - 1

    # Add pie to the pie list by finding the matching index and adding one to its value
    pies_purchased[choice_index] += 1

    print("----------------------------------------------")
    #prompt the user with their choice of pie and let them know its being made
    print("Great! We'll have that " + pie_list[int(pie_choice) - 1] + " right out for you.")
    #Ask the user if they want another pie
    shopping = input("Would you like another pie? Enter (y) for yes and (n) for no. ")
print("-------------------------------------------------")

#list complete order
print("You Purchased:")
#count  instances for each pie list
for pie_index in range(len(pie_list)):
    pie_count = str(pies_purchased[pie_index])
    pie_name = str(pie_list[pie_index])
    print(pie_count + " " + pie_name)
  





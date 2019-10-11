import os
import csv

video = input("Which video are you looking for? ")

csvpath = os.path.join("..","Resources","netflix_ratings.csv")

found = False

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    for row in csvreader:
        
        moviename = row[0]
        rating = row[1]
        user_score = row[5]
        
        if video == moviename:
            print(f"{moviename} is rated {rating} with a user score of {user_score}")
            
            found = True
            
            break
            
    if found is False:
        print(f"{video} was not found.")

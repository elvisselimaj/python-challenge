import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal.csv")

with open(cereal_csv) as csvfile:
    csvreader = csv.reader(csvfile)

    next(csvreader)
    
    for row in csvreader:
#        print(row)
        fiber = float(row[7])     
        
        if(fiber >= 5):
            print(row)
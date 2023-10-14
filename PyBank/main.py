# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #assign the first row as the header of the CSV
    csv_header = next(csvreader)
    print(csv_header)

    # for each row of data after the header
    for row in csvreader:
        
        # assign variables to each of the columns
        date = row[0]
        money = row[1]
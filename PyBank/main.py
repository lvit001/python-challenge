# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(r"C:\Users\loriv\Desktop\Challenge_3\python-challenge\pybank\Resources\budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)

    #assign the first row as the header of the CSV
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        print(row)
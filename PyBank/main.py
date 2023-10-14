# Modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #assign the first row as the header of the CSV
    csv_header = next(csvreader)

    #create lists to contain the data for each column
    date = []
    money = []

    # for each row of data after the header
    for row in csvreader:
        
        # add the data to the lists
        date.append(row[0])
        money.append(int(row[1]))

    # count the number of months
    month_count = len(date)

    # find the net total of the profits/losses column
    net_total = sum(money)

    print(month_count)
    print(net_total)
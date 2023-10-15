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

    # create a new list to hold changes in the money list
    change = [money[row + 1] - money[row] for row in range(len(money)-1)]

    # count the number of months
    month_count = len(date)

    # find the net total of the profits/losses column
    net_total = sum(money)

    # find the sum and length of the change list to calculate average change
    total_change = sum(change)
    length_change = len(change)
    average_change = round(total_change/length_change, 2) #use the round function to round the average to 2 decimal points

    print(f"Total Months: {month_count}")
    print(f"Total: ${net_total}")
    print(f"Average Change: ${average_change}")
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

    #find the max change in the change list
    max_change = max(change)

    #find the index for the max change and then use that index to find the coresponding month for the change
    max_index = change.index(max_change) + 1 #need to add 1 to this value since the change list has one less value than the date list
    max_month = date[max_index]

    #find the min change in the change list
    min_change = min(change)

    #find the index for the min change and then use that index to find the coresponding month for the change
    min_index = change.index(min_change) + 1 #need to add 1 to this value since the change list has one less value than the date list
    min_month = date[min_index]

#print out the analysis in the terminal
print(f"Total Months: {month_count}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {max_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_change})")

#set variable for output file
output_file = os.path.join("analysis", "analysis.txt")

#open the output txt file to write in it
f = open(output_file,'w')

#write the analysis data into the txt file
f.write('Financial Analysis' + '\n')
f.write('-------------------------------------' + '\n')
f.write('Total Months: ' + str(month_count) + '\n')
f.write('Total: $' + str(net_total) + '\n')
f.write('Average Change: $' + str(average_change) + '\n')
f.write('Greatest Increase in Profits: ' + str(max_month) + ' ' + '(' + '$' + str(max_change) + ')' + '\n')
f.write('Greatest Increase in Profits: ' + str(min_month) + ' ' + '(' + '$' + str(min_change) +')')

#close the txt file
f.close()
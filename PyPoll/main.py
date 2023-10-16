# import modules
import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #assign the first row as the header of the CSV
    csv_header = next(csvreader)

    #create lists to contain variables
    voter_id = []
    county = []
    candidate = []

    # create a for statement to go through the rows in the data after the header
    for row in csvreader:
        
        #add the data from the csv to the lists created above
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

    #count the total number of votes using the length function on the voter_id list
    total_votes = len(voter_id)
    print(total_votes)
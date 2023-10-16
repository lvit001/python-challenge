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

    #create lists to contain variables for voter_id and candidates
    voter_id = []
    candidate = []

    # create a for statement to go through the rows in the data after the header
    for row in csvreader:
        
        #add the data from the csv to the lists created above
        voter_id.append(row[0])
        candidate.append(row[2])

    #count the total number of votes using the length function on the voter_id list
    total_votes = len(voter_id)

    # create a list for each candidate
    Charles = []
    Diana = []
    Raymon = []

    #create a for loop and if/elif statements to look through the candidate list and pull out votes for Charles, Diana, and Raymon
    for row in candidate:
        
        if row == "Charles Casper Stockham":
            Charles.append(row)
        
        elif row == "Diana DeGette":
            Diana.append(row)
        
        elif row == "Raymon Anthony Doane":
            Raymon.append(row)


    #count the number of votes for each candidate using a length function on their lists
    Charles_votes = len(Charles)
    Diana_votes = len(Diana)
    Raymon_votes = len(Raymon)

    #calculate the percentage of votes for Charles
    Charles_percent = round(Charles_votes/total_votes * 100, 3)

    #calculate the percentage of votes for Diana
    Diana_percent = round(Diana_votes/total_votes * 100, 3)

    #calculate the percentage of votes for Raymon
    Raymon_percent = round(Raymon_votes/total_votes * 100, 3)

    #create if, elif, and else statements to determine the winner

    #if Charles has more votes than Diana and Raymon, Charles is the winner
    if Charles_votes > Diana_votes and Charles_votes > Raymon_votes:
        Winner = "Charles Casper Stockham"
    
    # if Diana has more votes than Charles and Raymon, Diana is the winner
    elif Diana_votes > Charles_votes and Diana_votes > Raymon_votes:
        Winner = "Diana DeGette"
    
    #if both of the above are not true, Raymon is the winner
    else:
        Winner = "Raymon Anthony Doane"

# printing the required analysis to the terminal
print("Election Results")
print("--------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
print(f"Charles Casper Stockham: {Charles_percent}% ({Charles_votes})")
print(f"Diana DeGette: {Diana_percent}% ({Diana_votes})")
print(f"Raymon Anthony Doane: {Raymon_percent}% ({Raymon_votes})")
print("--------------------")
print(f"Winner: {Winner}")
print("--------------------")

#set variable for output txt file
output_file = os.path.join("analysis", "analysis.txt")

#open the output txt file to write in it
f = open(output_file,'w')

#write the analysis data into the txt file
f.write('Election Results' + '\n')
f.write('-------------------------' + '\n')
f.write('Total Votes: ' + str(total_votes) + '\n')
f.write('-------------------------' + '\n')
f.write('Charles Casper Stockham: ' + str(Charles_percent) + '%' + ' ' + '(' + str(Charles_votes) + ")" + '\n')
f.write('Diana DeGette: ' + str(Diana_percent) + '%' + ' ' + '(' + str(Diana_votes) + ")" + '\n')
f.write('Raymon Anthony Doanne: ' + str(Raymon_percent) + '%' + ' ' + '(' + str(Raymon_votes) + ")" + '\n')
f.write('-------------------------' + '\n')
f.write('Winner: ' + str(Winner) + '\n')
f.write('-------------------------')

#close the txt file
f.close()
# python-challenge
Module 3 Challenge for Bootcamp

PyBank Code Explained:
* for lines 1-13, I used code from lectures on how to read a CSV file into python
* for lines 15-17, I created empty lists that would eventually contain the data from the CSV file
* for lines 19-24, I created a for loop that would cycle through the rows in the CSV file and add the data to the respective date and money lists
* for lines 26-27: Code to find the changes in the profits/losses column was found here: https://www.geeksforgeeks.org/python-generate-successive-element-difference-list/# and was changed to work for this data set. I made a change list that would contain the differences between cells in the money list to eventually find the average, max, and mean
* for lines 29-30: to find the total number of months, I used the length function to calculate the length of the date list, which contained all of the months
* for lines 32-33: to find the sum of the profits/losses, I used the sum function to add all of the values contained in the money list
* for lines 35-38, I was trying to calculate the average change, so I used the sum function to find the total change value and the length function to find the total number of changes. Then, I divided the total_change value by the length_change value and put this in a round function to round to the second decimal point.
* for lines 40-45: I was trying to find the max change and the corresponding month for the start of the change. To do so, I first used the max function on the change list to find the max change. Then, I found the index of the max value in the change list and added 1 since the change list in 1 shorter than the date list. I then looked for the max_index in the data list to find the corresponding month for the change.
* for lines 47-52, I did the same code as above but instead was looking for the min value instead of the max value. So, I used the min function in place of the max function
* for lines 54-61: I printed out the required analysis to the terminal
* for lines 63-64: I used code we learned in class to create an analysis.txt file in the analysis folder. I also used help from this video for specifically writing in a txt file as we were more focused on writing into csv files in class: https://www.youtube.com/watch?v=walXPsausPI
* for lines 66-67: I opened the analysis.txt file that I created and used 'w' to write in it. I called this variable 'f' for easy callback in further code.
* for lines 69-76: I created the required financial analysis lines in the analysis.txt file. I learned how to go to the next line using '\n' here: https://stackoverflow.com/questions/2918362/writing-string-to-a-file-on-a-new-line-every-time
* for lines 78-79: I used f.close() to close the txt file as suggested in the youtube video referenced in line 15 of this readme file

PyPoll:
*

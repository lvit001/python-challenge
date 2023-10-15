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

PyPoll:
*

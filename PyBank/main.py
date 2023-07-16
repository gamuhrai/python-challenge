# This will allow us to create file path across operating systems
import os

#Module for reading CSV files
import csv

import statistics

csvpath=os.path.join('Resources', 'budget_data.csv')

with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip head row
    header = next(csvreader)

#initialize variables to zero and create a list
    total_months = 0
    total_pnl = 0
    pnl = []
    pnl2 = []
#for loop to read each row of the csv file in csvreader
    for row in csvreader:
        #since unique months don't matter, 
        # total_months counts 1 for each line in csvreader
        total_months += 1
        #pnl_value holds current row's profit/loss value  
        pnl_value = int(row[1])
        #total_pnl holds integer sum total pf all profit/loss
        total_pnl += pnl_value
        #adding date and pnl value to each list element 
        #each list element has indices 0 = date and 1 = pnl value
        pnl.append((row[0], pnl_value))
        pnl2.append(pnl_value)

#determine max and min value by looking at the second index of each list element
    max_value = max(pnl, key=lambda x: x[1])
    min_value = min(pnl, key=lambda x: x[1])
#mades a second list pnl2 to hold only int value to pass it through statistics method
    avgchange = int(statistics.mean(pnl2))

  #print desired values
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_pnl}")
    print(f"Average Change: ${avgchange}")
    print(f"Greatest Increase in Profits: {max_value[0]} (${max_value[1]})")
    print(f"Greatest Decrease in Profits: {min_value[0]} (${min_value[1]})")
    

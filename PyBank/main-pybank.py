# This will allow us to create file path across operating systems
import os

#Module for reading CSV files
import csv
#module to use the statistics method
import statistics

csvpath=os.path.join('Resources', 'budget_data.csv')

output_path = os.path.join('analysis', 'financial_analysis.txt')


with open(csvpath, encoding='utf') as csvfile, open(output_path, 'w') as output_file:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip head row
    header = next(csvreader)

#initialize variables to zero and create a list
    total_months = 0
    total_pnl = 0
    pnl = []
    pnl2 = []
    previous_pnl = None
    mchange = []
#for loop to read each row of the csv file in csvreader
    for row in csvreader:
        #since unique months don't matter, 
        # total_months counts 1 for each line in csvreader
        total_months += 1
        #pnl_value holds current row's profit/loss value  
        pnl_value = int(row[1])
        #total_pnl holds integer sum total pf all profit/loss
        total_pnl += pnl_value

        #calculate pnl month changes
        if previous_pnl is not None:
            pnl_change = pnl_value - previous_pnl 


        #adding date and pnl value to each list element 
        #each list element has indices 0 = date and 1 = pnl value
            pnl.append((row[0], pnl_change))
            pnl2.append(pnl_change)
            

        #update previous pnl with current pnl_value for the next iteration
        previous_pnl = pnl_value
    

#determine max and min value by looking at the second index of each list element
    max_value = max(pnl, key=lambda x: x[1])
    min_value = min(pnl, key=lambda x: x[1])
#mades a second list pnl2 to hold only int value to pass it through statistics method
    avgchange = round((statistics.mean(pnl2)),2)

  #print to terminal
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_pnl}")
    print(f"Average Change: ${avgchange}")
    print(f"Greatest Increase in Profits: {max_value[0]} (${max_value[1]})")
    print(f"Greatest Decrease in Profits: {min_value[0]} (${min_value[1]})")
  
  #print output to file
    print("Financial Analysis", file=output_file)
    print("----------------------------", file=output_file)
    print(f"Total Months: {total_months}", file=output_file)
    print(f"Total: ${total_pnl}", file=output_file)
    print(f"Average Change: ${avgchange}", file=output_file)
    print(f"Greatest Increase in Profits: {max_value[0]} (${max_value[1]})", file=output_file)
    print(f"Greatest Decrease in Profits: {min_value[0]} (${min_value[1]})", file=output_file)
    

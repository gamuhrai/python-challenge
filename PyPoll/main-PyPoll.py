#This will allow us to create file path across operating systems
import os
#module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('analysis', 'Election_Results.txt')

with open(csvpath, encoding='utf') as csvfile, open(output_path, 'w') as output_file:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)

#initialize variables to zero
    total_votes = 0
    votes_ccs = 0
    votes_dd = 0
    votes_rad = 0
# loop through rows and count up votes for each candidates
    for row in csvreader:
        total_votes += 1

        if row[2] == "Charles Casper Stockham":
            votes_ccs += 1
        elif row[2] == "Diana DeGette":
            votes_dd += 1
        elif row[2] == "Raymon Anthony Doane":
            votes_rad += 1

    # Calculate the percentage of votes for each candidate
    percent_ccs = (votes_ccs / total_votes) * 100
    percent_dd = (votes_dd / total_votes) * 100
    percent_rad = (votes_rad / total_votes) * 100

    # Find the winner based on the maximum votes
    #dictionary of candidate_votes stores vote count 
    # for each candidate with the key being the candidate name
    candidate_votes = {"Charles Casper Stockham": votes_ccs, "Diana DeGette": votes_dd, "Raymon Anthony Doane": votes_rad}
    winner = max(candidate_votes, key=candidate_votes.get)

    # Print to terminal
    print("Election Results")
    print("----------------------------")
    print(f"Total Votes: {total_votes}")
    print("----------------------------")
    print(f"Charles Casper Stockham: {percent_ccs:.3f}% ({votes_ccs})")
    print(f"Diana DeGette: {percent_dd:.3f}% ({votes_dd})")
    print(f"Raymon Anthony Doane: {percent_rad:.3f}% ({votes_rad})")
    print("----------------------------")
    print(f"Winner: {winner}") 
    print("----------------------------")

    # Print output to file
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Charles Casper Stockham: {percent_ccs:.3f}% ({votes_ccs})\n")
    output_file.write(f"Diana DeGette: {percent_dd:.3f}% ({votes_dd})\n")
    output_file.write(f"Raymon Anthony Doane: {percent_rad:.3f}% ({votes_rad})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("----------------------------\n")
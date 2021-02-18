import os
import csv

election_data_csv = os.path.join('./Resources/election_data.csv')

#create variables and empty lists
total_votes = 0
candidates = []
votes = []
vote_percentage = []

#open file with CSV reader
with open(election_data_csv,newline='') as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    header = next(csvreader)
    for row in csvreader:
       
        #find total number of votes
        total_votes = total_votes + 1
      
        #Add candidate to the candidate list and their first vote
        if str(row[2]) not in candidates:
            candidates.append(row[2])
            candidate_index = candidates.index(row[2])
            votes.append(1)
        #Add a vote to an existing candidate in the candidate list
        else:
            candidate_index = candidates.index(row[2])
            votes[candidate_index] += 1
        
    #finding percentage of votes    
    for vote in votes:
        percentage = (vote/total_votes) * 100
        vote_percentage.append(percentage)
            
#finding the winner
winner = max(votes)
winner_index = votes.index(winner)
winning_candidate = candidates[winner_index]

#print results
print("Election Results")
print("---------------------------------------")
print(f"Total Votes: {int(total_votes)}")
print("---------------------------------------")
#use a loop to iterate through the lists and associated values
for a in range(len(candidates)):
    print(f"{candidates[a]}: {vote_percentage[a]:.3f}% ({votes[a]})")
print("---------------------------------------")
print(f"Winner: {winning_candidate}")
print("---------------------------------------")

output_path = os.path.join('./Analysis', "analysis.txt")
with open(output_path, 'w') as txt_file:
    
    txt_file.write("Election Results\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Total Votes: {int(total_votes)}\n")
    txt_file.write("---------------------------------------\n")
    for a in range(len(candidates)):
        txt_file.write(f"{candidates[a]}: {vote_percentage[a]:.3f}% ({votes[a]})\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("---------------------------------------\n")
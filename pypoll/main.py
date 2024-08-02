import os
import csv

#path the csv file
# election_data = os.path.join("C:/Users/Yiling C/Desktop/Data Analysis/python_challegen/Starter_Code/PyPoll/Resources/election_data.csv")
election_data = os.path.join("Resources","election_data.csv")

#list of variables:
total_Votes = 0 
vote_candidate = {}

# open the csv file:
with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        total_Votes += 1
        if row[2] not in vote_candidate:
            vote_candidate[row[2]] = 1
        else:
            vote_candidate[row[2]] += 1   
        
 #get the results       

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_Votes))
print("-------------------------")

for candidate, votes in vote_candidate.items():
    print(candidate + ": " + "{:.3%}".format(votes/total_Votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 

winner = max(vote_candidate, key=vote_candidate.get)

print(f"Winner: {winner}")

# now write this to an output file

f = open("election_results.txt", "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(total_Votes))
f.write('\n')
f.write("-------------------------")
f.write('\n')

for candidate, votes in vote_candidate.items():
    f.write(candidate + ": " + "{:.3%}".format(votes/total_Votes) + "   (" +  str(votes) + ")")
    f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')



  
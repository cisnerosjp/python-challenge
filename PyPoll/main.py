#PyPoll main.py
#import data and dependencies
from pathlib import Path
import csv
import operator

#importing election data
election_data = Path("Resources/election_data.csv")

#counter for the total number of votes
totalVotes = 0
#information for the candidates
candidateInfo = {}
#candidates votes and percentage

#opening the election data
with open(election_data, encoding="UTF-8") as csvfile:
    elections = csv.reader(csvfile, delimiter=",")
    #this skips the first line in the csv document because it's not relevant
    header = next(elections)
    #reads through the rows in the document
    for row in elections:
        #add to the counter for votes
        totalVotes += 1
        #get candidate informations and add to their counter and add the candidate
        candidate = row[2]
        if candidate in candidateInfo.keys():
            candidateInfo[candidate] += 1
        else:
            candidateInfo[candidate] = 1






print(totalVotes)
print(candidateInfo)

#candidate with most votes

winner = max(candidateInfo, key=candidateInfo.get)

#this section prints off the election results
print("Election Results\n")
print("-------------------------\n")
print("Total Votes: ", totalVotes, "\n")
print("-------------------------\n")
#percentage of votes each candidate won
#the total number of votes each candidate won
# the winner of the election based on popular vote
print("-------------------------\n")
#the winner
print(f"Winner: {winner}","\n")
print("-------------------------\n") 
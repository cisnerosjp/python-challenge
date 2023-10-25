#PyPoll main.py
#import data and dependencies
from pathlib import Path
import csv

#importing election data
election_data = Path("Resources/election_data.csv")

#counter for the total number of votes
totalVotes = 0
#information for the candidates
candidateInfo = {}

#opening the election data
with open(election_data, encoding="UTF-8") as csvfile:
    elections = csv.reader(csvfile, delimiter=",")
    #this skips the first line in the csv document because it's not relevant
    header = next(elections)
    #reads through the rows in the document
    for row in elections:
        #add to the counter for votes
        totalVotes += 1
        
print(totalVotes)


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
print("Winner:","\n")
print("-------------------------\n")
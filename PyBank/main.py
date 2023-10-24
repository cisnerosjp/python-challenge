#Pybank main.py
#import data and dependencies
from pathlib import Path
import csv

budget_data = Path("Resources/budget_data.csv")

#read in the months and totals from each row in the csv file

#counter for the number of months
monthCount = 0
#counter for the grand total
profLossCount = 0
with open(budget_data) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    #this next line skips the first line in the csv file since it is not relevant
    header=next(budget_reader) 
    for row in budget_reader:
        date = row[0]
        profitLoss = int(row[1])
        #adds to the counters declared earlier
        monthCount += 1
        profLossCount += profitLoss


#this section prints off the final financial analysis
print("Financial Analysis\n")
print("------------------------------\n")

print("Total Months: " , monthCount,"\n")
print("Total: ", profLossCount,"\n")




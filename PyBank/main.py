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
#holder for greatest increase in profits
greatestIncrease = 0
#holder for greatest decrease in profits
greatestDecrease = 0

with open(budget_data) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    #this next line skips the first line in the csv file since it is not relevant
    header=next(budget_reader) 
    #reads through the rows in the document
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
print("Average Change:","\n")
print("Greatest Increase in Profits:","\n")
print("Greatest Decrease in Profits:","\n")


#write it to a new text file. If you want to rewrite the document, you have to append by
#swapping the "x" for an "a" otherwise this will throw an error after initial run
f = open("PyBank_Results.txt","x")
f.write("Financial Analysis\n")
f.write("------------------------------\n")
f.write(f"Total Months: {monthCount}")
f.write("\n")
f.write(f"Total: {profLossCount}")
f.write("\n")
f.write("Average Change: \n")
f.write("Greatest Increase in Profits: \n")
f.write("Greatest Decrease in Profits: \n")
f.close()
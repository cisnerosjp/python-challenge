#Pybank main.py
#import data and dependencies
from pathlib import Path
import csv

budget_data = Path("Resources/budget_data.csv")

monthCount = 0
profLossCount = 0
with open(budget_data) as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=',')
    header=next(budget_reader) 
    for row in budget_reader:
        date = row[0]
        profitLoss = int(row[1])
        monthCount += 1
        profLossCount += profitLoss

print(monthCount)
print(profLossCount)




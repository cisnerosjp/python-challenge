#PyPoll main.py
#import data and dependencies
from pathlib import Path
import csv

election_data = Path("Resources/election_data.csv")

with open(election_data, encoding="UTF-8") as csvfile:
    elections = csv.reader(csvfile, delimiter=",")

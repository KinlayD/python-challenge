# dependencies
import os
import csv

# output path
output_path = os.path.join("Resources", "budget_data.csv")

with open(output_path) as x:
    budget_data = csv.DictReader(x, delimiter = ',')

    for row in budget_data:
        print(row['Date'], row['Profit/Losses'])
    




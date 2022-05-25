# dependencies
import os
import csv

# output path
output_path = os.path.join("Resources", "budget_data.csv")

with open(output_path) as x:
    budget_data = csv.DictReader(x, delimiter = ',')
    profit_loss = []
    for row_count, row in enumerate(budget_data):
        value = int(row['Profit/Losses'])
        profit_loss.append(value)

print(f'Total Months: {row_count}')
print(f'Net Total: {sum(profit_loss)}')
print(f'Average Change in Profit: {sum(profit_loss)/row_count}')







        






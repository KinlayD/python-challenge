# dependencies
import os
import csv

# file path
input_file = os.path.join("Resources", "budget_data.csv")

# initialize variables: total number of months and total profit/loss
total_months = 0
total_net = 0

# intitialize list to store months and change in profit/loss
list_month_change = []
list_change = []


# Read csv file
with open(input_file) as file:
    reader = csv.reader(file)

    headers = next(reader)

    # pass first row of budget data
    first_row = next(reader)
    total_months = total_months + 1
    total_net = total_net + int(first_row[1])
    previous_net = int(first_row[1])
    
    # For loop
    for row in reader:

        total_months = total_months + 1
        total_net = total_net + int(row[1])

        net_change = int(row[1]) - previous_net 
        previous_net = int(row[1])
        list_change = list_change + [net_change]
        list_month_change = list_month_change + [row[0]]
        
        # Find max increase and max decrease in profit by month
        max_increase = max(list_change)
        max_increase_index = list_change.index(max_increase)
        
        max_decrease = min(list_change)
        max_decrease_index = list_change.index(max_decrease)

    # Find average net change
    net_month_average = round(sum(list_change) / len(list_change), 2)
           


    print("Financial Analysis")
    print("------------------------------------")
    print(f'Total Months: {total_months}')
    print(f'Average Change: ${net_month_average}')    
    print(f'Greatest Increase in Profits: {list_month_change[max_increase_index]} (${max_increase})')
    print(f'Greatest Decrease in Profits: {list_month_change[max_decrease_index]} (${max_decrease})')


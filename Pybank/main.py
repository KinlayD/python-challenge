# dependencies
import csv

# initialise variables to count the total number of months and net profit/loss
total_months = 0
total_net = 0

# initialise variables to store months and change in profit/loss
months = []
change = []

# initialise variables to store greatest increase/greatest decrease in profit/loss
change_profit_loss_dict = {}

# open the file and read
filepath = "../Resources/budget_data.csv"
with open(filepath) as file:
    reader = csv.reader(file)

# skip header 
    # header stores the first row of the reader and then instructs the reader to return the next row
    # header = ['Date', 'Profit/Losses']
    header = next(reader)

# store first row
    # first_row stores the current (non_header) row of the reader and then instructs the reader to return the next row
    # first row = ['Jan-2010', '867884']
    first_row = next(reader)

# count the first row and store to total_months
    # total months = 0 + 1
    total_months = total_months + 1

# include the first row value from index = 1 (profit/losses) to the total_net
    # total_net = 0 + 867884
    total_net = total_net + int(first_row[1])

# create a variable that is assigned for holding one of the two values in the profit/loss column that will be used to find the difference between
# profit/loss in the current month and profit/loss in the previous month.
# x1 will hold the value for the previous month.
# x2 will hold the net difference between the current months profit/loss and the previous months profit/loss  
    # x1 = 867884
    x1 = int(first_row[1])

# use a for loop to iterate through rows in reader
    # 0th iteration:
        # x2 = 984655 - 867884 = 116771
        # x1 = 984655
        # change = [116771]
    # 1st iteration:
        # x2 = 322013 - 984655 = -662642
        # x1 = 322013
        # change = [116771, -662642]
    # 2nd iteration:
        # # x2 = -69417 - 322013 = -391430
        # x1 = -69417
        # change = [116771, -662642, -391430]
    # ...
    # until the nth iteration
    for row in reader:
        total_months = total_months + 1
        total_net = total_net + int(row[1])

        x2 = int(row[1]) - x1
        x1 = int(row[1])
        
        change.append(x2)
        months.append(row[0])

# find the greatest increase in profit:
    max_increase_value = max(change)
    max_increase_index = change.index(max_increase_value)
    month_max_increase = months[max_increase_index]

# find the greatest decrease in profit:
    max_decrease_value = min(change)
    max_decrease_index = change.index(max_decrease_value)
    month_max_decrease = months[max_decrease_index]

# calculate the average of the changes in profit/losses over the period
    avg_change = round(sum(change)/len(change), 2)


    print('-----------------')
    print('total months:')
    print(total_months)
    print('-----------------')
    print('net total:')
    print(total_net)
    print('-----------------')
    print('average change:')
    print(avg_change)
    print('-----------------')
    print('greatest increase in profit:')
    print(month_max_increase)
    print(max_increase_value)
    print('-----------------')
    print('greatest decrease in profit')
    print(month_max_decrease)
    print(max_decrease_value)

# export as .txt 
with open("PyBank_Analysis.txt", "w") as PyBank_Analysis:
    PyBank_Analysis.writelines("Financial Analysis\n")
    PyBank_Analysis.writelines("------------------------\n")
    PyBank_Analysis.writelines(f"Total Months: {total_months}\n")
    PyBank_Analysis.writelines(f"Total: ${total_net}\n")
    PyBank_Analysis.writelines(f"Average Change: ${avg_change}\n")
    PyBank_Analysis.writelines(f"Greatest Increase in Profits: {month_max_increase} (${max_increase_value})\n")
    PyBank_Analysis.writelines(f"Greatest Decrease in Profits: {month_max_decrease} (${max_decrease_value})\n")

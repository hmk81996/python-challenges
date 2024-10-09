# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output
file_to_load = os.path.join("PyBank", "Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("PyBank", "analysis", "analysis_output.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
month_to_month = []
net_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
        
    # Track the total and net change
    profit_loss = int(first_row[1])
    total_net += profit_loss
    total_months += 1
    previous_net = profit_loss

    # Process each row of data
    for row in reader:

        # Track the total
        profit_loss = int(row[1])
        total_net += profit_loss

        #calculate total months
        total_months += 1

        # Track the net change: get profit/loss value
        value = int(row[1])
    
        #caluculate net change
        net_change = profit_loss - previous_net
        previous_net = value

        # # Calculate the greatest increase in profits (month and amount)
        month_to_month += [row[0]]
        net_change_list += [net_change]
            
        #check for greatest increase
        if net_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = net_change
            
        # # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = net_change

# Calculate the average net change across the months
avg_net_change = (sum(net_change_list))/(len(net_change_list))

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${avg_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output 
print(output)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
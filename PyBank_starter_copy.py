# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("..", "analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0

# Add more variables to track other necessary financial data
initial_value = None
final_value = None
previous_profit = None
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)

    # Track the total and net change (make a list?)
    #total_net

    # Process each row of data
    for row in reader:

        # Track the total
        month = row["Date"]
        total_months[int(month)] += 1

        # Track the net change
        profit_loss = row["Profit/Losses"]
        total_net += float(profit_loss)

        net_change =  float(row["Profits/Losses"])

        if initial_value is None:
            initial_value = value
        
        final_value = value

        net_change = final_value - initial_value

        # Calculate the greatest increase in profits (month and amount)
        month = row[0]
        profit = int(row[1])

        if previous_profit is not None:
            change = profit - previous_profit

            #check for greatest increase
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = month
            
            previous_profit = profit

        # Calculate the greatest decrease in losses (month and amount)
        if previous_profit is not None:
            change = profit - previous_profit

            #check for greatest decrease
            if change > greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = month




# Calculate the average net change across the months
def avg(net_change):
    return net_change / total_months

avg(net_change)

# Generate the output summary
# total_months = 
# total_net = 
# changes = 
# greatest_increase = 
# greatest_decrease = 

# Print the output (Do I need an outpout variable?)
#output = 
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: + {total_months}")
print(f"Total: + $ + (total_net)")
print(f"Average Change: + int(avg(net_change))")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits:")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
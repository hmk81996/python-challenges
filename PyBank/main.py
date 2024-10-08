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

#variables to track net change
initial_value = None
final_value = None
# previous_profit = 

#variables used to track greatest increase and decrease
# greatest_increase = 0
# greatest_increase_month = ""
# greatest_decrease = 0
# greatest_decrease_month = ""


# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row (what's the difference from extracting first row?)
    header = next(reader)

    # QUESTION Extract first row to avoid appending to net_change_list (but then my total is off)
    # first_row = next(reader)

    # QUESTION Track the total and net change
        
    # Process each row of data
    for row in reader:

        # Track the total
        transaction = int(row[1])
        total_net += transaction

        #calculate total months
        if row[0]:  
            total_months += 1

        # Track the net change
        #get profit/loss value
        value = int(row[1])

        #set initial value      
        if initial_value is None:
            initial_value = value

        #update the final value with current value
        final_value = value

        #caluculate net change
        # if initial_value is not None and final_value is not None:
        net_change = final_value - initial_value

        # # Calculate the greatest increase in profits (month and amount)
        # month = row[0]
        # profit = int(row[1])

        # if previous_profit is not None:
        #     change = profit - previous_profit

        #     #check for greatest increase
        #     if change > greatest_increase:
        #         greatest_increase = change
        #         greatest_increase_month = month
            
        #     previous_profit = profit

        # # Calculate the greatest decrease in losses (month and amount)
        # if previous_profit is not None:
        #     change = profit - previous_profit

        #     #check for greatest decrease
        #     if change > greatest_decrease:
        #         greatest_decrease = change
        #         greatest_decrease_month = month




# Calculate the average net change across the months
# print(f"$" + str(net_change))

avg_net_change = float(net_change/total_months)


# Generate the output summary
total_months
total_net
avg_net_change
# greatest_increase = 
# greatest_decrease = 

# Print the output 

print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")
print(f"Total:"+ "$" + str(total_net) )
print(f"Average Change:" + "$" + str(avg_net_change))
# print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
# print(f"Greatest Decrease in Profits:")

# Write the results to a text file
# with open(file_to_output, "w") as txt_file:
#     txt_file.write(output)
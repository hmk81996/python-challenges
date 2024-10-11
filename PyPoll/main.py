# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("Analysis", "analysis_output.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

#Define lists and dictionaries to track candidate names and vote counts
candidate_dict = {}
vote_percentages = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="",)

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        key = row[2]
        
        # If the candidate is not already in the candidate list, add them
        if key not in candidate_dict:
            candidate_dict[key] = 0

        # Add a vote to the candidate's count
        candidate_dict[key] += 1 
                        
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    total_vote_count = (
        f"\nElection Results\n"
        f"-----------------------------\n"
        f"Total Votes: {str(total_votes)}\n"
        f"-----------------------------\n"
    )
    
    print(total_vote_count)
    
    # Write the total vote count to the text file
    txt_file.write(total_vote_count)
    
    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate, votes in candidate_dict.items():
        
        # Get the vote count and calculate the percentage
        percentage = (votes/total_votes) * 100           
        vote_percentages[candidate] = percentage

        # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winner = candidate
            winning_count = votes

        # Print and save each candidate's vote count and percentage
        candidate_results = (
            f"{candidate}: {percentage:.3f}% ({votes})\n"
              )
        print(candidate_results)

        with open(file_to_output,"w") as text_file: 
            txt_file.write(candidate_results)

    # Generate and print the winning candidate summary
    winning_summary = (
        f"-----------------------------\n"
        f"Winner: {winner}\n"
        f"-----------------------------\n"
    )

    print(winning_summary)
    
    # Save the winning candidate summary to the text file
    with open(file_to_output,"w") as text_file: 
        txt_file.write(winning_summary)
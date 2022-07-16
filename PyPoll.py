# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("Election_Analysis", "Analysis", "election_analysis.txt")

# Assign a variable to count total votes
total_votes = 0

# Assign a list to store candidate options
candidate_options = []

# Assign a dictionary to store votes for each candidate
candidate_votes = {}

# Winning Candidate Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        # Print the candidate name for each row
        candidate_name = row[2]

        # For each row determine if this is a new candidate name
        if candidate_name not in candidate_options:

            # Add the candidate name to the list of candidate options
            candidate_options.append(candidate_name)
    
            # Begin tracking the vote count for the candidate
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:
    
    # Assign a variable to count each candidate's votes
    votes = candidate_votes[candidate_name]

    # Assign a variable to calculate each candidate's vote percentage
    vote_percentage = ( float(votes) / float(total_votes) ) * 100
    
    # Output results for each candidate
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine for each candidate if they are the winner
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_candidate = candidate_name
        winning_count = votes
        winning_percentage = vote_percentage

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
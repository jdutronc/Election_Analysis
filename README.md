# Election_Analysis

## Audit Overview
The Colorado Board of Elections has tasked us with analyzing the latest elections results to come up with:
- the total number of votes cast
- a complete list of candidates who received votes
- the total number of votes that each candidate received
- the percentage of total votes that each candidate received
- th winner of the election based on popular vote

## Resources
- Data provided by the Colorado Board of Elections: elections_results.csv
- Python 3.7.6
- Visual Studio Code 1.69.1

## Audit Results

The results of the election (pictured right) show that:
<img align="right" src="https://github.com/jdutronc/Election_Analysis/blob/main/Resources/election_results.png" width=300>
- there were 369,711 total votes cast in the 3 districts of Arapahoe, Denver and Jefferson
- Each county received the following number of votes:
  - Denver 306,055 (82.8% of total votes)
  - Jefferson 38,855 (10.5%)
  - Arapahoe 24,801 (6.7%)
- Denver county received the overwhelming majority of the total number of votes (306,855 or 82.8%)
- 3 candidates received votes:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- the results for each candidate are:
  - Charles Casper Stockham: 23.0% (85,213)
  - Diana DeGette: 73.8% (272,892)
  - Raymon Anthony Doane: 3.1% (11,606)
- the winner of the election is Diana DeGette with 73.8% of the popular vote (272,892 votes cast)

## Audit Summary
This script can easily be used in the future for any upcoming election:
- the script can be used 'as is' for other elections whatever the number of counties, number of candidates or number of votes
- if the file format remains .csv and the structure of the raw data source remains the same (VoteID/County/Candidate), the only piece of code that would need updating is the path and possibly the name of the source file, here (lines 8-9):

```python
# Add a variable to load a file from a path.
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")
```

- if the structure of the raw data changes, be sure to update the column indexes in this piece here (lines 46-50):

```python
# Get the candidate name from each row.
candidate_name = row[2]

# Extract the county name from each row.
county_name = row[1]
```


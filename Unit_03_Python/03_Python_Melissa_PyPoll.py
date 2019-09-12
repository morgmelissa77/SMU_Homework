#!/usr/bin/env python
# coding: utf-8

# 
# ## PyPoll - Melissa Morgan


# Import Dependencies
import pandas as pd


# Save path to data set in a variable
py_poll = "Resources/election_data.csv"


# Use Pandas to read data
py_poll = pd.read_csv(py_poll)
py_poll.head()

#check type & info

py_poll.info()

#The total number of votes cast

total_votes = py_poll.County.count()
total_votes


# A complete list of candidates who received votes
candidates = py_poll["Candidate"].unique()
candidates

# A complete list of candidates who received votes and number of votes

count = py_poll["Candidate"].value_counts()
count

# The percentage of votes each candidate won 

percentage_votes = count/total_votes
percentage_votes

# The percentage of votes each candidate won (alt format)

percentage_votes = count/total_votes * 100
percentage_votes


# Create a data frame with given columns and value
py_poll_new = pd.DataFrame(
    {"Candidates": ['Khan', 'Correy', 'Li', "O'Tooley"],
     "Percent_of_Votes": [0.63, 0.20, 0.14, 0.03],
     "Total_Number_Votes": [2218231, 704200, 492940, 105630]
     })

py_poll_new


# Analysis of election results
output = (
    f"\nElection Results\n"
    f"---------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"---------------------------\n"
    f"{py_poll_new['Candidates'][0]}: {py_poll_new['Percent_of_Votes'][0]:.3%} ({py_poll_new['Total_Number_Votes'][0]})\n"
    f"{py_poll_new['Candidates'][1]}: {py_poll_new['Percent_of_Votes'][1]:.3%} ({py_poll_new['Total_Number_Votes'][1]})\n"
    f"{py_poll_new['Candidates'][2]}: {py_poll_new['Percent_of_Votes'][2]:.3%} ({py_poll_new['Total_Number_Votes'][2]})\n"
    f"{py_poll_new['Candidates'][3]}: {py_poll_new['Percent_of_Votes'][3]:.3%} ({py_poll_new['Total_Number_Votes'][3]})\n"
    f"---------------------------\n"
    f"Winner: {py_poll_new['Candidates'][0]}\n")
    
print (output)


text_file = open("Output.txt", "w") 
text_file.write(output) 
text_file.close()


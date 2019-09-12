#!/usr/bin/env python
# coding: utf-8

# ## PyBank
# 


# Import Dependencies
import pandas as pd


# Save path to data set in a variable
data_file = "Resources/budget_data.csv"


# Use Pandas to read data
data_file = pd.read_csv(data_file)
data_file.head()


# The total number of months included in the dataset

total_rows = data_file.Date.count()
total_rows 

# The net total amount of "Profit/Losses" over the entire period

total_profit = data_file["Profit/Losses"].sum()
total_profit

# The average of the changes in "Profit/Losses" over the entire period

total_profit/total_rows


changes = []
for indx, row in data_file.iterrows():
    if (indx < 85):
        change = data_file['Profit/Losses'][indx+1] - row['Profit/Losses']
        changes.append(change)
    

avg_change = sum(changes)/85


avg_change.round(decimals=2)


max_value = max(changes)
min_value = min(changes)


print (min_value)
print (max_value)


max_change = changes.index(max_value)
min_change = changes.index(min_value)


print (min_change)
print (max_change)


max_month = data_file.iloc[max_change + 1].Date
min_month = data_file.iloc[min_change +1].Date


print (min_month)
print (max_month)


output = (
    f"\nFinancial Analysis\n"
    f"---------------------------\n"
    f"Total Months: {total_rows}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${avg_change.round(decimals=2)}\n"
    f"Greatest Increase in Profit: {max_month} (${max_value})\n"
    f"Greatest Decrease in Profit: {min_month} (${min_value})\n")


print (output)


text_file = open("Output.txt", "w") 
text_file.write(output) 
text_file.close()




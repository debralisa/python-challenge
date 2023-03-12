#python challenge PyBank script

#Import Dependencies
import os
import csv

#failed attempt with code using os/path.join  Kept in comments to show progression
    #budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

#File locations for read and write files
#budget_data_csv = "/Users/debralisa3/Dropbox/python-challenge/PyBank/Resources/budget_data.csv"
#budget_out_txt = "/Users/debralisa3/Dropbox/python-challenge/PyBank/Analysis/budget_data_out.txt"
budget_data_csv = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources', 'budget_data.csv')
budget_out_txt = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'analysis', 'budget_data_out.txt')


#Profit/Loss Parameters and Lists for variables
total_months = 0
start_profit = 0
total_profit = 0

month_with_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

#Read in the csv file
#with open(budget_data_csv, 'r') as csvfile:


#read the csv, convert it into a list of dictionaries using DictReader.  Researched on DictReader
#cited on several sites 1 https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
#2 https://www.youtube.com/watch?v=5CEsJkKhS78  Thinking in terms of headers rather than
#indexes  This returns dictionaries instead of lists.

with open(budget_data_csv, "r") as profit_data:
    reader=csv.DictReader(profit_data)

    for row in reader:

        #calculating the totals through the rows
        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit/Losses"])

        #calculating the profit/loss changes
        profit_change = int(row["Profit/Losses"]) - start_profit
        start_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_with_change = month_with_change + [row["Date"]]

        #calculate the greatest increase in profit/loss with if statement
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profit_change

        #calculate the greatest decrease in profit/loss using if statement
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profit_change

#calculate the average of the profit/loss change
profit_aver = sum(profit_change_list)/len(profit_change_list)

#setup format for the Summary Information to print
output=(
    f"\nFinancial Analysis\n"
    f"______________________\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${profit_aver}\n"
    f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    
)

#Print the output summary
print(output)

#Export the summary output to the text file
with open(budget_out_txt, "w") as txt_file:
    txt_file.write(output)


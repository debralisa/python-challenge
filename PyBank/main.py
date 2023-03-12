#python challenge PyBank script
<<<<<<< HEAD
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
prev_profit = 0
total_profit = 0

month_of_change = []
profit_change_list = []
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999]

#Read in the CSV file
#with open(budget_data_csv, 'r') as csvfile:


#read the csv, convert it into a list of dictionaries using DictReader.  Researched on DictReader
#cited on several sites 1 https://courses.cs.washington.edu/courses/cse140/13wi/csv-parsing.html
#2 https://www.youtube.com/watch?v=5CEsJkKhS78  Thinking in terms of headers rather than
#indexes  This returns dictionaries instead of lists.

with open(budget_data_csv, "r") as profit_data:
    reader=csv.DictReader(profit_data)

    for row in reader:

        #track the totals
        total_months = total_months + 1
        total_profit = total_profit + int(row["Profit/Losses"])

        #track the profit/loss change
        profit_change = int(row["Profit/Losses"]) - prev_profit
        prev_profit = int(row["Profit/Losses"])
        profit_change_list = profit_change_list + [profit_change]
        month_of_change = month_of_change + [row["Date"]]

        #calculate the greatest increase
        if (profit_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = profit_change

        #calculate the greatest decrease
        if (profit_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = profit_change

#calculate the average profit/loss change
profit_aver = sum(profit_change_list)/len(profit_change_list)

#Output the Summary Information
output=(
    f"\nFinancial Analysis\n"
    f"______________________\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit}\n"
    f"Average Change: ${profit_aver}\n"
    f"Greatest Increase: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
    
)

#Print output
print(output)

#Export output to the text file
with open(budget_out_txt, "w") as txt_file:
    txt_file.write(output)
=======
>>>>>>> 0c19b7d359f6e4332631ccea2cde5e99fcaae89c

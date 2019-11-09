# Import Modules
import os
import csv

#Set file path
budget_csv = os.path.join("..","PyBank","Resources","budget_data.csv")

#Set variables
total_months= 0
total_profitloss= 0
monthly_change= 0
start= 0
dates= []
profits= []

#Open and read CSV file with delimiter set
with open(budget_csv, newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)    
    row = next(csvreader)
    total_months = 1
    total_profitloss += int(row[1])
    start = int(row[1])
    
    for row in csvreader:
        dates.append(row[0])
        change = int(row[1]) - start
        profits.append(change)
        start = int(row[1])
        total_months +=1

total_profitloss = total_profitloss + int(row[1])

greatest_increase = max(profits)
highest_index = profits.index(greatest_increase)
greatest_date = dates[highest_index]

greatest_decrease = min(profits)
lowest_index = profits.index(greatest_decrease)
worst_date = dates[lowest_index]

average_change = sum(profits)/len(profits)

print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_months}")
print(f"Total: $ {(total_profitloss)}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_date},(${str(greatest_increase)})")
print(f"Greatest Decrease in Profits:, {worst_date},(${str(greatest_decrease)})"


Financial Analysis
---------------------------
Total Months: 86
Total: $ 1538983
Average Change: $-2315.12
Greatest Increase in Profits:, Feb-12,($1926159)
Greatest Decrease in Profits:, Sep-13,($-2196167)

output_file= os.path.join('..',"PyBank","Resources","budget_data_completed.text")

with open(output_file,'w',)as txtfile:
    txtfile.write(f"Financial Analysis")
    txtfile.write(f"---------------------------")
    txtfile.write(f"Total Months: {total_months}")
    txtfile.write(f"Total: ${total_profitloss}")
    txtfile.write(f"Average Change: ${average_change:.2f}")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_date},(${str(greatest_increase)})")
    txtfile.write(f"Greatest Decrease in Profits:, {worst_date},(${str(greatest_decrease)})")

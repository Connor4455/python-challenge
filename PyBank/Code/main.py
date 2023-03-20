import os
import csv
import statistics

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

months = 0
profit = 0
greatest_increase = 0
best_month = ''
greatest_decrease = 0
worst_Month = ''
change = []
monthToMonthChange = []

with open(budget_data_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


    for row in csvreader:
        months += 1
        profit += int(row[1])
        if int(row[1]) > greatest_increase:
            best_month = (row[0])
            greatest_increase = int(row[1])
        elif int(row[1]) < greatest_decrease:
            worst_Month = (row[0])
            greatest_decrease = int(row[1])
        change.append(int(row[1]))

  
for i in range(len(change)-1):
    monthly_change = (change[i+1] - change[i])
    monthToMonthChange.append(monthly_change)   

average_change = statistics.mean(monthToMonthChange)

print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~~~~")
print("Total Months: " + str(months))
print("Total: $" + str(profit))
print("Average Change is: $" + str(round(average_change, 2)))
print("Greatest Increase in Profits: " + str(best_month) + "  ($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits: " + str(worst_Month) + "  ($" + str(greatest_decrease) + ")")

# now write this to an output file
output_file = os.path.join("..", "Analysis", "analysis.md")

with open(output_file,"w") as file:
    file.write("Financial Analysis")
    file.write("~~~~~~~~~~~~~~~~~~~~~")
    file.write("Total Months: " + str(months))
    file.write("Total: $" + str(profit))
    file.write("Average Change is: $" + str(round(average_change, 2)))
    file.write("Greatest Increase in Profits: " + str(best_month) + "  ($" + str(greatest_increase) + ")")
    file.write("Greatest Decrease in Profits: " + str(worst_Month) + "  ($" + str(greatest_decrease) + ")")





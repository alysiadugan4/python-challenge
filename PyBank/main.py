import csv
import os

total_profit_losses = 0
current = 0
last = 0
months = 0
total_change = 0


with open("Resources\-budget_data.csv",'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:

        total_profit_losses = total_profit_losses + int(row[1])

        months = months + 1

        current = int(row[1])

        if months > 1:

            change = current - last

            total_change = total_change + change

        last = int(row[1])

        average_change = total_change/months

    print("Financial Analysis\n")
    print("--------------------\n")
    print("Total months:" + str(months))
    print("Total:" + "${:.0f}".format(total_profit_losses))
    print("Average Change:" + str(round(average_change,2)))
    print("Greatest Increase in Profits:")
    print("Greatest Decrease in Profits:")

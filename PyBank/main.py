import csv
import os

total_profit_losses = []
current = 0
last = 0
months = 0
total_change = 0
max_change = 0
min_change = 0
t_change = []
month_year = []

with open("Resources\-budget_data.csv",'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)

    for row in csvreader:

        total_profit_losses = (int(row[1]))

        months = months + 1

        current = int(row[1])

        if months >= 1:

            change = current - last

            total_change = total_change + change

            t_change.append(change)

            month_year.append(row[0])

            last = int(row[1])

    #print(month_year)
    average_change = total_change/(months - 1)
    max_change = max(t_change)   
    max_index = t_change.index(max_change)
    min_change = min(t_change)
    min_index = t_change.index(min_change)

    #print(max_index)
       
    print("Financial Analysis\n")
    print("--------------------\n")
    print("Total months:" + str(months))
    print("Total:" + "${:.0f}".format(total_profit_losses))
    print("Average Change:" + str(round(average_change,2)))
    print("Greatest Increase in Profits:" + str(month_year[max_index])  + "," + "$" + str(max_change))
    print("Greatest Decrease in Profits:" + str(month_year[min_index])  + "," + "$" + str(min_change))


file_name = "PyBank.txt"

with open(file_name,'w') as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("--------------------\n")
    txt_file.write("Total months:" + str(months) + "\n")
    txt_file.write("Total:" + "${:.0f}".format(total_profit_losses) + "\n")
    txt_file.write("Average Change:" + str(round(average_change,2)) + "\n")
    txt_file.write("Greatest Increase in Profits:" + str(month_year[max_index])  + "," + "$" + str(max_change) + "\n")
    txt_file.write("Greatest Decrease in Profits:" + str(month_year[min_index])  + "," + "$" + str(min_change) + "\n")


#Import Dependecies
import os
import csv

#Declare file location
csv_file_path = ("Resources/budget_data.csv")

#create empty lists 
total_months=[]
total_profit= []
montly_profit_change=[]

#Open csv file
with open(csv_file_path,newline="",encoding="utf-8") as budget:

    #create variable to store content
    csvreader = csv.reader(budget,delimiter=",")

    #Skip header line
    header = next(csvreader)

    #Iterate through the rows
    for row in csvreader:
        #Append the total months and profits to their lists
        total_months.append(row[0])
        total_profit.append(int(row[1]))

    #Iterate trhough the profits to get the montly change
    for i in range(len(total_profit)-1):
         #Take the difference between two months and append to monthly profit change
        montly_profit_change.append(total_profit[i+1]-total_profit[i])

#Obtain the max and min of the the montly profit change list
max_increase_value = max(montly_profit_change)
max_decrease_value = min(montly_profit_change)
#Correlate the info to the proper month using month list and index from max and min
max_increase_month = montly_profit_change.index(max(montly_profit_change))+1
max_decrease_month = montly_profit_change.index(min(montly_profit_change))+1

#Print results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit)}")
print(f"Average Change: {round(sum( montly_profit_change)/len(montly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

#create output file
output_file = ("Resources/Financial_Analysis_Summary.txt")
#open output file
with open(output_file,'w') as file:
    #write results to print in the Analysis.txt
    file.write("Financial Analysis")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Total: ${sum(total_profit)}")
    file.write("\n")
    file.write(f"Average Change: {round(sum(montly_profit_change)/len(montly_profit_change),2)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
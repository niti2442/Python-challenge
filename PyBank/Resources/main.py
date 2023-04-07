#Modules
import os
import csv
#Set path for file
csvpath= os.path.join('.', 'Documents', 'Python-challenge', 'PyBank', 'Resources','budget_data.csv')
#List to store data
budget_data= []
#Open the csv
with open(csvpath, encoding='utf') as csvfile:
csvreader= csv.reader(csvfile,delimiter",")
for row in csvreader:
budget_data.append({"month": row["Date"], "amount": int(row["profit/losses"]),"change": 0})
#Total months
total_months= len(budget_data)
#Calculate changes between months
previous_amount= budget_data[0]["amount"]
i in range(total_months):
budget_data[i]["change"]= budget_data[i]["amount"]-previous_amount
prev_amount= budget_data[i]["amount"]
#Calculate the total amount
total_amount= sum(row['amount'] for row in budget_data)
#Calculate the average amount
total_change= sum(row['change'] for row in budget_data)
average= round(total_change/(total_months-1), 2)
#Greatest Increase and Decrease
get_increase= max(budget_data, key=lamdba x:x['change'])
get_decrease=min(budget_data, key=lambda x:x['change'])
#Print Financial Analysis
print ("Financial Analysis")
print("-----------------------")
print(f"Total Months: {len(Total_Months)}")
print(f"total: ${sum(Total_Profit)}")
print(f"Average Change: {round(sum(Monthly_Profit_Change)/len(Monthly_Profit_Change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")
#Output files
output_file= path("Documents", "Python-challenge", "PyBank", "Resources", "Financial Analysis_Summary.txt")
with open(output_file,"w") as file:
#Print Financial Analysis summary
file.write("Financial Analysis")
file.write("\n")
file.write("--------------------")
file.write("\n")
file.write(f"Total Months: {len(total_months)}")
file.write("\n")
file.write(f"Total: ${sum(total_profit)}")
file.write("\n")
file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
file.write("\n")
file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
file.write("\n")
file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

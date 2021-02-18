import os
import csv

budget_data_csv = os.path.join('./Resources/budget_data.csv')

#create values and lists
total_months = 0
total_pl = 0
previous_value = 0
monthly_change = 0
dates = []
profit_loss = []

#Open and read the CSV file
with open(budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)

    #Finding inital values from the first row
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    previous_value = int(first_row[1])
    
    #loop through each row
    for row in csvreader:
        
        # Keep track of the dates
        dates.append(row[0])
        
        # Calculate the value change, then add it to list of changes
        monthly_change = int(row[1])-previous_value
        profit_loss.append(monthly_change)
        previous_value = int(row[1])
        
        #Add months to find total 
        total_months = total_months + 1

        #Add the profits or losses for each row 
        total_pl = total_pl + int(row[1])

    #find greatest increase in profits and the associated date
    greatest_increase_pl = max(profit_loss)
    greatest_increase_date = dates[profit_loss.index(greatest_increase_pl)]

    #find greatest decrease in profits and the associated date 
    greatest_decrease_pl = min(profit_loss)
    greatest_decrease_date = dates[profit_loss.index(greatest_decrease_pl)]

    #Average change in Profit/Losses between months over entire period
    avg_change = sum(profit_loss)/len(profit_loss)


print("Financial Analysis")
print("---------------------------------------")
print(f"Total Months: {int(total_months)}")
print(f"Total: ${int(total_pl)}")
print(f"Average Change: $ {(avg_change):.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_pl})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_pl})")

output_path = os.path.join('./Analysis', "analysis.txt")
with open(output_path, 'w') as txt_file:
    
    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------------------------------\n")
    txt_file.write(f"Total Months: {int(total_months)}\n")
    txt_file.write(f"Total: ${int(total_pl)}\n")
    txt_file.write(f"Average Change: $ {(avg_change):.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_pl})\n")
    txt_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_pl})\n")
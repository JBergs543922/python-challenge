#library imports
import csv
import os
import statistics

#script variables
csv_header = " "
months_sum = 0
revenue_sum = 0.0
average_change_value = 0.0
revenue_list = []
monthly_change = []
average_final = 0.0
changes_list = []
greatest_increase_index = 0
greatest_decrease_index = 0
greatest_increase = 0.0
greatest_decrease = 0.0

#define the file path and read into reader
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")
with open(csv_path, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

        #read and store csv file header  
    csv_header = next(csv_reader)

        #logic control to loop through csv document/read needed values into lists and calculate months and total while reading
    for row in csv_reader:
        
        #read to from csv to list
        revenue_list.append(float(row[1]))
        
        #add to months_sum
        months_sum = months_sum+1
        
        #add to revenue_sum
        revenue_sum = revenue_sum + float(row[1])
        #logic control to loop through the csv document ends     
#csv reader closes

#logic control to evaluate revenue_sum list and
for x in range(len(revenue_list)-1):
        
        #calculate monthly changes and fill changes list 
        monthly_change.append(revenue_list[x+1] - revenue_list[x])

#determine final aver-age_change, greatest_increase, greatest_decrease
average_final = round(statistics.mean(monthly_change),2)
greatest_increase = round(max(monthly_change),2)
greatest_decrease = round(min(monthly_change),2)

#write to text file and create
filename = 'PyBank/Analysis/financial_analysis.csv'
fpath = ('PyBank/Analysis/financial_analysis.csv')
with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["Financial Analysis"])
        csvwriter.writerow(" ")
        csvwriter.writerow(["------------------"])
        csvwriter.writerow(" ")
        csvwriter.writerow(["Total Months: " + str(months_sum)])
        csvwriter.writerow(" ")
        csvwriter.writerow(["Total Revenue: $" + str(revenue_sum)])
        csvwriter.writerow(" ")
        csvwriter.writerow(["Average Change: $" + str(average_final)])
        csvwriter.writerow(" ")
        csvwriter.writerow(["Greatest Increase in Profits: $"+ str(greatest_increase)])
        csvwriter.writerow(" ")
        csvwriter.writerow(["Greatest Decrease in Profits: $"+ str(greatest_decrease)])
        csvwriter.writerow(" ")
        csvwriter.writerow(["------------------"])
#write to text file closes

#print results
print("Financial Analysis")
print(" ")
print("---------------------------")
print(" ")
print("Total Months: " + str(months_sum))
print(" ")
print("Total Revenue: $" + str(revenue_sum))
print(" ")
print("Average Change: $" + str(average_final))
print(" ")
print("Greatest Increase in Profits: $"+ str(greatest_increase))
print(" ")
print("Greatest Decrease in Profits: $"+ str(greatest_decrease))
print(" ")
print("---------------------------")
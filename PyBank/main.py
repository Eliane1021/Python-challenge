import os
import csv

#path the csv file
budget_csv = os.path.join("C:/Users/Yiling C/Desktop/Data Analysis/python_challegen/Starter_Code/PyBank/Resources/budget_data.csv")
# budget_csv = os.path.join("..","PyBank","Resources""budget_data.csv")

#list of variable
months=[]
total_Profit=[]
change_Profit=[]

#open and read csv
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

# find the first row of header
    csvheader = next(csvreader)
    print(f"Header:{csvheader}")

#loop for the total month 
    for row in csvreader:    
        months.append(row[0])
        total_Profit.append(int(row[1])) 

#calcultate the chage of profit 

    for x in range(1, len(total_Profit)):
        change_Profit.append((int(total_Profit[x]) - int(total_Profit[x-1])))
    
    # calculate average revenue change
    revenue_average = sum(change_Profit) / len(change_Profit)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(change_Profit)
    # greatest decrease in revenue
    greatest_decrease = min(change_Profit)


#the analysis of budget data:

#print out the result
    print("Financial Analysis")

    print("....................................................................................")

    print("total months: " + str(total_months))

    print("Total: " + "$" + str(sum(total_Profit)))

    print("Average change: " + "$" + str(round(revenue_average, 2)))

    print("Greatest Increase in Profits: " + str(months[change_Profit.index(max(change_Profit))+1]) + " " + "$" + str(greatest_increase))

    print("Greatest Decrease in Profits: " + str(months[change_Profit.index(min(change_Profit))+1]) + " " + "$" + str(greatest_decrease))


    # output to a text file

    file = open("Analysis.txt","w")

    file.write("Financial Analysis")

    file.write("....................................................................................")

    file.write("total months: " + str(total_months))

    file.write("Total: " + "$" + str(sum(total_Profit)))

    file.write("Average change: " + "$" + str(round(revenue_average, 2)))

    file.write("Greatest Increase in Profits: " + str(months[change_Profit.index(max(change_Profit))+1]) + " " + "$" + str(greatest_increase))

    file.write("Greatest Decrease in Profits: " + str(months[change_Profit.index(min(change_Profit))+1]) + " " + "$" + str(greatest_decrease))

    file.close()






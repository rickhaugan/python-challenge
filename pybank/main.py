import os
import csv

#gets current path
mypath = os.getcwd()
#adds current path to file source path
mypath = mypath + '\\resources\\budget_data.csv'

#declare 2 lists for column 1 and 2
mydates = []
mytrans = []

#opens file and appends to lists
with open(mypath) as data2:
    mylist = csv.reader(data2)
    for x in mylist:
        mydates.append(x[0])
        mytrans.append(x[1])

#column header names if needed
col1_header = mydates[0]
col2_header = mytrans[0]

#calc total months
total_months = len(mydates) - 1

#initialize variables
i = 1
mytotal= 0
greatest_increase = 0
greatest_decrease = 0
avg_change = []



while i < (len(mytrans)):
    #sums column 2 values
    mytotal = mytotal + int(mytrans[i] ) 
    
    #appends to new list to calc averages
    if (i + 1) < (len(mytrans)): 
        avg_change.append(int(mytrans[i+1]) - int(mytrans[i]))

    #Does calc to determine greatest increase
    if (greatest_increase == 0) and (i < len(mytrans)):
        greatest_increase = int(mytrans[i+1]) - int(mytrans[i])
        greatest_increase_date = mydates[i+1]

    elif (i + 1) < (len(mytrans)):
        if greatest_increase < (int(mytrans[i+1]) - int(mytrans[i])):
            greatest_increase = (int(mytrans[i+1]) - int(mytrans[i]))
            greatest_increase_date = mydates[i+1]

    #Does calc to determine greatest decrease
    if (greatest_decrease == 0) and (i < len(mytrans)):
        greatest_decrease = int(mytrans[i+1]) - int(mytrans[i])
        greatest_decrease_date = mydates[i+1]

    elif (i + 1) < (len(mytrans)):
        if greatest_decrease > (int(mytrans[i+1]) - int(mytrans[i])):
            greatest_decrease = (int(mytrans[i+1]) - int(mytrans[i]))
            greatest_decrease_date = mydates[i+1]

            
    i += 1


#calc Average change
myaverage = sum(avg_change)/len(avg_change)

#get filename from user
valid_input = True
while valid_input:
    filename = input("\nWhat do you want the text output file to be named? ---> " )
    if len(filename) > 0:
        filename = filename.strip() + ".txt"
        valid_input = False
    else:
        print("\nInvalid filename.  Must be at least 1 character long. \n")

print("------------------")
print("\nFinancial Analysis")
print("\n------------------")
print(f"\nTotal months: {total_months}")
print(f"\nTotal: ${mytotal}")
print(f"\nAverage change: ${round(myaverage,2)}")
print(f"\nGreatest increase was on: {greatest_increase_date} for ${greatest_increase}.")
print(f"\nGreatest decrease was on: {greatest_decrease_date} for ${greatest_decrease}.")


#prints to file that already exists
if os.path.exists(filename):
    outfile = open(filename, "w")
    outfile.write("------------------")
    outfile.write("\nFinancial Analysis")
    outfile.write("\n------------------")
    outfile.write(f"\nTotal months: {total_months}")
    outfile.write(f"\nTotal: ${mytotal}")
    outfile.write(f"\nAverage change: ${round(myaverage,2)}")
    outfile.write(f"\nGreatest increase was on: {greatest_increase_date} for ${greatest_increase}.")
    outfile.write(f"\nGreatest decrease was on: {greatest_decrease_date} for ${greatest_decrease}.")
    outfile.close()
#creates new file and prints to file
else:
    outfile = open(filename, "x")
    outfile.write("------------------")
    outfile.write("\nFinancial Analysis")
    outfile.write("\n------------------")
    outfile.write(f"\nTotal months: {total_months}")
    outfile.write(f"\nTotal: ${mytotal}")
    outfile.write(f"\nAverage change: ${round(myaverage,2)}")
    outfile.write(f"\nGreatest increase was on: {greatest_increase_date} for ${greatest_increase}.")
    outfile.write(f"\nGreatest decrease was on: {greatest_decrease_date} for ${greatest_decrease}.")

outfile.close()


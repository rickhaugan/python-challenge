import os
import csv
from datetime import datetime as dt

#gets current path
mypath = os.getcwd()
#adds current path to file source employee data file path
mypath = mypath + '\\employee_data.csv'

#declare lists for columns
emp_id = []
full_name = []
dob = []
ssn = []
state = []

#opens file and appends to lists
with open(mypath) as data:
    employee_list = csv.reader(data)
    for x in employee_list:
        emp_id.append(x[0])
        full_name.append(x[1])
        dob.append(x[2])
        ssn.append(x[3])
        state.append(x[4])

#column header names if needed
col1_header = emp_id[0]
col2_header = full_name[0]
col3_header = dob[0]
col4_header = ssn[0]
col5_header = state[0]

#Format DOB
i = 1
format_date_list = []
while (i < (len(dob))):
    mydate = dt.strptime((dob[i]), "%Y-%m-%d")
    formatted_date = dt.strftime(mydate,"%m/%d/%Y")
    format_date_list.append(formatted_date)  
    i += 1

#add header
format_date_list.insert(0,col3_header)    



#SSN changes
i = 1
format_ssn_list = []
while (i < (len(ssn))):
    formatted_ssn = "***-**-" + str(ssn[i])[-4] + str(ssn[i])[-3] + str(ssn[i])[-2] + str(ssn[i])[-1]
    format_ssn_list.append(formatted_ssn)  
    i += 1

#add header
format_ssn_list.insert(0,col4_header)    




mystatefilepath = os.getcwd()
#adds current path to file source path
#This file has state names and abrevations
mystatefilepath = mystatefilepath + '\\states.csv'

#declare lists for columns
statesfile = []
statesabvfile = []


#opens file and appends to lists
with open(mystatefilepath) as data2:
    state_file_list = csv.reader(data2)
    for x in state_file_list:
        statesfile.append(x[0])
        statesabvfile.append(x[1])


#State changes
i = 1
format_state_list = []
while (i < (len(state))):
    #Finds state abrevation from full state name
    tempstate = state[i]
    mystateindex = statesfile.index(tempstate)
    myabvstate = statesabvfile[mystateindex]
    format_state_list.append(myabvstate)

    i += 1

#add header
format_state_list.insert(0,col5_header)    



#get filename from user to output file
valid_input = True
while valid_input:
    filename = input("\nWhat do you want the csv output file to be named? ---> " )
    if len(filename) > 0:
        filename = filename.strip() + ".csv"
        valid_input = False
    else:
        print("\nInvalid filename.  Must be at least 1 character long. \n")


#overwrites current file
if os.path.exists(filename):
    outfile = open(filename, "w")
    i=1
    outfile.write(f"{emp_id[0]},first_name,last_name,{format_date_list[0]},{format_ssn_list[0]},{format_state_list[0]}\n")
    while i <  len(emp_id):
        namestripped = full_name[i].replace(" ",",")
        outfile.write(f"{emp_id[i]},{namestripped},{format_date_list[i]},{format_ssn_list[i]},{format_state_list[i]}\n")
        i += 1

#creates new file and prints to file
else:
    outfile = open(filename, "x")
    i=1
    outfile.write(f"{emp_id[0]},first_name,last_name,{format_date_list[0]},{format_ssn_list[0]},{format_state_list[0]}\n")
    while i <  len(emp_id):
        namestripped = full_name[i].replace(" ",",")
        outfile.write(f"{emp_id[i]},{namestripped},{format_date_list[i]},{format_ssn_list[i]},{format_state_list[i]}\n")
        i += 1


outfile.close()
import os
import csv

#gets current path
mypath = os.getcwd()
#adds current path to file source path
mypath = mypath + '\\resources\\election_data.csv'

#declare lists for columns
myvoterid = []
mycounty = []
mycandidate = []


#opens file and appends to lists
with open(mypath) as data2:
    mylist = csv.reader(data2)
    for x in mylist:
        myvoterid.append(x[0])
        mycounty.append(x[1])
        mycandidate.append(x[2])

#column header names if needed
col1_header = myvoterid[0]
col2_header = mycounty[0]
col3_header = mycandidate[0]

# print (col1_header)
# print (col2_header)
# print (col3_header)

#calc total voters
total_voters = len(myvoterid) - 1

#initialize variables
i = 1
khan_total = 0
li_total = 0
correy_total = 0
tooley_total = 0




while i < (len(mycandidate)):
    #sums column 2 values
    if mycandidate[i] == "Khan":
        khan_total += 1

    if mycandidate[i] == "Correy":
        correy_total += 1

    if mycandidate[i] == "Li":
        li_total += 1

    if mycandidate[i] == "O'Tooley":
        tooley_total += 1                

    i += 1

#Determines winner based on who has the largest total of votes
if khan_total > correy_total and khan_total > li_total and khan_total > tooley_total:
    winner = "Khan"
elif correy_total > khan_total and correy_total > li_total and correy_total > tooley_total:
    winner = "Correy"
elif li_total > khan_total and li_total > correy_total and li_total > tooley_total:
    winner = "Li"
elif tooley_total > khan_total and tooley_total > li_total and tooley_total > correy_total:
    winner = "O'TOoley"    
else:
    winner = "Houston, we have a problem!"


#get filename from user
valid_input = True
while valid_input:
    filename = input("\nWhat do you want the text output file to be named? ---> " )
    if len(filename) > 0:
        filename = filename.strip() + ".txt"
        valid_input = False
    else:
        print("\nInvalid filename.  Must be at least 1 character long. \n")

#Print results to screen
print("------------------")
print("\nElection Results")
print("\n------------------")
print(f"\nTotal votes: {total_voters}")
print("\n------------------")
print(f"\nKhan: {round((khan_total / total_voters)*100,3)}% ({khan_total})")
print(f"\nCorrey: {round((correy_total / total_voters)*100,3)}% ({correy_total})")
print(f"\nLi: {round((li_total / total_voters)*100,3)}% ({li_total})")
print(f"\nO'Tooley: {round((tooley_total / total_voters)*100,3)}% ({tooley_total})")
print("\n------------------")
print(f"\nWinner is: {winner}!")
print("\n------------------")



#prints to file that already exists
if os.path.exists(filename):
    outfile = open(filename, "w")
    outfile.write("------------------")
    outfile.write("\nElection Results")
    outfile.write("\n------------------")
    outfile.write(f"\nTotal votes: {total_voters}")
    outfile.write("\n------------------")
    outfile.write(f"\nKhan: {round((khan_total / total_voters)*100,3)}% ({khan_total})")
    outfile.write(f"\nCorrey: {round((correy_total / total_voters)*100,3)}% ({correy_total})")
    outfile.write(f"\nLi: {round((li_total / total_voters)*100,3)}% ({li_total})")
    outfile.write(f"\nO'Tooley: {round((tooley_total / total_voters)*100,3)}% ({tooley_total})")
    outfile.write("\n------------------")
    outfile.write(f"\nWinner is: {winner}!")
    outfile.write("\n------------------")
#creates new file and prints to file
else:
    outfile = open(filename, "x")
    outfile.write("------------------")
    outfile.write("\nElection Results")
    outfile.write("\n------------------")
    outfile.write(f"\nTotal votes: {total_voters}")
    outfile.write("\n------------------")
    outfile.write(f"\nKhan: {round((khan_total / total_voters)*100,3)}% ({khan_total})")
    outfile.write(f"\nCorrey: {round((correy_total / total_voters)*100,3)}% ({correy_total})")
    outfile.write(f"\nLi: {round((li_total / total_voters)*100,3)}% ({li_total})")
    outfile.write(f"\nO'Tooley: {round((tooley_total / total_voters)*100,3)}% ({tooley_total})")
    outfile.write("\n------------------")
    outfile.write(f"\nWinner is: {winner}!")
    outfile.write("\n------------------")


outfile.close()


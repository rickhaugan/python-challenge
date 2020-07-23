import os
import re

#gets current path
mypath = os.getcwd()
#adds current path to file source path
filename = input("Enter the filename you want to process. (paragraph_1.txt,paragraph_2.txt or paragraph_3.txt):")
mypathfile1 = mypath + "\\raw_data\\" + filename
#open file
file1 = open(mypathfile1,"r") 
#split out file by words
filedata = (str(file1.readlines()).split())
file1.close()

totalletterCount = 0
averagelettercountperfile = 0
for x in filedata:
    totalletterCount += int(len(x))

#Approx Average letter count
averagelettercountperfile =  round(totalletterCount / int(len(filedata)),2)


#File read without splitting
filesub = open(mypathfile1,"r") 
filedataNOSPLIT = (filesub.readlines())
filesub.close()

entireFilePerLine = []
for line in filedataNOSPLIT:
    entireFilePerLine.append(line)
   
# print(f"entire file per line var {len(entireFilePerLine)}")
mytextlistbysentence = []
mytextlistbysentence = re.split("(?<=[.!?]) +", entireFilePerLine[0], maxsplit=0)


# for words in mytextlist:
mysentencesplit = []
for sentence in mytextlistbysentence:
    mysentencesplit.append(sentence.split())

wordcounttotal = 0
wordcountpersentence = []
#split sentences into word count
for x in mysentencesplit:
    wordcountpersentence.append(len(str(x).split()))

lettercountperword = []
totalwords = 0
for x in mysentencesplit:
    lettercountperword.append(len(str(x).split()))
    totalwords += len(str(x).split())

#count words in sentences
for x in wordcountpersentence:
    wordcounttotal += int(x)



sentence_count = len(mysentencesplit)
avgwordspersent = wordcounttotal / sentence_count

print(f"Approximate Word Count: {totalwords}")
print (f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {averagelettercountperfile}")
print (f"Average Sentence Length: {avgwordspersent}")

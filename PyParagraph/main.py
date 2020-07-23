import os
import re
from nltk.tokenize import sent_tokenize

#gets current path
mypath = os.getcwd()
#adds current path to file source path
filename = input("Enter the filename you want to process. (Default:paragraph_3.txt) --->")

#Default filename if nothing entered
if filename == "":
    filename = "paragraph_3.txt"

mypathfile1 = mypath + "\\raw_data\\" + filename

#File read 
filesub = open(mypathfile1,"r") 
filedata = (filesub.readlines())
filesub.close()


entireFilePerLine = []
for line in filedata:
    entireFilePerLine.append(line)


#split file into words
filedatatosplit = []
filedatatosplit = str(filedata).split()


totallettercount = 0
#get total letters per all words in file
for words in filedatatosplit:
    totallettercount += int(len(re.sub("[^A-Za-z0-9_]","",words)))


#average of total letters per word per file
avglettersperwordperfile = round(totallettercount / int(len(filedatatosplit)),2)


# split file by sentence
mytextlistbysentence = []
for line in entireFilePerLine:
    #imported package https://www.nltk.org/
    mytextlistbysentence += (sent_tokenize(str(line))) 



# gets words in sentence
# gets sentence length
# sums sentences lengths
wordsinsent = []
sentencelength = []
sumofsentenceslength = 0
for sentence in mytextlistbysentence:
    sentencelength.append(str(len(sentence)))
    wordsinsent +=(str(sentence).split())
    sumofsentenceslength += len(sentence)

avglengthpersent = round(sumofsentenceslength/len(sentencelength),2)
sentence_count = len(mytextlistbysentence)

print(f"Approximate Word Count: {len(wordsinsent)}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {avglettersperwordperfile}")
print(f"Average Sentence Length: {avglengthpersent}")

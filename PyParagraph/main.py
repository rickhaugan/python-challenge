import os
import re

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

filedataremovelinebeaks = []
#read file data and remove line breaks
for x in filedata:
    x = str.replace(x,"\n","")
    if len(x) > 1:
        filedataremovelinebeaks.append(x)


split_into_sentences = []
#split list into sentences
for line in filedataremovelinebeaks:
    split_into_sentences += (re.split("(?<=[.!?]) +",line))

sentence_count = len(split_into_sentences)



split_into_words = []
words_per_sentence = []
# split sentences into words
for sentence in split_into_sentences:
    split_into_words += (str(sentence).split())
    words_per_sentence.append(len(str(sentence).split()))

total_letter_count = 0
#get word length in characters
for words in split_into_words:
    total_letter_count += len(str(words))

word_count = len(split_into_words)
avg_letters_per_word = round(total_letter_count / word_count,2)
avg_sentence_length_per_words = round(sum(words_per_sentence) / len(words_per_sentence),2)


print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count (Per word): {avg_letters_per_word}")
print(f"Average Sentence Length(In words): {avg_sentence_length_per_words}")

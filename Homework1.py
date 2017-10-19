#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Alexandra Pawlak
TCSS 555
October 19, 2017
Homework #1

Description: Reads in transcript files and gathers information about the 
tokens. Calculates the TF, IDF, TF*IDF, and Probability of the 30 most
common words across all input files. 
"""
import glob
from collections import Counter
import re
import math

# Initialize counters and dictionaries
wordcount = Counter() #counter for words accross all docs
docCount = Counter() #counter for number of docs each word occurs in
top30TF = {} #dic for top 30 words TF
top30IDF = {} #dic for top 30 words IDF
top30TFIDF = {} #dic for top 30 words TF*IDF
top30Prob = {} #dic for top 30 words probabilities 
    
# Read Volg text files, change all words to lowercase, and remove punctuation
# Count occurances of each word and how many docs they're present in
def count(filelist):   
    for f in filelist:
        file = open(f, "r")
        text = file.read().lower()
        file.close()
        text = re.sub('[^a-z\ \']+', " ", text)
        words = text.split()
        wordcount.update(words)
        docWords = []
        for word in words:
            if word not in docWords:
                docWords.append(word)
        docCount.update(docWords)

# Returns number of Vlog documents
def numDocs(filelist):
    return len(filelist)

# Print word count for each word
#for item in wordcount.items(): print("{}\t{}".format(*item))

# Returns total number of words across all documents
def totalWordCount():
    return sum(wordcount.values())    

# Returns number of unique words across all documents
def uniqueWords():
    return(len(wordcount))

# Count words that only occur once
def occurOnce():
    once = 0
    for key in wordcount:
        if wordcount[key] == 1:
            once+=1
    return(once)

# Average number of words per document, rounded to nearest integer
def avgWords():
    return(round(sum(wordcount.values())/numDocs(filelist)))

# Calculate TF, IDF, TF*IDF, probability for 30 most frequent words
def mostFreq():
    top30 = wordcount.most_common(30)

    for i in range(len(top30)):
        tempWord = top30[i][0]
        tempCount = top30[i][1]
        tempDocCount = docCount[tempWord]
        top30TF[tempWord] = tempCount
        top30IDF[tempWord] = math.log10(numDocs(filelist)/tempDocCount)
        top30TFIDF[tempWord] = tempCount * top30IDF[tempWord]
        top30Prob[tempWord] = tempCount / totalWordCount()

# Read list of Vlog text files
filelist = glob.glob('./transcripts/*.txt')

# Process word counts in all documents
count(filelist)

# Run and store counts and calculations
total = totalWordCount()
unique = uniqueWords()
once = occurOnce()
avg = avgWords()
mostFreq()

# Open output file
out = open('output.txt', "w")

# Write results to output file
out.write('Total Word Count: {}\n'.format(total))
out.write('Number of Unique Words: {}\n'.format(unique))
out.write('Number of Words That Occur only Once: {}\n'.format(once))
out.write('Average Word Count Per Document: {}\n'.format(avg))

out.write('30 Most Frequent Words:\n')
out.write('Word\tTF\tIDF\tTF*IDF\tProbability\n')
for key in top30TF:
    out.write('{}:\t{}\t{}\t{}\t{}\n'.format(key, top30TF[key], round(top30IDF[key], 4), 
          round(top30TFIDF[key], 2), round(top30Prob[key], 4)))

# Close output file
out.close()


    

    
    
    
    
    
    
    

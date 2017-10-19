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

# Read list of Vlog text files
filelist = glob.glob('./transcripts/*.txt')

# Initialize counters and dictionaries
wordcount = Counter()
docCount = Counter()
top30IDF = {}
top30TFIDF = {}
top30Prob = {}
top30TF = {}
    
# Read Volg text files, change all words to lowercase, and remove punctuation
# Count occurances of words and how many docs they're present in
for f in filelist:
    file = open(f, "r")
    text = file.read().lower()
    file.close()
    text = re.sub('[^a-z\ \']+', " ", text)
    words = text.split()
    wordcount.update(text.split())
    docWords = []
    for word in words:
        if word not in docWords:
            docWords.append(word)
    docCount.update(docWords)

# Number of Vlog documents
numDocs = len(filelist)

# Print word count for all words
#for item in wordcount.items(): print("{}\t{}".format(*item))

# Total number of words across all documents
totalWordCount = sum(wordcount.values())
print('Total Word Count: {}'.format(totalWordCount))

# Average number of words per document, rounded to nearest integer
avgWords = round(sum(wordcount.values())/numDocs)
print('Average Word Count Per Document: {}'.format(avgWords))

# Print 30 most common words and their counts
#print(wordcount.most_common(30))

# Number of unique words across all documents
uniqueWords = len(wordcount)
print('Number of Unique Words: {}'.format(uniqueWords))

# 30 most frequently used words and their counts (TF)
top30 = wordcount.most_common(30)
#print(top30)

# Calculate IDF, TF*IDF, probability for top 30 words
for i in range(len(top30)-1):
    tempWord = top30[i][0]
    tempCount = top30[i][1]
    tempDocCount = docCount[tempWord]
    top30TF[tempWord] = tempCount
    top30IDF[tempWord] = math.log10(numDocs/tempDocCount)
    top30TFIDF[tempWord] = tempCount * top30IDF[tempWord]
    top30Prob[tempWord] = tempCount / totalWordCount

# Count words that only occur once
occurOnce = 0
for key in wordcount:
    if wordcount[key] == 1:
        occurOnce+=1
        
print('Number of Words That Occur only Once: {}'.format(occurOnce))

# Print TF, IDF, TF*IDF, Probabilities of top 30 words
print('30 Most Frequent Words')
print('Word\tTF\tIDF\tTF*IDF\tProbability')
for key in top30TF:
    print('{}:\t{}\t{}\t{}\t{}'.format(key, top30TF[key], round(top30IDF[key], 4), 
          round(top30TFIDF[key], 2), round(top30Prob[key], 4)))
    

    
    
    
    
    
    
    

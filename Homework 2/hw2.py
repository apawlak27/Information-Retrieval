"""
Alexandra Pawlak
TCSS 554
November 30, 2017
Homework #1

Description: Implementation of PageRank. Reads in an adjacency matrix (inputfile)
through a text file. The input file must be in the matrix format 
with 3 columns (i j k).
Each row denotes that the matrix contains a value k at the row i, column j.
The value k=1 denotes that there is a link from the document (node) i to 
document (node) j.
The dampening factorb (beta) is set to 0.85

The program outputs the original matrix, the original rank vector, 
the converged rank vector, and the number of iterations it took to convergence.
"""

import pandas as pd
import numpy as np

beta = 0.85
epsilon = 0.0001
inputfile = 'graph.txt'

# Read in adjacency matrix
df = pd.read_table(inputfile, sep=' ', header=None)
del df[2]

if isinstance(df[0][0], str) == True:
    for i in range(len(df[0])):
        df[0][i] = ord(df[0][i])-96
        df[1][i] = ord(df[1][i])-96

# Store unique values (nodes) in adjacency matrix
inNode = df[0].unique()
outNode = df[1].unique()
nodes = np.concatenate((inNode, outNode), axis=0)
nodes = np.unique(nodes)

# Find total number of nodes
numNodes = len(nodes)

#Count edges leaving each node
inCount = df[0].value_counts()
inCount = inCount.to_dict()

# Create matrix in dimensions of number of nodes and zero out
matrix = np.zeros((numNodes, numNodes))

# Fill transition matrix
for i in range(len(df[0])):
    tempIn = df[0][i]
    tempOut = df[1][i]
    matrix[tempIn-1][tempOut-1] = 1/inCount.get(tempIn)

matrix = np.transpose(matrix)
matrix = np.round(matrix, decimals = 6)

print('Matrix M:')
print(matrix)

# Multiply transistion matrix by dampening and round
matrix = matrix*beta
matrix = np.round(matrix, decimals=6)

# Create matrix for page ranks
rv = np.ones((numNodes, 1)) * (1/numNodes)
rv = np.round(rv, decimals = 6)

print('Original Rank Vector:')
print(rv)

#Calculate random jump value
jump = (1-beta)/numNodes

# Compute page ranks until convergence
iterCount = 1
while True:
    prev_rv = rv
    rv = np.matmul(matrix, rv) + jump
    rv = np.round(rv, decimals = 6)
    if (abs(np.subtract(rv, prev_rv))<epsilon).all():
        break
    iterCount+=1

# Print page ranks and number of iterations 
print('Converged Rank Vector:')
print(rv)
print('Number of Iterations to Convergence:')
print(iterCount)

    
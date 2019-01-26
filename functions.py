# -*- coding: utf-8 -*-

import numpy as np
def buildGraph(numberNodes):
    am = np.array([[1 if np.random.rand(1,1)>0.7 and x>y else 0 for x in range(numberNodes)]
    for y in range(numberNodes)]) #adjacent Matrix
    
    
    #Need to check to make sure every row has at least a single entry that is 1
    for x in range(numberNodes-1):
        if not any(am[x][:]):
            idx = np.random.randint(x+1,numberNodes,size=1)
            am[x][idx] = 1            
    
    amT = np.transpose(am) #transpose the matrix
    amF = am + amT #Full adjacency matrix
    return amF
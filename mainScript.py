import numpy as np
import networkx as nx
from matplotlib import pyplot

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

def plotGraph(adjacencyMatrix):
    (numberNodes, _) = adjacencyMatrix.shape
    
    G = nx.from_numpy_matrix(adjacencyMatrix)
    
    # Build the two plots
    pyplot.figure()
    
    # Plot for the adjacency matrix
    pyplot.subplot(1, 2, 1)
    pyplot.imshow(
        adjacencyMatrix,
        cmap="Greys",
        interpolation="none",
        extent=[0, numberNodes, 0, numberNodes],
    )
    ax1 = pyplot.gca()
    
    # Centers the labels on the axes
    ax1.xaxis.tick_top()
    ax1.set_xticks(np.arange(0.5, numberNodes + 0.5, 1))
    ax1.set_yticks(np.arange(0.5, numberNodes + 0.5, 1))
    ax1.set_xticklabels(np.arange(0, numberNodes, 1))
    ax1.set_yticklabels(np.arange(numberNodes - 1, -1, -1))
    
    # Plot of the graph
    pyplot.subplot(1, 2, 2)
    nx.draw(G, with_labels=True, font_weight="bold")
    
    pyplot.show()

def getRewardMatrix(adjacencyMatrix):
    (numberNodes,_) = adjacencyMatrix.shape
    #For the reward matrix:
    #If a transistion is not possible, make reward -10
    #If transistion is possible make reward -1
    
    #Thought process is that impossible transistions should be penalized
    #not sure if can use null, and may have to use something larger than -10
    #I believe it is necessary to also penalize movement because it may be
    #possible that the "agent" gets stuck going between nodes
    #the potential infinite loop could maybe be avoided by having some sort of
    #memory component but I'm hoping a -1 should be effective

    #Since it is python list comprehension
    rewardMatrix = np.array([[-10 if adjacencyMatrix[x][y]==0 else -1 
                     for x in range(numberNodes)]
                     for y in range(numberNodes)])
    return rewardMatrix


if __name__ == '__main__':
    NUM_NODES = 8

    adjacencyMatrix = buildGraph(NUM_NODES)
    plotGraph(adjacencyMatrix)
    rewardMatrix = getRewardMatrix(adjacencyMatrix)

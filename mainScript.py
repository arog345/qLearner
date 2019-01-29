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


if __name__ == '__main__':
    NUM_NODES = 8

    adjacencyMatrix = buildGraph(NUM_NODES)
    plotGraph(adjacencyMatrix)

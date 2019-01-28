import networkx as nx
from matplotlib import pyplot
import numpy as np

from functions import buildGraph

# Build the matrix
numberNodes = 8
adjacencyMatrix = buildGraph(numberNodes)
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

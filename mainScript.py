# -*- coding: utf-8 -*-

from functions import buildGraph
import networkx as nx
from matplotlib import pyplot

numberNodes = 8
am = buildGraph(numberNodes)

#This is just for plotting, will probably delete
nx.from_numpy_matrix(am)

fig = pyplot.figure(figsize=(5, 5)) # in inches
pyplot.imshow(am,
                  cmap="Greys",
                  interpolation="none")

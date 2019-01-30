import numpy as np
import networkx as nx
from matplotlib import pyplot


def main():
    NUM_NODES = 5
    GAMMA = 0.8
    NUM_EPISODES = 1

    adjacencyMatrix = buildGraph(NUM_NODES)
    plotGraph(adjacencyMatrix)

    # Create object to track the reward amounts for different actions
    rewardCalc = RewardCalculator(adjacencyMatrix) 

    # We would then have to run enough episodes in order for the Q matrix to converge or some time limit
    # Some code -- not really sure if this works
    Q = np.empty_like(adjacencyMatrix)
    episode = 0

    # For ease, just run a set number of episodes
    while episode < NUM_EPISODES:

        # Choose a random starting node
        currentNode = np.random.randint(0, adjacencyMatrix.shape[0])
        rewardCalc.reset()

        # Run one episode
        while not rewardCalc.hasReachedGoal():
            possibleNodes = rewardCalc.getActionsForNode(currentNode)
            nextNode = possibleNodes[np.random.randint(0, len(possibleNodes))]

            qValuesForNextNode = [
                rewardCalc.getReward(nextNode, x)
                for x in rewardCalc.getActionsForNode(nextNode)
            ]
            rewardForAction = rewardCalc.getReward(currentNode, nextNode)
            Q[currentNode][nextNode] = rewardForAction + GAMMA * max(qValuesForNextNode)

            rewardCalc.visitNode(nextNode)
            currentNode = nextNode

        episode += 1
    
    print(Q)


def buildGraph(numberNodes):
    am = np.array(
        [
            [
                1 if np.random.rand(1, 1) > 0.7 and x > y else 0
                for x in range(numberNodes)
            ]
            for y in range(numberNodes)
        ]
    )  # adjacent Matrix

    # Need to check to make sure every row has at least a single entry that is 1
    for x in range(numberNodes - 1):
        if not any(am[x][:]):
            idx = np.random.randint(x + 1, numberNodes, size=1)
            am[x][idx] = 1

    amT = np.transpose(am)  # transpose the matrix
    amF = am + amT  # Full adjacency matrix
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


class RewardCalculator:
    def __init__(self, adjacencyMatrix):
        if len(adjacencyMatrix.shape) != 2:
            raise Exception("Matrix should have rank 2")
        elif adjacencyMatrix.shape[0] != adjacencyMatrix.shape[1]:
            raise Exception("Matrix should be square")

        self.adjacencyMatrix = adjacencyMatrix
        self.numNodes = adjacencyMatrix.shape[0]
        self.visitedNodes = set()

    def getActionsForNode(self, node):
        self.__validateNodeNumber(node, "node")

        return [i for i, x in enumerate(self.adjacencyMatrix[node]) if x != 0]

    def getReward(self, fromNode, toNode):
        self.__validateNodeNumber(fromNode, "fromNode")
        self.__validateNodeNumber(toNode, "toNode")

        if self.adjacencyMatrix[fromNode][toNode] == 0:
            return -100
        elif toNode in self.visitedNodes:
            return -1
        else:
            return 1

    def visitNode(self, node):
        self.__validateNodeNumber(node, "node")

        self.visitedNodes.add(node)

    def hasReachedGoal(self):
        return len(self.visitedNodes) == self.numNodes

    def reset(self):
        self.visitedNodes = set()

    def __validateNodeNumber(self, nodeNumber, nodeType):
        if nodeNumber < 0 or nodeNumber >= self.numNodes:
            raise Exception(
                f"Invalid '{nodeType}' value. Expected: 0 < {nodeType} < {self.numNodes}. Actual: {nodeNumber}"
            )


if __name__ == "__main__":
    main()

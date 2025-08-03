class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def __init__(self):
        self.visited = set()
    def cloneGraph(self, node: Node) :
        self.visited.add(node.val)
        root = Node(node.val)
        for nighNode in node.neighbors :
            if nighNode.val not in self.visited :
                root.neighbors.append(self.cloneGraph(nighNode))
        return root        
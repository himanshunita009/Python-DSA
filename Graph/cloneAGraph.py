class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Node) -> Node:
        vis = dict()
        return self.solve(node,vis)
    def solve(self,node: Node,vis: dict):
        newNode = Node(node.val)
        vis[node.val] = newNode
        for adjNode in node.neighbors:
            if adjNode.val in vis:
                newNode.neighbors.append(vis[adjNode.val])
            else:
                newNode.neighbors.append(self.solve(adjNode,vis))
        return newNode

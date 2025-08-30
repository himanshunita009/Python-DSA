class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def finKey(self,root,key,pred,succ):
        if not root:
            return None,pred,succ
        if root.data < key:
            pred = root
            return self.finKey(root.right,key,pred,succ) 
        elif root.data > key :
            succ = root
            return self.finKey(root.left,key,pred,succ) 
        return root,pred,succ
    def findPredecessorFromtargetNode(self,node):
        if not node:
            return None
        if node.right:
            return self.findPredecessorFromtargetNode(node.right)
        return node
    def findSuccessorFromtargetNode(self,node):
        if not node:
            return None
        if node.left:
            return self.findSuccessorFromtargetNode(node.left)
        return node
    def findPreSuc(self, root, key):
        pred  = None
        succ  = None
        targetNode,pred,succ = self.finKey(root,key,pred,succ)
        if not targetNode:
            return [pred, succ]
        if targetNode.left :
            pred = self.findPredecessorFromtargetNode(targetNode.left)
        if targetNode.right:
            succ = self.findSuccessorFromtargetNode(targetNode.right)
        return [pred,succ]
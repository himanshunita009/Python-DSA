class Node :
    def __init__(self,x=0):
        self.left : Node = None
        self.right : Node = None
        self.val : int = x

def preOrderTraversal(root: Node):
    stack= []
    stack.append(root)
    while len(stack) > 0:
        curr = stack.pop()
        print(curr.val)
        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)
        
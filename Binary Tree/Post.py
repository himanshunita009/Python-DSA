class Node :
    def __init__(self,x=0):
        self.left : Node = None
        self.right : Node = None
        self.val : int = x
def postOrderTraversal(root: Node):
    stack = []
    curr = root
    while curr is not None or stack:
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()
    print(curr.val)
    curr = curr.left
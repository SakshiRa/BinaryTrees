import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTreePostOrder(postorder, inorder):
  
   
    postlength = len(postorder)
    inlength = len(inorder)
    if postlength != inlength or postorder == None or inorder == None or postlength ==0:
        return None
    root = BinaryTreeNode(postorder[-1])
    rootIndex = inorder.index(root.data)
    
    root.left = buildTreePostOrder(postorder[:rootIndex],inorder[:rootIndex])
    root.right = buildTreePostOrder(postorder[rootIndex:-1],inorder[rootIndex +1 :])
    
    return root
    pass

def printLevelATNewLine(root):
    # Given a binary tree, print the level order traversal. Make sure each level
    # start in new line.
    if root==None:
        return
    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)
    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left!=None:
                outputQ.put(curr.left)
            if curr.right!=None:
                outputQ.put(curr.right)
        print()
        inputQ, outputQ = outputQ, inputQ

# Main
n=int(input())
postOrder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
root = buildTreePostOrder(postOrder, inorder)
printLevelATNewLine(root)
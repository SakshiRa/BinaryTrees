import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def heightOfTree(root):
    if root == None:
        return 0
    
    
    leftheight = heightOfTree(root.left)
    rightheight = heightOfTree(root.right)
    largest = max(leftheight,rightheight)
    return 1 + largest 
    # Find the Height Of Binary Tree
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    

def buildLevelTree():
    
    root = BinaryTreeNode(int(input()))
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = int(input())
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = int(input())
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
root = buildLevelTree()
print(heightOfTree(root))


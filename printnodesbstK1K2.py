import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def elementsInRangeK1K2(root, k1, k2):
 
    if root == None:
        return None
    if k1 <= root.data and k2 >= root.data:
        elementsInRangeK1K2(root.left,k1,k2)
        print(root.data, end = " ")
        elementsInRangeK1K2(root.right, k1,k2)
        return
    if k1 > root.data:
        elementsInRangeK1K2(root.right,k1,k2)
    else:
        elementsInRangeK1K2(root.left,k1,k2)
    
   
    
    # Given a Binary Search Tree and two integers k1 and k2, find and print the
    # elements which are in range k1 and k2 (both inclusive). Print the elements
    # in increasing order.
    # Solution: Since the elemnts have to be printed in increasing oder we will
    # use in-order traversal and print the node only if it lies between range
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass

def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k1, k2 = (int(i) for i in input().strip().split())
elementsInRangeK1K2(root, k1, k2)


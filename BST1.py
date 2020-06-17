import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
        
        
def searchInBST(root, k):
    if root == None:
        return None
    if root == k:
        return root
    if k > root.data:
        return searchInBST(root.right, k)
    else:
        return searchInBST(root.left, k)
    
    
def elementsInRangeK1K2(root, k1, k2):
 
    if root == None:
        return 
    if  k1 > root.data:
        elementsInRangeK1K2(root.right,k1,k2)
    elif root.data > k2:
        elementsInRangeK1K2(root.left,k1,k2)
    else:
        print(root.data, end = " ")
        elementsInRangeK1K2(root.left,k1,k2)
        elementsInRangeK1K2(root.right, k1,k2)
        
        
def BuildBSTusingArray(lst):
    if n == None:
        return None
    middleindex = int(len(n)/2)
    rootindex = n[middleindex]
    leftindex = n[:middleindex]
    rightindex = n[middleindex+1:]
    root = BinaryTreeNode(rootindex)
    BuildBSTusingArray(leftindex)
    BuildBSTusingArray(rightindex)
    root.left = leftindex
    root.right = rightindex
    return root
    
    
    
    
    
    
        
    
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
#root = buildLevelTree(levelOrder)
#k1, k2 = (int(i) for i in input().strip().split())
#elementsInRangeK1K2(root, k1, k2)
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=BinaryTreeNode(lst)
#preOrder(root)
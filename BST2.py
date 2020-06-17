import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def BuildBSTusingArray(lst):
    n = len(lst)
    if lst == None or n <= 0:
        return None
    rootindex = (n-1)//2
   
    leftindex = lst[:rootindex]
    rightindex = lst[rootindex+1:]
    root = BinaryTreeNode(lst[rootindex])
    root.left = BuildBSTusingArray(leftindex)
    root.right = BuildBSTusingArray(rightindex)
    return root

def mintree(root):
    if root == None:
        return 100000
    leftmin = mintree(root.left)
    rightmin = mintree(root.right)
    return min(leftmin,rightmin,root.data)

def maxtree(root):
    if root == None:
        return -100000
    leftmax = maxtree(root.left)
    rightmax = maxtree(root.right)
    return max(leftmax,rightmax,root.data)


def checkifBST(root):
# first create a min and max function
    if root == None:
        return True
    leftmax = maxtree(root.left)
    rightmin = mintree(root.right)
    if leftmax > root.data and rightmin < root.data:
        return False
    isleftBST = checkifBST(root.left)
    isrightBST = checkifBST(root.right)
    return isleftBST and isrightBST



def isBST2(root):
    if root == None:
        return 100000, -100000, True
    leftmin, leftmax, isleftBST = isBST2(root.left)
    rightmin, rightmax, isrightBST = isBST2(root.right)
    minimum = min(leftmin, rightmin, root.data)
    maximum = max(rightmax, rightmax, root.data)
    istreeBST = True
    if root.data <= leftmax and root.data > rightmax:
        istreeBST = False
    if not(isleftBST) or not(isrightBST):
        return minimum, maximum, istreeBST
    





def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

    
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
#levelOrder = [int(i) for i in input().strip().split()]
# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=BuildBSTusingArray(lst)
preOrder(root)
checkifBST(root)






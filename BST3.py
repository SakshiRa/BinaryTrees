import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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


#node to root path print
#create a function
def nodetopath(root,s):
    #take base cases
    if root == None:
        return None
    if root.data == s:
    #create an empty list and append root.data into it
        l = list()
        l.append(root.data)
        return l
    #if none of them is true then use recursion on both left and right tree
    leftoutput = nodetopath(root.left,s)
    if leftoutput != None:
        leftoutput.append(root.data)
        return leftoutput
    rightoutput = nodetopath(root.right,s)
    if rightoutput != None:
        rightoutput.append(root.data)
        return rightoutput
    else:
        return None
    
# node to root path in BST
def nodetorootBST(root,data):
    if root == None:
        return None
    if root.data == data:
        l = list()
        l.append(root.data)
        return root
    if root.data > data:
        leftoutput = nodetorootBST(root.left, data)
        if leftoutput != None:
            leftoutput.append(root.data)
            return leftoutput
        else: 
             rightoutput = nodetorootBST(root.right, data)
             if rightoutput != None:
                 rightoutput.append(root.data)
                 return rightoutput
        
        

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)   
data = int(input())
path = nodetorootBST(root,data)
if path is not None:
    for ele in path:
        print(ele)

    
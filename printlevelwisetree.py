
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def printLevelWise(root):
        if root == None:
            return
        #make a queue
        q = queue.Queue()
        #put root in queue
        q.put(root)
        # work while q is not empty
        while (not(q.empty())):
            # take out the current node
            curr = q.get()
            #assign a variable to currdata
            currdata = curr.data
            left =-1
            right =-1
            #check if curr.left is valid or not
            if curr.left != None:
                # assign a variabla name to curr.left
                left = curr.left.data
                #put it into queue
                q.put(curr.left)
                # repeat for right 
            if curr.right != None:
                right = curr.right.data
                q.put(curr.right)
                
                
            print(currdata,":L:",left,",R:",right,sep = "")

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
printLevelWise(root)           
            
            


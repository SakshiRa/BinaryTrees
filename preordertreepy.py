
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

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



# tree using preorder and inorder
def buildtreeorder(preorder,inorder):
    #check length of both tree
    lengthpre = len(preorder)
    lenghtin = len(inorder)
    # check of both are equal
    if lengthpre != lenghtin or preorder == None or inorder == None or lengthpre == 0:
        return None
    #check index for root
    root = BinaryTreeNode(preorder[0])
    #assign a variable to root.data index in inorder
    rootindex = inorder.index(root.data)
    # assign left and right tree usign function
    
    root.left = buildtreeorder(preorder[1:rootindex + 1],inorder[:rootindex])
    root.right = buildtreeorder(preorder[rootindex + 1: ], inorder[rootindex + 1: ])
    return root
    

# Main
n=int(input())
preorder = [int(i) for i in input().strip().split()]

inorder = [int(i) for i in input().strip().split()]
root = buildtreeorder(preorder, inorder)

printLevelATNewLine(root)
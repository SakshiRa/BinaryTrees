# make a class
class BinaryTreeNode:
# create a init function, pass self and data
# init function
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
# take input from user
def TreeInput():
    # take root data as input
    rootData= int(input())
    # base case root -1, return none
    if rootData == -1:
        return None
    # make root data as root using BinaryTreeNode class
    root = BinaryTreeNode(rootData)
    # take left tree and right tree and use funstion treeinput
    leftTree = TreeInput()
    rightTree = TreeInput()
    # assign both to the left and right nodes
    root.left = leftTree
    root.right = rightTree
    
    return root


# count the number of nodes in tree
def NumNodes(root):
    if root == None:
        return 0
    leftcount = NumNodes(root.left)
    rightcount = NumNodes(root.right)
    return 1 + leftcount + rightcount



def sumOfAllNodes(root):
    
    if root == None:
        return 0
    left_sum = sumOfAllNodes(root.left)
    right_sum = sumOfAllNodes(root.right)
    return root.data + left_sum + right_sum

root = TreeInput()
print(NumNodes(root))
print(sumOfAllNodes(root))


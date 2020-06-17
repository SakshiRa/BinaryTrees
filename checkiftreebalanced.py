
# make a class
class BinaryTreeNode:
# create a init function, pass self and data
# init function
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
# print tree detailed
    # create a function
def PrintTreeDetailed(root):
    # base case root none
    if root == None:
        return
    # print root 
    print(root.data, end = ":")
    # print left tree data if not none
    if root.left != None:
        
        print("L",root.left.data, end ="," )
    # print right tree data if not None
    if root.right != None:
        print("R", root.right.data, end = " " )
    print()
    # call recusrion on both sides
    PrintTreeDetailed(root.left)
    PrintTreeDetailed(root.right)
    
    
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
 

# check height of tree
#count the number of nodes in left and right
# check max of both 
# return 1 plus max
def height(root):
    if root == None:
        return 0
    leftheight = height(root.left)
    rightheight = height(root.right)
    largest = max(leftheight,rightheight)
    return largest + 1
    
#check if tree is balanced
# if the height diff between left and right is more than one
#check height than minus form each
def checkbalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh - rh > 1 or rh - lh > 1:
        return False
    isleftbalanced = checkbalanced(root.left)
    isrightbalanced = checkbalanced(root.right)
    if isleftbalanced and isrightbalanced:
        return True
    else:
        return False

#checkbalanced improved
# check height and balance consecutively
def getheightandcheckbalanced(root):
    if root == None:
        return 0,True
    
    lh,isleftbalanced = getheightandcheckbalanced(root.left)
    rh,isrightbalanced = getheightandcheckbalanced(root.right)
    
    h = 1 + max(lh,rh)
    if lh-rh >1 or rh-lh > 1:
        return h,False
     
    if isleftbalanced and isrightbalanced:
        return h, True
    else:
        return h,False

root = TreeInput() 
PrintTreeDetailed(root)   
print(checkbalanced(root))
print(getheightandcheckbalanced(root))

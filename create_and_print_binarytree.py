# make a class
class BinaryTreeNode:
# create a init function, pass self and data
# init function
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
# print Tree
#create a function, pass root
def PrintTree(root):
    # base case root is none, return 
    if root == None:
        return
    # print root data
    print(root.data)
    # call func on both sides
    PrintTree(root.left)
    PrintTree(root.right)
    
    
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
    

    
# create nodes 
btn1 = BinaryTreeNode(1)
btn2 = BinaryTreeNode(2)
btn3 = BinaryTreeNode(3)

# join them
btn1.left = btn2
btn1.right = btn3


# print the tree         
PrintTree(btn1)        
# print tree detailed
PrintTreeDetailed(btn1)  
    


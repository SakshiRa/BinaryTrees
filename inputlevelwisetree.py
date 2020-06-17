
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


# print level wise tree
# import queue
import queue
# make function
def levelwisetree():
    q = queue.Queue()
# print enter root
    print("Enter Root:")
    #take input for root
    rootdata = int(input())
    #check root value
    if (rootdata == -1) :
        return None
    #create rootnode using Function of binarytreenode
    root = BinaryTreeNode(rootdata)
    # put in queue
    q.put(root)
    #check while q is not empty
    while (not (q.empty())):
        #check current node
        currentnode = q.get()
        #print enter left child of, currentnode
        print("Enter left child of:",currentnode.data)
        #take input of left child
        leftchilddata = int(input())
        #check if inpput is valid
        if leftchilddata != -1:
            # if valid then create leftnode using function binarytreenode
            leftchild = BinaryTreeNode(leftchilddata)
            # make that value as left node of currentnode
            currentnode.left = leftchild
            #put that value in queue
            q.put(leftchild)
            # repeat for right side
        
        #print enter right child of, currentnode
        print("Enter right child of:",currentnode.data)
        #take input of right child
        rightchilddata = int(input())
        #check if input is valid
        if rightchilddata != -1:
            # if valid then create rightnode using function binarytreenode
            rightchild = BinaryTreeNode(rightchilddata)
            # make that value as right node of currentnode
            currentnode.right = rightchild
            q.put(rightchild)
            
     # return root
    return root

root = levelwisetree() 
PrintTreeDetailed(root)








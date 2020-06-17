import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
               
        
        
# print the mirror image of tree
# make a temp left node
# make leftnode as right
#make rightnode as left
#call func on both        
def mirrortree(root):
    if root == None:
        return None
    left = root.left
    root.left = root.right
    root.right = left
    mirrortree(root.left)
    mirrortree(root.right)       




#remove the leaf nodes
#if the root does not have any left or right node than return None        
def removeleafnode(root):
    if root == None:
        return None
    if root.left and root.right == None:
        return None
    root.left = removeleafnode(root.left)
    root.right = removeleafnode(root.right)
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
    
    lh,checkbalanced = getheightandcheckbalanced(root.left)
    rh, checkbalanced = getheightandcheckbalanced(root.right)
    
    h = 1 + max(lh,rh)
    if lh-rh >1 or rh-lh > 1:
        return h,False
    
    if isleftbalanced and isrightbalanced:
        return h, True
    else:
        return h,False
    
    
#find diameter of tree
# find the height of left and right subtree
# comapre the max height plus root
#def diameter(root):
#    if 
    
# print level wise tree
# import queue
import queue
# make function
def levelwisetree(root):
    q = queue.Queue()
# print enter root
    print("Enter Root:")
    #take input for root
    rootdata = int(input())
    #check root value
    if root == -1 :
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
            leftchild = BinaryTreeNode(leftchild)
            # make that value as left node of currentnode
            currentnode.left = leftchild
            #put that value in queue
            # repeat for right side
        currentnode = q.get()
        #print enter right child of, currentnode
        print("Enter right child of:",currentnode.data)
        #take input of right child
        rightchilddata = int(input())
        #check if input is valid
        if rightchilddata != -1:
            # if valid then create rightnode using function binarytreenode
            rightchild = BinaryTreeNode(rightchild)
            # make that value as right node of currentnode
            currentnode.right = rightchild
            
     # return root
    return root
 
        
# print levelwisetree
    def printlevelwisetree(root):
        
# check if root is none
        if root == None:
            return
        #make a queue
        q = queue.Queue
        #put root in queue
        q.put(root)
        # work while q is not empty
        while (not(queue.empty())):
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
                
                
            print(currdata,":L:",left,"R:",right,sep = " ")


# tree using preorder and inorder
def buildtreeorder(preorder,inorder):
    #check length of both tree
    lengthpre = len(preorder)
    lenghtin = len(inorder)
    # check of both are equal
    if lengthpre != lenghtin or preorder == None or inorder == None or lengthpre == 0:
        return None
    #check index for root
    root = preoder[0]
    #assign a variable to root.data index in inorder
    rootindex = inorder.index(root.data)
    # assign left and right tree usign function
    
    root.left = buildtreeorder(preorder[1:rootindex + 1],inorder[:rootindex])
    root.right = buildtreeorder(preorder[rootindex + 1: ], inorder[rootindex + 1: ])
    return root
    
    
#build tree using postorder and inorder
def buildtreepostorder(postorder,inorder):
    lengthpost = len(postorder)       
    lengthin = len(inorder)
    if lenghtpost != lengthin or postorder == None or inorder == None or lengthin == 0:
        return None
    root = postorder[-1]
    rootindex = inorder.index(root.data)
    
    root.left = buildtreepostorder(postorder[:rootindex], inorder[:rootindex])
    root.right = buildtreepostorder(postorder[rootindex :-1],inorder[rootindex +1:])
    return root

    

root = removeleafnode(root)
mirrortree(root)
print(checkbalanced(root)
getheightandcheckbalanced(root)  
root = levelwisetree()
printlevelwisetree(root)
preorder = [int(i) for i in input().strip().split()]
inorder = [int(i) for i in input().strip().split()]
postorder = [int(i) for i in input().strip().split()]
root = buildtreeorder(preorder,inorder)


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
  

def preOrder(root):
    # Given a binary tree, print the preorder traversal of given tree. Pre-order
    # traversal is: Root LeftChild RightChild
    if root==None:
        return
    print(root.data, end=' ')
    preOrder(root.left)
    preOrder(root.right)

# Main
n=int(input())
lst=[int(i) for i in input().strip().split()]
root=BuildBSTusingArray(lst)
preOrder(root)
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root):
        if root == None:
            return
        print(root.data, end = ":")
        if root.left != None:
            print("L:",end='')
            print(root.left.data,end=',')
        if root.right != None:
            print("R:",end='')
            print(root.right.data,end='')
        print()
        self.printTreeHelper(root.left)
        self.printTreeHelper(root.right)
    
    def printTree(self):
        self.printTreeHelper(self.root)
    
    def searchhelper(self,root,data):
        if root == None:
            return False
        if root.data == data:
            return True
        if root.data > data:
            return self.searchhelper(root.left,data)
        else:
            return self.searchhelper(root.right,data)
        
    def search(self, data):
        return self.searchhelper(self.root,data)
    
        
    #Implement this function here
    def inserthelper(self,root,data):
        if root == None:
            node ==  BinaryTreeNode(data)
        return node 
        if data > root.data:
            root.right = self.inserthelper(root.left,data)
            return root
        else:
            root.left = self.inserthelper(root.right,data)
            return root
        
    def insert(self, data):
        self.numNodes += 1
        self.root = self.inserthelper(self.root,data)
        
    def min(self,data):
        if root == None:
            return 10000
        if root.left == None:
            return root.data
        return self.min(root.left)
            
    #Implement this function here
    def deletehelper(self,root,data):
        if root == None:
            return False,None
        if root.data > data:
            deleted,newleft = self.deletehelper(root.left,data)
            root.left = newleft
            return deleted,root
        
        if root.data < data:
            deleted,newright = self.deletehelper(root.right,data)
            root.right = newright
            return deleted, root
        
        if root.data == data:
            if root.right == None and root.left == None:
                return True,None
            if root.right != None and root.left == None:
                return True, root.right
            if root.right == None and root.left != None:
                return True, root.left
            
        replacement = self.min(root.right)
        root.data = replacement
        deleted, newrightnode = self.deletehelper(root.right,replacement)
        root.right = newrightnode
        return True, root
                
                
            
        
    def delete(self, data):
        deleted, newroot = self.deletehelper(self.root,data)
        if deleted:
            self.numNodes -= 1
            self.root = newroot
            return deleted
        
            
        
    #Implement this function here
    
    def count(self):
        return self.numNodes
b = BST()
li = [int(ele) for ele in input().split()]
i = 0
while(i < (len(li) )):
    choice = li[i]
    if choice == 1:
        data = li[i+1]
        b.insert(data)
        i+=2
    elif choice == 2:
        data = li[i+1]
        b.delete(data)
        i+=2
    elif choice == 3:
        data = li[i+1]
        ans = b.search(data)
        if ans is True:
            print('true')
        else:
            print('false')
        i+=2
    else:
        b.printTree()
        i+=1

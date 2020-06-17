import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def depth(root):
    if root == None:
        return 0
    left = depth(root.left)
    right = depth(root.right)
    return max(left,right) + 1


def diameterNdepth(root):
    dia,depth = 0,0
    if root == None:
        return dia, depth
    leftdia, leftdepth = diameterNdepth(root.left)
    rightdia, rightdepth = diameterNdepth(root.right)
    depth = max(leftdepth, rightdepth) + 1
    diameterwithroot = leftdepth + rightdepth + 1
    dia = max(leftdia, rightdia, diameterwithroot)
    return dia, depth
    

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
print(diameterNdepth(root))



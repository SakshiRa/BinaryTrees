#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 18:48:55 2019

@author: sakshirathi
"""

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
 

# remove leaf nodes  
def removeleafnodes(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeleafnodes(root.left)
    root.right = removeleafnodes(root.right)
    return root
    

   
root = TreeInput() 
PrintTreeDetailed(root)   
removeleafnodes(root)
PrintTreeDetailed(root)   